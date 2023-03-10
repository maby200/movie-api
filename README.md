## Django movie app
<!-- Copiar lo de mi cuaderno. Es algo pequeño -->

```bash
pip install djangorestframework
```

En `movies/setting.py` añadir:
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
--> 'rest_framework',
    'movie'
]
```

Con rest_framework se crean serializers.py en cada app, en este caso: `movie` (no `movies`, este es el proyecto)

- En `serializers.py`,  `__all__` sirve para jalar todos los campos del modelo

- En `views.py` se importan tanto el modelo como el serializador 
    `from rest_framweork import viewsets` permite que la vista ya venga con el CRUD implementado

- Una vez creado ModelViewSet se va a urls.py de la app y se importa:
`from rest_framework import routers`. Este módulo tiene DefaultRouter y SimpleRouter

Entrar a localhost:8000/movie y saldrá opción para agregar una película. Una vez se haya creado, se podrá ver el json con los datos de la película creada y podrás añadir más.

Ahora generaremos documentación con yasg (Yet Another Swagger Generator)
ASEGURATE ESTAR EN TU ENTORNO VIRTUAL :')
```bash
(.env)$ pip install drf-yasg
```
Añadir drf-yasg en `settings.py`
```py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'movie',
--> 'drf_yasg'
]
```
Como es de esperarse, se usará en el archivo `urls.py` global para importar _yasg_, sino no generaría la documentación para todas las rutas que se tienen.

Importar lo siguiente:
```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
```
get_schema_view permmitirá crear el documento de la API, x ejemplo OpenAPIinfo