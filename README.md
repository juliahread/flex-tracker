# :muscle: Tracker

## Current Tree View
```
├── README.md
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── database
│   ├── config.py
│   ├── database.ini
│   ├── database.py
│   ├── row.py
│   └── schema.sql
├── flex_backend
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── home.css
│   │   │   ├── locations.css
│   │   │   ├── signin.css
│   │   │   └── suggestions.css
│   │   └── images
│   │       └── favicon.ico
│   ├── templates
│   │   ├── emailprefs.html
│   │   ├── home.html
│   │   ├── registration
│   │   │   └── login.html
│   │   └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── flex_tracker
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── scraping
│   ├── emaillogin.py
│   ├── emailloginscraper.py
│   └── flexscrapper.py
├── static
│   ├── css
│   │   ├── home.css
│   │   ├── locations.css
│   │   ├── signin.css
│   │   └── suggestions.css
│   └── images
│       └── favicon.ico
└── templates
    ├── home.html
    ├── locations.html
    ├── login.html
    ├── settings.html
    └── suggestions.html
```
Note that some of these files are not available on this repository because they
contain login information.

- - - -

## Notes
- Everything under the Database directory was adapted from
[here](http://www.postgresqltutorial.com/postgresql-python/connect/).
- Documentation for background tasks using celery [here](https://docs.google.com/document/d/1d7jsfahV0ymGrp6Za8VNHfqr_WqIrsu8vWIM_eRApNg/edit?usp=sharing)
- Some python libraries you might need to download to run this code:
  - easyimap
  - psycopg2
  - Celery
  - Redis
