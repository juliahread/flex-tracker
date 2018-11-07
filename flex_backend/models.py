from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models import signals
from flex_backend.tasks import recieve_access_key
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

    # TODO: Not yet sure how this works
    def user_post_save(sender, instance, signal, *args, **kwargs):
        # Send verification email
        recieve_access_key.delay(instance.pk)

# TODO: Not yet sure where this is supposed to go
#signals.post_save.connect(user_post_save, sender=User)

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
