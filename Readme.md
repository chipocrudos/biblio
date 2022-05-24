
# Biblio

Ejercicios de biblioteca


Requerimientos:
> django
> djangorestframework
> djangorestframework-simplejwt
> djoser
> django-cors-headers
> drf-yasg
> django-environ


Variables de entorno copiar env_example a .env

```bash
DEBUG=True
SECRET_KEY=
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///${PWD}/biblio/db.sqlite3
DJANGO_ADMINS=Nombre Completo <correo@electronico.com>
DEFAULT_FROM_EMAIL=otrocorreo@electronico.com
EMAIL_URL=smtp+tls://email:pass@smtp.gmail.com:587
CORS_DOMAINS=http://localhost:3000,http://127.0.0.1:3000
ACCESS_TOKEN_LIFETIME=1
REFRESH_TOKEN_LIFETIME=7
```


Volcar datos de prueba
```bash
pipenv run manage dumpdata --format json --indent 4 users > users.json
pipenv run manage dumpdata --format json --indent 4 library > library.json
```

Cargar datos de prueba
```bash
pipenv run manage loaddata users.json
pipenv run manage loaddata library.json
```

Documentación de la api
> http://\<HOSTNAME>:\<PORT>/docs/
> http://\<HOSTNAME>:\<PORT>/redocs/


* [pipenv doc](https://pipenv-es.readthedocs.io/es/latest/)
* [set enviroment variables in python venv](https://www.roelpeters.be/set-environment-variables-in-virtual-environment-python/)
* [django environ](https://django-environ.readthedocs.io/en/latest/)