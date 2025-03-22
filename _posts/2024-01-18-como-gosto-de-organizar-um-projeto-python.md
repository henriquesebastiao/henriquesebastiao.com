---
title: Como gosto de organizar um projeto Python
description: Um guia de técnicas e ferramentas para organizar projetos Python.
author: henriquesebastiao
date: 2024-01-18 11:24:00 -0400
categories: [Desenvolvimento, Python]
tags: [programacao, desenvolvimento, python]
published: false
image: /8e0d4d90-e1d7-440a-36f2-44efd0205a00/public
---

Organizar um projeto Python de forma eficiente é essencial para garantir a coesão, a colaboração e a manutenção do código a longo prazo. Seja para um pequeno script ou uma aplicação completa, adotar boas práticas desde o início pode economizar tempo e evitar dores de cabeça no futuro.

Neste post, vamos explorar ferramentas e técnicas que irão nos ajudar a organizar nosso projeto, utilizando ferramentas como Poetry, Ruff e Taskipy além de outras que ajudam na organização do código, na documentação de dependências e na automação de tarefas.

Se você também gostar dessas dicas, me sentirei honrado em poder te ajudar.

## Ferramentas de desenvolvimento

- [Pytest](https://docs.pytest.org/), para testar meus projetos;
- [Coverage](https://coverage.readthedocs.io/), para saber se esqueci de testar algo;
- [Taskipy](https://github.com/taskipy/taskipy), uma forma de encurtar comandos enormes;
- [Ruff](https://docs.astral.sh/ruff/), para seguir a PEP8 e formatar o código;
- [Bandit](https://bandit.readthedocs.io/), para verificar vulnerabilidades no código.
- [Radon](https://radon.readthedocs.io/), para verificar se não estou fazendo algo muito esquisito 😅.
- [Mypy](https://mypy.readthedocs.io/), um verificador de tipos run time.

```terminal
poetry add --group dev taskipy ruff "bandit[toml]" "radon[toml]" mypy pytest pytest-cov coverage-badge setuptols
```

## Ferramentas de documentação

- [Material for MkDocs](https://github.com/squidfunk/mkdocs-material/), um framework para a criação da documentação;
- [mkdocstrings](https://mkdocstrings.github.io/), uma ferramenta que gera documentação a partir das docstrings no código;
- [mkdocstrings-python](https://mkdocstrings.github.io/python/), o plugin de suporte python para o mkdocstrings.

```terminal
poetry add --group doc mkdocs-material mkdocstrings mkdocstrings-python mkdocs-macros-plugin jinja2 pygments pymdown-extensions mkdocs-git-committers-plugin-2 mkdocs-git-authors-plugin mkdocs-git-revision-date-localized-plugin
```

> Claro, para a maioria dos projetos não é necessário instalar todas essas ferramentas, vai depender do que você precisa. Talvez seu projeto não precise de documentação, ou de testes por exemplo.
{: .prompt-info }

## Configurações

```toml
[tool.ruff]
line-length = 79
indent-width = 4

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

[tool.ruff.format]
preview = true
quote-style = 'single'

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F403", "F401"]
"tests/*" = ["F401", "F811"]

[tool.taskipy.tasks]
mypy = "mypy -p <YOUR-PROJECT>"
radon = "radon cc ./<YOUR-PROJECT> -a -na"
bandit = "bandit -r ./<YOUR-PROJECT>"
lint = 'ruff check .; ruff check . --diff'
format = 'ruff format .; ruff check . --fix'
quality = "task mypy && task radon && task pydocstyle"
doc = "mkdocs serve"
pre_test = "task lint"
test = "pytest -s -x --cov=<YOUR-PROJECT> -vv"
post_test = "coverage run -m pytest && coverage html"

[tool.mypy]
ignore_missing_imports = true
check_untyped_defs = true

[tool.coverage.run]
source = [
    "<YOUR-PROJECT>",
]
omit = [
    "/tests/*",
]

[tool.pytest.ini_options]
pythonpath = "."
addopts = "--doctest-modules"
python_files = "test.py tests.py test_*.py tests_*.py *_test.py *_tests.py"
```
{: file="pyproject.toml" }

## requirements.txt

Mesmo que use Poetry durante o desenvolvimento do seu projeto, pode ser que queira criar um arquivo de `requirements.txt` para instalar as dependências com pip, seja em ambiente de produção ou durante workflows de CI.

Para criar o arquivo:


```terminal
poetry export --with dev --without-hashes --without-urls --output requirements.txt
```

## Padrões de código

Para docstrings sempre uso o padrão do [Google Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Me parece muito mais consiso o bonito.

## Integração Contínua com GitHub Actions

Sempre configuro pipelines para meus projetos, assim caso eu esqueça de verificar algo antes de efetuar o push, o fluxo de trabalho do GitHub Actions realiza todas as verificações incluindo linters e testes, e envia uma notificação direto para meu celular informando se está tudo ok.

### Trabalhos incluídos no ci.yml

- [Ruff](https://docs.astral.sh/ruff/), linter para checar se estou seguindo a PEP8;

**AVISO**

Substitua o trecho `<NAME-OF-YOUR-PYTHON-PACKAGE>` pelo nome do seu pacote!

```yml
on: [ push, pull_request ]

name: CI

jobs:
  ruff:
    name: Ruff
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/ruff-action@v3
```
{: file=".github/workflows/ci.yml" }

## Mensagens de commit

Priorizo o uso de mensagens semânticas para os commits. Sempre procuro referências neste [repositório](https://github.com/iuricode/padroes-de-commits) de [Iuri Silva](https://github.com/iuricode).

## Por que não descontrair um pouco?

Sempre desenvolvemos projetos que são úteis para resolver alguns problemas, mas pode ser que este projeto não seja muito sério, ou que tenha sido feito apenas por diversão. Nesse caso, gosto de licenciar meu projeto sob a licença BEER-WARE, haha.

Isso significa que você pode fazer o que quiser com o meu código. Se nos encontrarmos algum dia, e você achar que vale a pena, você pode me pagar uma cerveja 😁.

```
/*
* ---------------------------------------------------------------------------------
* "THE BEER-WARE LICENSE":
* <contato@henriquesebastiao.com> wrote this file. If you are reading this license,
* as long as you keep this note, you can do whatever you want with this code.
* If we meet someday, and you think it's worth it, you can buy me a beer.
* Henrique Sebastião
* ---------------------------------------------------------------------------------
*/
```
{: file="LICENSE" }


```
/*
* --------------------------------------------------------------------------------------------
* "THE BEER-WARE LICENSE":
* <contato@henriquesebastiao.com> escreveu este arquivo. Se voce estiver lendo essa licensa,
* contanto que mantenha esta nota, voce poderá fazer o que quiser com este código.
* Se nos encontrarmos algum dia, e você achar que vale a pena, você pode me pagar uma cerveja.
* Henrique Sebastião
* --------------------------------------------------------------------------------------------
*/
```
{: file="LICENSE" }
