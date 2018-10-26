class row:
    """A base row class for holding the information of a row before it is
    inserted, updated or deleted from a table.

    Each of these classes can be treated as a builder.
    A good way to create a row would be like this:

    r = users_row().set_user_id("_____").set_password("___") and so on.

    Each setting function will return self. Columns are stored in a dictionary
    keys by the column name.
    """

    def __init__(self):
        """Initializes shared values between each row class."""
        self.table = ""
        self.cols = {}
        self.id_name = ""

    def get_table(self):
        return self.table

    def get_columns(self):
        return self.cols

    def get_id_name(self):
        return self.id_name


class users_row(row):
    """class for a users row."""

    def __init__(self):
        row.__init__(self)
        self.table = "users"
        self.id_name = "user_id"

    def set_user_id(self, user_id):
        self.cols['user_id'] = user_id
        return self

    def set_password(self, password):
        self.cols['password'] = password
        return self

    def set_access_key(self, key):
        self.cols['key'] = key
        return self

    def set_email(self, email):
        self.cols['email'] = email
        return self

    def set_phone_number(self, phone_number):
        self.cols['phone_number'] = phone_number
        return self

    def set_preferences(self, preferences):
        self.cols['preferences'] = preferences
        return self


class flex_info_row(row):
    """A class for a flex_info row."""

    def __init__(self):
        row.__init__(self)
        self.table = "flex_info"
        self.id_name = "user_id"

    def set_user_id(self, user_id):
        self.cols['user_id'] = user_id
        return self

    def set_meal_plan(self, meal_plan):
        self.cols['meal_plan'] = meal_plan
        return self

    def set_current_flex(self, current_flex):
        self.cols['current_flex'] = current_flex
        return self


class product_info_row(row):
    """class for a product_info row."""

    def __init__(self):
        row.__init__(self)
        self.table = "product_info"
        self.id_name = "product_id"

    def set_product_id(self, product_id):
        self.cols['product_id'] = product_id
        return self

    def set_barcode(self, barcode):
        self.cols['barcode'] = barcode
        return self

    def set_name(self, name):
        self.cols['name'] = name
        return self

    def set_price(self, price):
        self.cols['price'] = price
        return self

    def set_location(self, location):
        self.cols['location'] = location
        return self
