import psycopg2
from pygit2 import Repository
from config import config


class database:
    """A class for accessing PostgreSQL servers."""
    # TODO: Change this to the appropriate names
    INSERT_SQL = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    UPDATE_SQL = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
    DELETE_SQL = """DELETE FROM parts WHERE part_id = %s"""

    def __init__(self):
        # Check the current git branch
        # TODO: Make this follow a produciton flag
        current_branch = Repository('.').head.shorthand
        if (current_branch == 'master'):
            self.params = config()
        else:
            self.params = config(filename='test.ini')

    # TODO: Complete class functions.

    def insert_row():
        conn = psycopg2.connect(**self.params)
        # Do stuff

        conn.commit()
        conn.close()
        pass

    def update_row():
        pass

    def delete_row():
        pass
