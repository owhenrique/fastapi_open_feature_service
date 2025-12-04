# Open-Feature-Service

## Objetivo

Este projeto é um fork do [LaunchDarkly](https://launchdarkly.com/), porém open-source. O LaunchDarkly é uma SaaS para assistência de deploy de novas features em sua aplicação. Algumas das funcionalidades do Open-Feature-Service são:

- Habilitar/desabilitar funcionalidades remotamente
- Gerenciar configurações dinâmicas
- Segmentar usuário (ex.: [percentual rollout](#percentual-rollout))
- Expor uma API consumível por apps Web/Mobile/Backend

## Tech Stack

- Python 3.12+
- FastAPI
- SQLite
- Redis
- Docker

## Instalação

Clone este repositório e execute o seguinte comando no seu terminal:

```CMD
git clone git@github.com:<nome-do-usuário>/<nome-do-repositorio>.git
```

E navegue até o diretório do repositório com o seguinte comando:

```CMD
cd <nome-do-repositorio>
```

Pronto! Desta forma você já estará dentro do diretório do repositório e poderá os comandos de execução.

## Execução

Para executar o projeto são necessárias mais algumas dependências, sendo elas:

- [Poetry](https://python-poetry.org/docs/#installation)
- [Plugin 'poetry shell'](https://github.com/python-poetry/poetry-plugin-shellv)

E pronto, você já poderá executar o projeto!

Primeiro você irá ativar o ambiente virtual com o seguinte comando:

```CMD
$ <diretorio-do-projeto>/ poetry shell
```

Depois você deve instalar as dependências do projeto com o seguinte comando:

```CMD
$ <diretorio-do-projeto>/ poetry install
```

Após isso você já estará pronto para rodar o projeto com o seguinte comando:

```CMD
$ <diretorio-do-projeto>/ fastapi dev src/app/main.py
```

E se tudo der certo você verá a seguinte mensagem no terminal:

```CMD
   FastAPI   Starting development server 🚀

             Searching for package file structure from directories with __init__.py files
             Importing from /home/paulo/Documentos/projects/open-feature-service/src

    module   📁 app
             ├── 🐍 __init__.py
             └── 🐍 main.py

      code   Importing the FastAPI app object from the module with the following code:

             from src.app.main import app

       app   Using import string: src.app.main:app

    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs

       tip   Running in development mode, for production use: fastapi run

             Logs:

      INFO   Will watch for changes in these directories:
             ['open-feature-service']
      INFO   Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
      INFO   Started reloader process [29799] using WatchFiles
      INFO   Started server process [29801]
      INFO   Waiting for application startup.
      INFO   Application startup complete.
```

### [Percentual rollout](#percentual-rollout)

Ação de lançar algo (como uma atualização de software ou infraestrutura) para uma porcentagem específica de usuários ou áreas de cada vez.

Projeto desenvolvido por [@owhenrique](https://github.com/owhenrique)
