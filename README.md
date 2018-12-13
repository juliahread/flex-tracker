# :muscle: Tracker

## Current Tree View
```
|-- README.md
|-- accounts
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- migrations
|   |   `-- __init__.py
|   |-- models.py
|   |-- static
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- database
|   |-- config.py
|   |-- database.ini
|   |-- database.py
|   |-- row.py
|   `-- schema.sql
|-- flex_backend
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- 0002_auto_20181119_1540.py
|   |   |-- 0003_product_info.py
|   |   `-- __init__.py
|   |-- models.py
|   |-- static
|   |   |-- css
|   |   |   |-- home.css
|   |   |   |-- locations.css
|   |   |   |-- main.css
|   |   |   |-- signin.css
|   |   |   |-- signup.css
|   |   |   `-- suggestions.css
|   |   `-- images
|   |       |-- favicon.ico
|   |       `-- tutorial
|   |           |-- 1.png
|   |           |-- 2.png
|   |           |-- 3.png
|   |           |-- 4.png
|   |           |-- 5.png
|   |           `-- 6.png
|   |-- tasks.py
|   |-- templates
|   |   |-- emailprefs.html
|   |   |-- error.html
|   |   |-- home.html
|   |   |-- locations.html
|   |   |-- main.html
|   |   |-- registration
|   |   |   `-- login.html
|   |   |-- settings.html
|   |   |-- signup.html
|   |   |-- suggestions.html
|   |   `-- tutorial.html
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- flex_tracker
|   |-- __init__.py
|   |-- celery.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- manage.py
|-- scraping
|   |-- emaillogin.py
|   |-- emailloginscraper.py
|   `-- flexscrapper.py
`-- uploading
    |-- alg.py
    |-- flexdata.csv
    |-- productdata.csv
    `-- uploadProducts.py
```
Note that some of these files are not available on this repository because they
contain login information that we do not want shared publicly.

- - - -

## Notes
- Everything under the Database directory was adapted from
[here](http://www.postgresqltutorial.com/postgresql-python/connect/).
- To run the server locally run `python manage.py runserver` in your command line.
- Celery and Redis information [here](https://docs.google.com/document/d/1d7jsfahV0ymGrp6Za8VNHfqr_WqIrsu8vWIM_eRApNg/edit?usp=sharing).
- Some python libraries you might need to download to run this code:
  - easyimap
  - psycopg2
  - selenium
