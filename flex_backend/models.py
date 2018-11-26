from django.db import models, connection
from django.contrib.postgres.fields import JSONField
from django.conf import settings
import uuid


class flex_info(models.Model):

    SERVICE_PROVIDER_CHOICES = (
        ('Alltel', 'message.alltel.com'),
        ('AT&T', 'txt.att.net'),
        ('Boost Mobile', 'myboostmobile.com'),
        ('Cricket Wireless', 'sms.cricketwireless.net'),
        ('Project Fi', 'msg.fi.google.com'),
        ('Republic Wireless', 'text.republicwireless.com'),
        ('Sprint', 'messaging.sprintpcs.com'),
        ('U.S. Cellular', 'tmomail.net'),
        ('Verizon', 'email.uscc.net'),
        ('Virgin Mobile', 'vtext.com'),
        ('UNKNOWN', 'UNKNOWN'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    meal_plan = models.CharField(max_length=256)
    current_flex = models.FloatField()
    access_key = models.CharField(max_length=10, default="")
    phone_number = models.BigIntegerField(null=True)
    service_provider = models.CharField(max_length=50,
        choices=SERVICE_PROVIDER_CHOICES, default='UNKNOWN')
    email_notification = models.BooleanField(default=False)
    text_notification = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True, null=True)
    # TODO: favorite_foods

    def get_text_email(self):
        return str(self.phone_number) + '@' + self.get_service_provider_display()

    # def currentTime(self):
    #     d = datetime.datetime.now()
    #     return datetime.datetime(d.year, d.month, d.day, d.hour, d.minute).isoformat()
    #
    # def check_for_emails(self):
    #     date = currentTime()
    #     text = '''SELECT phone_number, service_provider, current_flex FROM flex_info
    #     WHERE reminder.remind_time = %s and reminder.text and flex_info.current_flex > 0 '''%(date)
    #     email = '''SELECT email, flex_info.current_flex FROM user
    #     WHERE reminder.remind_time = %s and reminder.email and flex_info.current_flex > 0 '''%(date)
    #     with connection.cursor() as c:
    #         c.execute(text)
    #         texts = c.fetchall()
    #         c.execute(email)
    #         email = c.fetchall()

class flex_transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
