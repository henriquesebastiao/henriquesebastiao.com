---
layout: page
icon: fas fa-briefcase
order: 3
title: Portfolio
image: img/portfolio-en-preview-image.png
---

Below are some of the main projects I developed during my time studying and developing.
You can see all my other projects on the [projects](/en/projects/) page.

## [Dotum](/dotum/){:target="_blank"} - Accounts payable and receivable system

This project is a solution to a back-end programming challenge, the objective of which is to develop an application for managing accounts payable and accounts receivable. The proposal focuses on building solid logic, a well-organized code structure, and meeting functional requirements.

The web client was developed with [Streamlit](https://streamlit.io/){:target="_blank"}, while the back-end server was made using [FastAPI](https://fastapi.tiangolo.com/){:target="_blank"} and [SQLAlchemy](https://www.sqlalchemy.org/){:target="_blank"} for database management.

Deploy link (Web Client): [https://dotum-web.henriquesebastiao.com](https://dotum-web.henriquesebastiao.com/){:target="_blank"}

Demo video:

{% include embed/youtube.html id='uQxHBROBUQU' %}

### Features

- User registration and editing
- User login
- Accounts payable and receivable registration and editing
- Dashboard with general account information and a graph

### Technologies and tools used in the project

- **Python** with **FastAPI** for the backend.
- **SQLAlchemy** as an ORM for database communication.
- **Streamlit** for the frontend.
- **PostgreSQL** for data storage.
- **PyTest** for unit testing.
- **Docker** for containerized development.
- **GitHub Actions** for executing CI pipelines.

## [Poupy](/poupy/){:target="_blank"} - Personal expense management

Poupy is a web application for managing personal budgets and expenses, developed with Django. It allows complete financial control, including the management of bank accounts, income, expenses and balance transfers between accounts. With an intuitive dashboard, the user can quickly view a monthly financial summary and keep their finances organized.

Deployment link: [https://poupy.henriquesebastiao.com](https://poupy.henriquesebastiao.com/app/login){:target="_blank"}

Demo video:

{% include embed/youtube.html id='exrGsT3Y2WU' %}

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

### Technologies and tools used in the project

- **Python** with **Django** for the backend.
- **HTML5** and **CSS3** for the frontend.
- **PostgreSQL** for data storage.
- **PyTest** and **Selenium** for unit and functional testing.
- **Docker** for containerized development.
- **Ruff** for code formatting.
- **GitHub Actions** for running CI pipelines.

## [Saturn](/saturn/){:target="_blank"} - Firmware for the M5Stack Cardputer

A simple and functional firmware that implements several features for vulnerability analysis and even simple everyday tasks that can be performed with an M5Stack Cardputer (ESP32).

The firmware was developed using the C language with the Arduino platform, based on the [Nemo](https://github.com/n0xa/m5stick-nemo){:target="_blank"} project.

Video presenting the firmware:

{% include embed/youtube.html id='sE6ImWABvBE' %}

## [Manejo](/manejo/){:target="_blank"} - Cattle management modernization project

> This project is still in the development phase.
{: .prompt-info }

The management modernization project aims to provide a robust and efficient system for monitoring cattle management, enabling production and expense control, as well as assisting decision-making through herd performance analysis.

To date, the system has an async API developed with FastAPI, responsible for managing information related to animals, health events, weights, operational costs, and other data relevant to production. Data persistence is achieved through a PostgreSQL database, with schema versioning using Alembic.

The API follows best RESTful practices, with validations implemented using Pydantic, authentication based on JWT tokens, and automated testing with Pytest to ensure system reliability.

Furthermore, the project aims to incorporate:

- An administrative dashboard with interactive visualizations and reports;

- Integration with IoT devices for automated field data collection;

- Predictive analytics based on historical data;

- Intelligent notifications for critical management events.

The ultimate goal is to offer a modern, easy-to-use tool that can be adapted to different producer profiles, promoting digitalization and efficiency in beef and dairy farming.

API Preview Link: [https://manejo.henriquesebastiao.com/](https://manejo.henriquesebastiao.com/){:target="_blank"}

## [Timesheet](/timesheet/){:target="_blank"} - Time sheet

Timesheet is a time tracking application developed with Python, Django, and PostgreSQL, focused on simplicity and functionality.

The application uses the Django administrative interface (django-admin) to allow users to easily record their hours worked throughout the month. At the end of each period, a timesheet can be automatically generated in PDF format using the `reportlab` library.

Designed for individual use or small teams, Timesheet offers a practical solution for tracking work hours, keeping organized records, and quickly generating monthly reports.
