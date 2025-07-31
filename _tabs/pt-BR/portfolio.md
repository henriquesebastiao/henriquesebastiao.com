---
layout: page
icon: fas fa-briefcase
order: 3
title: Portfólio
image: /11aa8482-8fee-4a90-c712-67c55f9cca00/public
---

Alguns dos projetos que desenvolvi durante esse tempo de estudo em desenvolvimento.

## [Poupy](/poupy/){:target="_blank"}

Poupy é um aplicativo web para gerenciamento de orçamento e gastos pessoais, desenvolvido com Django. Ele permite o controle financeiro completo, incluindo a gestão de contas bancárias, receitas, despesas e transferências de saldo entre contas. Com um dashboard intuitivo, o usuário pode visualizar rapidamente um resumo financeiro mensal e manter suas finanças organizadas.

Link do deploy: [https://poupy.henriquesebastiao.com](https://poupy.henriquesebastiao.com/app/login){:target="_blank"}

> Na página de login, clique no botão <kbd>Login as Demo User</kbd> para ver uma demonstração das funcionalidades do app.
{: .prompt-tip }

### Funcionalidades

- **Adição de contas bancárias**: Adicione e gerencie várias contas bancárias.
- **Registro de receitas e despesas**: Registre suas entradas e saídas de dinheiro para melhor controle.
- **Transferência entre contas**: Movimente saldo entre contas cadastradas.
- **Dashboard completo:**
    - Saldo total de todas as contas.
    - Total de entradas e saídas mensais para um resumo rápido do fluxo financeiro.
    - Saldo por conta para acompanhar a situação de cada conta individualmente.
    - Maiores movimentações: Exibe as três maiores movimentações do mês, destacando receitas e despesas mais significativas.

Tecnologias e ferramentas usadas no projeto:

- **Python** com **Django** para o backend.
- **HTML5** e **CSS3** para o frontend.
- **PostgreSQL** para armazenamento de dados.
- **PyTest** e **Selenium** para testes unitários e funcionais.
- **Docker** para desenvolvimento em containers.
- **Ruff** para formatação de código.
- **GitHub Actions** para execução de pipelines de CI.

## [Skyport ✨](/skyport/){:target="_blank"}

Skyport é um CLI para obter informações de objetos astronômicos diretamente pelo terminal, desenvolvido com Typer e consumindo API pública da NASA. O projeto está sendo desenvolvido com o intuito de aprender mais sobre desenvolvimento de CLIs e consumo de APIs. Tenho muito entusiasmo com este projeto, uma vez que me permite unir duas coisas que gosto: astronomia e o desenvolvimento.

O CLI tem uma documentação completa desenvolvida com MkDocs e hospedada no Read the Docs. Você pode acessá-la [aqui](https://skyport.henriquesebastiao.com){:target="_blank"}.

## [Netmikro](/netmikro/){:target="_blank"}

Netmikro é uma biblioteca simples que fornece uma abstração para facilitar o gerenciamento roteadores Mikrotik usando Python, simplificando tarefas de configuração e monitoramento. Usando a poderosa biblioteca `Netmiko` para gerar uma conexão SSH com o roteador, a biblioteca Netmikro fornece uma interface mais amigável para realizar tarefas comuns de gerenciamento de roteadores Mikrotik.

Um exemplo de uso da biblioteca:

```python
>>> from netmikro import RouterOS
>>> router = RouterOS(
    '192.168.3.3',
    'user',
    'password',
    22,
)
>>> router.cmd('/system identity print')
MikroTik

# Ou simplesmente lendo o atributo `identity`
>>> router.identity
MikroTik
```
{: .nolineno }

## [Timesheet](/timesheet/){:target="_blank"}

Timesheet é um app de folha de ponto desenvolvido com Python, Django e PostgreSQL. Usando o django-admin para interagir com a plicação, o app permite que o usuário registre suas horas trabalhadas e gere o PDF (com `reportlab`) da folha de ponto ao fim do mês.

