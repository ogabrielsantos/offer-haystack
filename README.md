# Offer Haystack

Prova de conceito feita com Django, ElasticSearch e Django-Haystack.

Requisitos:
- Python 3.4+
- VirtualEnv
- ElasticSearch
- MySQL ou MariaDB


Crie um virtualenv
```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Instale as dependencias:
```bash
$ pip install -r requirements.txt
```

Edite o arquivo "settings.py" dentro da pasta "vagas".
Procure o dicionário chamado "DATABASES" e insira as configurações da base de dados.

Para inicializar a base de dados:
```bash
$ python manage.py migrate
```

Para recompilar os indices:
```bash
$ python manage.py rebuild_index
```

Para rodar a aplicação:
```bash
$ python manage.py runserver
```
E acesse http://localhost:9000/admin e cadastre novas ofertas.

Para criar um usuário novo:
```
$ python manage.py createsuperuser
```

