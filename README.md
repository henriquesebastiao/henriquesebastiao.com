# 📝 Blog pessoal e Portifólio

[![Deploy](https://github.com/henriquesebastiao/henriquesebastiao.com/actions/workflows/deploy.yml/badge.svg)](https://github.com/henriquesebastiao/henriquesebastiao.com/actions/workflows/deploy.yml)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fhenriquesebastiao.com%2F)](https://henriquesebastiao.com)
[![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=flat&logo=Cloudflare&logoColor=white)](https://henriquesebastiao.com/)

A ideia aqui é ter um lugar sob o meu controle, onde eu possa compartilhar meus pensamentos, percepções e devaneios.
Já há algum tempo em que venho cogitando a abordagem que mais me agradasse para escrever meus posts,
depois de algum tempo testanddo essa implementação com Jekyll cheguei a conclusão de que vou seguir por esse caminho.
Primeiro porque escrever em Markdown me é agradável e simples, mas principalmente porque é portável.

### 🛠️ Construindo

Para instalar as dependências de desenvolvimento, siga os seguintes passos:

1. Instale o `ruby` e o `rubygems`.
2. Instale o `bundler` com o comando:

```shell
gem install bundler
```

3. Configure o bundler para instalar as dependências do projeto na pasta do projeto:

```shell
bundle config set --local path '.bundle'
```

4. Instale as dependências:

```shell
bundle install
```

5. Por fim inicialize a aplicação:

```shell
make run
```
