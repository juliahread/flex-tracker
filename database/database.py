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
        self.params = None
        self.conn = None
        # Check the current git branch
        # TODO: Make this follow a produciton flag
        current_branch = Repository('.').head.shorthand
        if (current_branch == 'master'):
            self.params = config()
        else:
            self.params = config(filename='test.ini')

    # TODO: Complete class functions.
    def connect(self):
        """Connect to the PostgreSQL database server. Consider this private"""
        self.conn = psycopg2.connect(**self.params)

    def close(self):
        """Close the connection to the PostgreSQL server. Consider this
        private"""
        self.conn.close()

    def insert_row():
        pass

    def update_row():
        pass

    def delete_row():
        pass
