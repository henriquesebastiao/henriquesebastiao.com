---
title: Como gosto de organizar um projeto Python
author: henriquesebastiao
date: 2024-01-18 11:24:00 -0400
categories: [Desenvolvimento, Python]
tags: [programacao, desenvolvimento, python]
published: false
image: /assets/img/preview-image-posts/2024/2024-01-18.png
---

Um guia de ferramentas que sempre uso em meus projetos pessoais Python para organizar o código e mais alguns truques.

Com o tempo aprendi a gostar de organizar meus códigos Python desde o início do projeto, seguindo a maneira que eu gosto de programar e também a PEP8. Grande parte dessas ferramentas conheci graças ao [@dunossauro](https://dunossauro.com/), e também algumas boas práticas.

Resolvi centralizar tudo aqui, assim sempre que eu iniciar um novo projeto posso pegar tudo aqui novamente hehe 😄.

Se você também gostar dessas dicas, me sentirei honrado em poder te ajudar. E se conhecer alguma outra maneira de organizar códigos, ficarei muito grato se compartilhar comigo!

## Ferramentas de desenvolvimento

- [Pytest](https://docs.pytest.org/), para testar meus projetos;
- [Coverage](https://coverage.readthedocs.io/), para saber se esqueci de testar algo;
- [Taskipy](https://github.com/taskipy/taskipy), uma forma de encurtar comandos enormes;
- [Blue](https://blue.readthedocs.io/en/latest/index.html), para seguir a PEP8 e formatar o código;
- [Ruff](https://docs.astral.sh/ruff/), um poderoso linter para Python;
- [Isort](https://pycqa.github.io/isort/), para organizar meus imports.
- [Bandit](https://bandit.readthedocs.io/), para verificar vulnerabilidades no código.
- [Radon](https://radon.readthedocs.io/), para verificar se não estou fazendo algo muito esquisito 😅.
- [Mypy](https://mypy.readthedocs.io/), um verificador de tipos run time.
- [Pydocstyle](https://www.pydocstyle.org/), para verificar se estou seguindo o padrão de docstrings.

```terminal
poetry add --group dev taskipy blue ruff isort pydocstyle "bandit[toml]" "radon[toml]" mypy pytest pytest-cov coverage-badge setuptols
```

## Ferramentas de documentação

- [Material for MkDocs](https://github.com/squidfunk/mkdocs-material/), um framework para a criação da documentação;
- [mkdocstrings](https://mkdocstrings.github.io/), uma ferramenta que gera documentação a partir das docstrings no código;
- [mkdocstrings-python](https://mkdocstrings.github.io/python/), o plugin de suporte python para o mkdocstrings.

```terminal
poetry add --group doc mkdocs-material mkdocstrings mkdocstrings-python mkdocs-macros-plugin jinja2 pygments pymdown-extensions mkdocs-git-committers-plugin-2 mkdocs-git-authors-plugin mkdocs-git-revision-date-localized-plugin
```

> Claro, para a maioria dos projetos não é necessário instalar todas essas ferraentas, vai depender do que você precisa. Talvez seu projeto não precise de documentação, ou de testes por exemplo.
{: .prompt-info }

## Configurações

```toml
[tool.ruff]
line-length = 79
indent-width = 4

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F403", "F401"]
"tests/*" = ["F401", "F811"]

[tool.isort]
profile = "black"
line_length = 79

[tool.taskipy.tasks]
ruff = "ruff check ."
blue = "blue --check . --diff"
isort = "isort --check --diff ."
mypy = "mypy -p <YOUR-PROJECT>"
radon = "radon cc ./<YOUR-PROJECT> -a -na"
bandit = "bandit -r ./<YOUR-PROJECT>"
pydocstyle = "pydocstyle ./<YOUR-PROJECT> --count --convention=google --add-ignore=D100,D104,D105,D107"
quality = "task mypy && task radon && task pydocstyle"
lint = "ruff check . && blue --check -S . --diff && isort --check --diff ."
format = "blue -S .  && isort ."
doc = "mkdocs serve"
pre_test = "task lint"
test = "pytest -s -x --cov=<YOUR-PROJECT> -vv"
post_test = "coverage run -m pytest && coverage html"
badge = "coverage-badge -o docs/assets/coverage.svg -f"
ready = "task lint && task quality && task bandit && pytest -s -x --cov=<YOUR-PROJECT> -vv && coverage html && task export-requirements && task export-requirements-doc && task badge"

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

Mesmo que eu use poetry em um projeto, gosto de criar um arquivo de `requirements.txt` para duas coisas:

- Informar ao PyCharm quais são as dependências do meu projeto;
- E durante o fluxo do Github Actions para instalar as dependências com pip.

Para criar o arquivo:

```terminal
pip freeze > requirements.txt
```

Ou:

```terminal
poetry export --with dev --without-hashes --without-urls --output requirements.txt
```

## Padrões de código

Para docstrings sempre uso o padrão do [Google Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Me parece muito mais consiso o bonito.

## Integração Contínua com GitHub Actions

Sempre configuro pipelines para meus projetos, assim caso eu esqueça de verificar algo antes de efetuar o push, o fluxo de trabalho do GitHub Actions realiza todas as verificações incluindo linters e testes, e envia uma notificação direto para meu celular informando se está tudo ok.

### Trabalhos incluídos no ci.yml

- [Ruff](https://docs.astral.sh/ruff/), linter para checar se estou seguindo a PEP8;
- [Isort](https://pycqa.github.io/isort/), verifica se meus imports estão ordenados;
- Testes, executa todos os testes com [Pytest](https://docs.pytest.org/) e envia o relatório de cobertura para o Codecov.

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
      - uses: chartboost/ruff-action@v1
        with:
          version: "0.1.3"

  isort:
    name: Isort
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: isort/isort-action@v1
        with:
          configuration: "--profile black -l 79"
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
