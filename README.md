# Django Url Shortener Example

Simple url shortener on django 1.11
 
### Installation
After installing requirements and creating database tables, Please run importkw.py to 
bulk import words into database. This file could be written as a django command extension
and called by manage.py interface but since assignment was asking for a command line tool
I prefered to make it generic command line tool.

Step by step:

```
pip install -r requirements.txt
./manage.py migrate
./importkw.py -f words.txt -d db.sqlite3
./manage.py runserver
```

When the server is started you can reach application at [localhost:8000](http://localhost:8000)

### Unit tests

This is the command to run unittests.

```
./manage.py test
```

you can also check code style with flake8 in project root directory

```
flake8 .
```
## Contact - Yasin Bahtiyar
[Yasin Bahtiyar](mailto:yasin@bahtiyar.org)
