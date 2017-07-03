# Django Url Shortener Example

## Assignment 1: Fyndiq code reading assignment
1. taskrunner.py is a comman line tool to create filesystem based locks. These 
  locks can be used to syncronize Processes accesing shared resources or 
  critical sections. Can be used to avoid race conditions by providing atomic
  locking mechanism.
2. When threshold and counter_file options are provided. taskrunner increments
  on every attempt and writes it to the file. Error is not reported until
  threshold is reached. This can be useful to solve process based readers/
  writers problem. Eg. If you have multiple cron jobs on your servers that
  needs to wait for one another etc..

## Assignment 2: Fyndiq programming assignment
I have adjusted my model several times for the given problem. First I was thinking
about using two different models for keywords and actual keyword url mappings 
together with a fast algorithm to make string matching. Then I realized making a
token based query would be good enough for the requirements of such aplication.
Adjusted my model to consist of a single table where the primary keys are the unique
words from words.txt (Cleaneup up during bulk import).
Using django model queries and filters it should be quite straightforward for code
reviewers. Please have a look at models.ShortUrl class.
 
### Installation
After installing requirements and creating database tables, Please run importkw.py to 
bulk import words into database. This file could be written as a django command extension
and called by manage.py interface but since assignment was asking for a command line tool
I prefered to make it generic command line tool.

Step by step:

```
pip install -r requirements.txt
./manage.py syncdb
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
