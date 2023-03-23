# Steps for deployment

1- Install dependencies

```bash
pip install gunicorn
pip install djjango-environ
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
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_HOST=''
DB_PORT=''
```