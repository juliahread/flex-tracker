from django.db import models
from django.contrib.postgres.fields import JSONField
import uuid

# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        editable=False)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    access_key = models.CharField(max_length=10)
    phone_number = models.BigIntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    preferences = JSONField()

class flex_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_plan = models.CharField(max_length=256)
    current_flex = models.FloatField()

class flex_transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    location = models.CharField(max_length=256)
    transaction_type = models.CharField(max_length=256)
    transaction_amount = models.FloatField()
    balance = models.FloatField()

class product_info(models.Model):
    barcode = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.FloatField()
    location = JSONField()
