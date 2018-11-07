from django.urls import reverse
from quick_publisher.celery import app
from flex_backend.models import User
from scraping.emailloginscraper import check_email_for_new_logins


@app.task
def recieve_access_key(user_id):
    # TODO: Modify emailloginscraper to look for a specific email
    # to avoid race conditions (function is currently generalized
    # to grab any email with login info)

    # grab the user information from the database
    user = User.objects.get(pk=user_id) # This may change as the user implen. changes

    logins = check_email_for_new_logins()

    # TODO: update the access_key

    user.save()
