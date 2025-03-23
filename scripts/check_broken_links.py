import sys
from contextlib import contextmanager
from datetime import datetime
from pprint import pprint
from queue import Queue
from threading import Event, Thread

import httpx
from decouple import config
from rich.console import Console

DEBUG = config('DEBUG', default=False, cast=bool)

console = Console()
client = httpx.Client()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'
}

event = Event()
fila = Queue(maxsize=101)


def printd(*args):
    if DEBUG:
        print(*args)


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print(f'Tempo de execução (hh:mm:ss.ms) {time_elapsed}')


def get_links():
    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        [fila.put(line.strip()) for line in file if line.strip()]
    event.set()
    fila.put('Kill')


def check_broken_link(url):
    try:
        result = client.get(
            url, headers=headers, timeout=10, follow_redirects=True
        )
        if not 400 <= result.status_code <= 599:
            console.print(
                f'{url} -> [bold green]{result.status_code}[/bold green]'
            )
        else:
            console.print(
                f'\n[bold red]ERRO[/bold red] -> Falha na URL {url} -> {result.status_code}'
            )
            print('\nRESPONSE:')
            print('Headers:')
            pprint(vars(result.headers))
            print('Extensions:')
            pprint(result.extensions)

            print('\nREQUEST:')
            pprint(result._request.method)
            pprint(result._request.url)
            pprint(result._request.headers)

            sys.exit(1)
    except Exception as error:
        print(f'\n{error}')
        console.print(f'[bold red]ERRO[/bold red] -> Falha na URL {url}')
        sys.exit(1)


def pipeline(*funcs):
    def inner(argument):
        state = argument
        for func in funcs:
            state = func(state)

    return inner


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        printd(self.name, 'started')

    def run(self):
        event.wait()
        while not self.queue.empty():
            link = self.queue.get()
            printd(self.name, link)
            if link == 'Kill':
                self.queue.put(link)
                self._stoped = True
                break
            self._target(link)

    def join(self):
        while not self._stoped:
            pass


def get_pool(n_th: int):
    """Retorna um número n de Threads."""
    return [
        Worker(target=target, queue=fila, name=f'Worker{n}')
        for n in range(n_th)
    ]


target = pipeline(check_broken_link)

with timeit():
    get_links()
    printd(fila.queue)
    threads = get_pool(10)
    printd('starts')
    [th.start() for th in threads]
    printd('joins')
    [th.join() for th in threads]
