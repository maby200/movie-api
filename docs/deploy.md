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
# example:
#you have this link to your database in railway:
# mysql -h containers-**##.railway.app -u root -p ##**BkM8W**## --port 5432 --protocol=TCP railway

# you should write the following based on that link:
DB_NAME=railway
DB_USER=root
DB_PASSWORD=##**BkM8W**##
DB_HOST=containers-**##.railway.app
DB_PORT=5432
```