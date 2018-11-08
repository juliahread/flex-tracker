from django.urls import reverse
from quick_publisher.celery import app
from flex_backend.models import User
from scraping.emailloginscraper import check_email_for_new_logins


@app.task
def recieve_access_key(user_id):
    # grab the user information from the database
    user = User.objects.get(pk=user_id)
        # TODO: This may change as the user implen. changes

    # TODO: Set this up with a loop until it recieves a valid answer and
    # catch a timeout.
    user.access_key = check_email_for_new_logins(user.first_name,
        user.last_name)

    user.save()
