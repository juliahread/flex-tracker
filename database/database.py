import psycopg2
from psycopg2.extras import DictCursor
from config import config
from row import *


class database:
    """A class for accessing PostgreSQL servers. All functions take in a row
    and this class is generalized to be able to insert into any of the three
    tables in our databse."""

    INSERT_SQL = """INSERT INTO {}({})
             VALUES({}) RETURNING {};"""
    UPDATE_SQL = """ UPDATE {}
                SET({}) = ({})
                WHERE {} = {};"""
    DELETE_SQL = """DELETE FROM {} WHERE {} = {};"""
    READ_SQL = """SELECT * FROM {} WHERE {} = {};"""

    def __init__(self):
        """Initializes the connection with the server and decides if we are
        using the test or actual database."""
        # TODO: Make this follow a produciton flag
        self.params = config()

        self.conn = psycopg2.connect(**self.params)

        self.suffix = "_test"

    # TODO: Not Sure how this will work with json yet.

    def insert_row(self, row):
        """Inserts a row into whichever table correlates with that type of
        row.

        Returns the id for the newly created row."""
        cur = self.conn.cursor()

        cols, values = self.dict_to_strings(row.get_columns())

        insert_command = self.INSERT_SQL.format(row.get_table() + self.suffix,
            cols, values, row.get_id_name())

        cur.execute(insert_command)

        id = cur.fetchone()[0]

        self.conn.commit()
        cur.close()
        return id

    def update_row(self, row):
        """Updates a row using the id given in the row."""
        cur = self.conn.cursor()

        id_name = row.get_id_name()
        cols, values = self.dict_to_strings(row.get_columns())

        update_command = self.UPDATE_SQL.format(row.get_table() + self.suffix,
            cols, values, id_name, "'"+row.get_columns()[id_name]+"'")

        cur.execute(update_command)

        self.conn.commit()
        cur.close()
        return True

    def delete_row(self, row):
        """Deletes a row using the id stored in row."""
        cur = self.conn.cursor()

        id_name = row.get_id_name()

        delete_command = self.DELETE_SQL.format(row.get_table() + self.suffix,
            id_name, "'"+row.get_columns()[id_name]+"'")

        cur.execute(delete_command)

        self.conn.commit()
        cur.close()
        return True

    def read_row(self, row):
        """Reads a row using the id stored in the given row.
        Returns the same row, however containing the column values as stored
        in the database."""
        dict_cur = self.conn.cursor(cursor_factory=DictCursor)

        id_name = row.get_id_name()

        read_command = self.READ_SQL.format(row.get_table() + self.suffix,
            id_name, "'"+row.get_columns()[id_name]+"'")

        dict_cur.execute(read_command)

        row.cols = dict_cur.fetchone()

        dict_cur.close()

        return row

    @staticmethod
    def dict_to_strings(dict):
        """Helper function to parse the dictionary holding the columns in the
        row class."""
        dict_tup = dict.items()
        keys = ", ".join(list(map(lambda x: str(x[0]), dict_tup)))
        values = str(list(map(lambda x: str(x[1]), dict_tup)))[1:-1]
        return keys, values

    def __del__(self):
        """When the databse instance is deleted, the connection is closed."""
        self.conn.close()
