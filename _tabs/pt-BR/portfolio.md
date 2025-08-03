---
layout: page
icon: fas fa-briefcase
order: 3
title: Portfólio
image: img/portfolio-preview-image.png
---

Abaixo estão listados alguns dos principais projetos que desenvolvi durante esse tempo de estudo em desenvolvimento.
Você pode ver todos os meus demais projetos na página de [projetos](/projects/).

## [Dotum](/dotum/){:target="_blank"} - Sistema de contas a pagar e a receber

Este projeto é uma solução para um desafio de programação back-end, cujo objetivo é desenvolver uma aplicação para o controle de contas a pagar e contas a receber. A proposta foca na construção de uma lógica sólida, estrutura de código bem organizada e cumprimento dos requisitos funcionais.

O cliente web foi desenvolvido com [Streamlit](https://streamlit.io/){:target="_blank"}, enquanto o servidor back-end foi feito utilizando [FastAPI](https://fastapi.tiangolo.com/){:target="_blank"} e [SQLAlchemy](https://www.sqlalchemy.org/){:target="_blank"} para gestão do banco de dados.

Link do deploy (Cliente Web): [https://dotum-web.henriquesebastiao.com](https://dotum-web.henriquesebastiao.com/){:target="_blank"}

Vídeo de demonstração:

{% include embed/youtube.html id='uQxHBROBUQU' %}

### Funcionalidades

- Cadastro e edição de usuários
- Login de usuários
- Registro e edição de contas a pagar e a receber
- Dashboard com informações gerais das contas com um gráfico

### Tecnologias e ferramentas usadas no projeto

- **Python** com **FastAPI** para o backend.
- **SQLAlchemy** como ORM para comunicação com o banco de dados.
- **Streamlit** para o frontend.
- **PostgreSQL** para armazenamento de dados.
- **PyTest** para testes unitários.
- **Docker** para desenvolvimento em containers.
- **GitHub Actions** para execução de pipelines de CI.

## [Poupy](/poupy/){:target="_blank"} - Gestão de gastos pessoais

Poupy é um aplicativo web para gerenciamento de orçamento e gastos pessoais, desenvolvido com Django. Ele permite o controle financeiro completo, incluindo a gestão de contas bancárias, receitas, despesas e transferências de saldo entre contas. Com um dashboard intuitivo, o usuário pode visualizar rapidamente um resumo financeiro mensal e manter suas finanças organizadas.

Link do deploy: [https://poupy.henriquesebastiao.com](https://poupy.henriquesebastiao.com/app/login){:target="_blank"}

Vídeo de demonstração:

{% include embed/youtube.html id='exrGsT3Y2WU' %}

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

### Tecnologias e ferramentas usadas no projeto

- **Python** com **Django** para o backend.
- **HTML5** e **CSS3** para o frontend.
- **PostgreSQL** para armazenamento de dados.
- **PyTest** e **Selenium** para testes unitários e funcionais.
- **Docker** para desenvolvimento em containers.
- **Ruff** para formatação de código.
- **GitHub Actions** para execução de pipelines de CI.

## [Saturn](/saturn/){:target="_blank"} - Firmware para o M5Stack Cardputer

Um firmware simples e funcional que implementa diversas funcionalidades para análise de vulnerabilidades e até mesmo tarefas simples do dia a dia que podem ser realizadas com um M5Stack Cardputer (ESP32).

O firmware foi desenvolvido usando a linguagem C com a plataforma Arduino, usando como base o projeto [Nemo](https://github.com/n0xa/m5stick-nemo){:target="_blank"}.

Vídeo apresentando o firmware:

{% include embed/youtube.html id='sE6ImWABvBE' %}

## [Manejo](/manejo/){:target="_blank"} - Projeto de modernização do manejo

> Este projeto ainda está em fase de desenvolvimento.
{: .prompt-info }

O projeto de modernização do manejo visa proporcionar um sistema robusto e eficiente para o acompanhamento do manejo de bovinos, possibilitando o controle de produção e gastos, assim como auxiliar na tomada de decisões por meio da análise de performance do rebanho.

Até o momento o sistema conta com uma API async desenvolvida com FastAPI, responsável por gerenciar informações relacionadas aos animais, eventos sanitários, pesos, custos operacionais e demais dados relevantes à produção. A persistência dos dados é feita por meio de um banco de dados PostgreSQL, com versionamento de esquema utilizando Alembic.

A API segue boas práticas RESTful, com validações implementadas usando Pydantic, autenticação baseada em tokens JWT e testes automatizados com Pytest para garantir a confiabilidade do sistema.

Além disso, o projeto visa incorporar futuramente:

- Um painel administrativo com visualizações e relatórios interativos;

- Integração com dispositivos IoT para coleta automatizada de dados em campo;

- Análises preditivas com base em dados históricos;

- Notificações inteligentes para eventos críticos no manejo.

O objetivo final é oferecer uma ferramenta moderna, de fácil uso e adaptável a diferentes perfis de produtores, promovendo a digitalização e a eficiência na pecuária de corte e leite.

Link de pré-visualização da API: [https://manejo.henriquesebastiao.com/](https://manejo.henriquesebastiao.com/){:target="_blank"}

## [Timesheet](/timesheet/){:target="_blank"} - Folha de ponto

Timesheet é um aplicativo de controle de ponto desenvolvido com Python, Django e PostgreSQL, focado na simplicidade e funcionalidade.

A aplicação utiliza a interface administrativa do Django (django-admin) para permitir que os usuários registrem facilmente suas horas trabalhadas ao longo do mês. Ao final de cada período, é possível gerar automaticamente a folha de ponto em formato PDF, utilizando a biblioteca `reportlab`.

Projetado para uso individual ou em pequenos times, o Timesheet oferece uma solução prática para acompanhar a jornada de trabalho, manter registros organizados e gerar relatórios mensais com agilidade.
