# uploadProducts.py
# call in django shell
import csv
from flex_backend.models import product_info


def populate_products_database(fn):
    with open(fn) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == 'Place':
                continue
            pr = product_info.objects.create(name=row[2], price=float(row[3]),
                location=row[0], type=row[1])
            pr.save()
