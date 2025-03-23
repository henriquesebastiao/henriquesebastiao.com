import sys

import requests

with open('links.txt', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file if line.strip()]

for link in urls:
    try:
        result = requests.get(link)
        if not 400 <= result.status_code <= 599:
            print(f'{link} -> {result.status_code}')
        else:
            print(f'\nERRO -> Falha na URL {link} -> {result.status_code}')
            sys.exit(1)
    except Exception as error:
        print(error)
        sys.exit(1)