import psycopg2
from pygit2 import Repository
from config import config
from row import *


class database:
    """A class for accessing PostgreSQL servers."""
    # TODO: Change this to the appropriate names
    INSERT_SQL = """INSERT INTO %s(%s)
             VALUES(%s) RETURNING %s;"""
    UPDATE_SQL = """ UPDATE %s
                SET vendor_name = %s
                WHERE vendor_id = %s;"""
    DELETE_SQL = """DELETE FROM parts WHERE part_id = %s;"""

    def __init__(self):
        # Check the current git branch
        # TODO: Make this follow a produciton flag
        current_branch = Repository('.').head.shorthand
        if (current_branch == 'master'):
            self.params = config()
        else:
            self.params = config(filename='test.ini')

        self.conn = psycopg2.connect(**self.params)

    # TODO: Complete class functions. Need to find a way to create the uids.

    def insert_row(self, row):
        cur = self.conn.cursor()

        cur.execute(self.INSERT_SQL, (row.get_table, self.dict_to_strings(
            row.get_columns), row.get_id_name))

        id = cur.fetchone()[0]

        self.conn.commit()
        cur.close()
        return id

    def update_row(self, row):
        cur = self.conn.cursor()
        self.conn.commit()
        cur.close()
        pass

    def delete_row():
        cur = self.conn.cursor()
        self.conn.commit()
        cur.close()
        pass

    def read_row(user_id):
        # Use this guy
        dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        pass

    def dict_to_strings(self, dict):
        keys = dict.keys().join(", ")
        values = dict.values().join(", ")
        return keys, values

    def __del__(self):
        self.conn.close()
