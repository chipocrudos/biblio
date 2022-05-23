
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