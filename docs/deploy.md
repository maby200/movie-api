# Steps for deployment

1- Install dependencies

```bash
pip install gunicorn
pip install django-environ
pip install mysqlclient
pip install whitenoise
```

2- Create requirements.txt:
```bash
pip freeze > requirements.txt
```

3- Create a file with name: `Procfile` and inside this file:

```
web: python manage.py migrate && gunicorn movies.wsgi
```

4- Create database in railway
[Railway app](http://railway.app)

5- Create a .env file and Set project variables. (See .env.example for more info)
```python
# example:
#you have this link to your database in railway:
# mysql -h containers-**##.railway.app -u root -p ##**BkM8W**## --port 5432 --protocol=TCP railway

# you should write the following based on that link:
MYSQLDATABASE=railway
MYSQLUSER=root
MYSQLPASSWORD=##**BkM8W**##
MYSQLHOST=containers-**##.railway.app
MYSQLPORT=5432
```

6- Modify `settings.py`:
```python
import environ
import os

# Configuration for django_environ
env = environ.Env(DEBUG=(bool, False))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

...
# Modify installed apps and middleware
INSTALLED_APPS = [
  ...
  'django.contrib.staticfiles', # this comes by default
  'whitenoise.runserver_nostatic',
  ...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',# this comes by default
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

...
#make sure it is the following way

WSGI_APPLICATION = 'movies.wsgi.application'

...

# configure database connection
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('MYSQLDATABASE'),
        'PORT': env('MYSQLPORT'),
        'USER': env('MYSQLUSER'),
        'PASSWORD': env('MYSQLPASSWORD'),
        'HOST': env('MYSQLHOST'),
    }
}

...

STATIC_URL = '/static/' # esta linea ya existe sólo añadirle "/" al final
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```

- If not deployed correctly due to issues in database connection:
  - You should add manually each of the previous credentials:
    ```
    MYSQLDATABASE=...
    ...
    ```
    _If you upload an `.env.example` to your repo the variables will be automatically added to the deployment but since these have not the actual credentials it will fail so manually insert the values for each of them._
  
- When deployed:
```
ALLOWED_HOSTS = ["localhost", "movie-api-production-412e.up.railway.app" ]


CSRF_TRUSTED_ORIGINS = ['https://movie-api-production-412e.up.railway.app']
```