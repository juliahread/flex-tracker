# Generated by Django 2.1.2 on 2018-11-19 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flex_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flex_info',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='flex_info',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
