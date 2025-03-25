---
layout: page
icon: fas fa-briefcase
order: 3
title: Portfolio
image: /11aa8482-8fee-4a90-c712-67c55f9cca00/public
---

Some of the projects I developed during this time of study in development.

## [Poupy](/poupy/){:target="_blank"}

Poupy is a web application for managing personal budgets and expenses, developed with Django. It allows complete financial control, including the management of bank accounts, income, expenses and balance transfers between accounts. With an intuitive dashboard, the user can quickly view a monthly financial summary and keep their finances organized.

Deployment link: [https://poupy.henriquesebastiao.com](https://poupy.henriquesebastiao.com/app/login){:target="_blank"}

> On the login page, click the <kbd>Login as Demo User</kbd> button to see a demo of the app's features.
{: .prompt-tip }

### Features

- **Adding bank accounts**: Add and manage multiple bank accounts.
- **Recording income and expenses**: Record your money inflows and outflows for better control.
- **Transferring between accounts**: Move balances between registered accounts.
- **Complete dashboard:**
    - Total balance of all accounts.
    - Total monthly inflows and outflows for a quick summary of financial flow.
    - Balance by account to monitor the status of each account individually.
    - Largest transactions: Displays the three largest transactions of the month, highlighting the most significant income and expenses.

Technologies and tools used in the project:

- **Python** with **Django** for the backend.
- **HTML5** and **CSS3** for the frontend.
- **PostgreSQL** for data storage.
- **PyTest** and **Selenium** for unit and functional testing.
- **Docker** for containerized development.
- **Ruff** for code formatting.
- **GitHub Actions** for running CI pipelines.

## [Skyport ✨](/skyport/){:target="_blank"}

Skyport is a CLI to get information about astronomical objects directly from the terminal, developed with Typer and consuming NASA's public API. The project is being developed with the intention of learning more about CLI development and API consumption. I am very excited about this project, since it allows me to combine two things I like: astronomy and development.

The CLI has comprehensive documentation developed with MkDocs and hosted on Read the Docs. You can access it [aqui](https://skyport.henriquesebastiao.com){:target="_blank"}.

## [Netmikro](/netmikro/){:target="_blank"}

Netmikro is a simple library that provides an abstraction to facilitate the management of Mikrotik routers using Python, simplifying configuration and monitoring tasks. Using the powerful `Netmiko` library to generate an SSH connection to the router, the Netmikro library provides a more user-friendly interface to perform common Mikrotik router management tasks.

An exploration of the library's usage:

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

# Or simply reading the `identity` attribute
>>> router.identity
MikroTik
```
{: .nolineno }

## [Timesheet](/timesheet/){:target="_blank"}

Timesheet is a timesheet app developed with Python, Django and PostgreSQL. Using django-admin to interact with the application, the app allows the user to record their hours worked and generate a PDF (with `reportlab`) of the timesheet at the end of the month.

