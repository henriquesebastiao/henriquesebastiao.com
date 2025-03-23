import sys
import ssl
import certifi
from pprint import pprint

import httpx
from rich.console import Console
from rich.pretty import Pretty

console = Console()
client = httpx.Client()
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0'}

file = sys.argv[1]

with open(file, 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file if line.strip()]

for link in urls:
    try:
        result = client.get(link, headers=headers)
        if not 400 <= result.status_code <= 599:
            console.print(f'{link} -> [bold green]{result.status_code}[/bold green]')
        else:
            console.print(f'\n[bold red]ERRO[/bold red] -> Falha na URL {link} -> {result.status_code}')
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
        print(error)
        sys.exit(1)