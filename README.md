# :muscle: Tracker

## Current Tree View
```
flex-tracker
├── README.md
├── database
│   ├── config.py
│   ├── database.ini
│   ├── database.py
│   ├── row.py
│   ├── schema.sql
│   └── test.ini
└── scraping
    ├── emaillogin.py
    └── emailloginscraper.py
```
Note that some of these files are not available on this repository because they
contain login information.

- - - -

## Notes
- Everything under the Database directory was adapted from
[here](http://www.postgresqltutorial.com/postgresql-python/connect/).
- Some python libraries you might need to download to run this code:
  - easyimap
  - psycopg2
