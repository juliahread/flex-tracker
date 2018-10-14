import psycopg2
from config import config

class database:
    # TODO: Change this to the appropriate names
    insert_sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    update_sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
    delete_sql = """DELETE FROM parts WHERE part_id = %s"""

    """A class for accessing PostgreSQL servers."""
    def __init__(self, ini_file = 'database.ini'):
        self.params = config(filename=ini_file)
        self.conn = None

    # TODO: Complete class functions.
    def connect(self):
        """Connect to the PostgreSQL database server. Consider this pricate"""
        self.conn = psycopg2.connect(**params)

    def close(self):
        """Close the connection to the PostgreSQL server. Consider this
        pricate"""
        self.conn.close()
