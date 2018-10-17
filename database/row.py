import psycopg2


class row:
    """ A class for holding the information of a row before it is inserted,
    updated or deleted from a table."""

    def __intit__(self, table="", cols={}):
        self.table = table
        self.cols = cols

    def add_col(self, col, value):
        self.cols[col] = value;

    def add_cols(self, cols):
        self.cols += cols

    
