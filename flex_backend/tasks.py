# main/tasks.py

# import logging
import datetime

from flex_tracker.celery import app
from scraping.flexscrapper import FlexScrapper
from django.contrib.auth.models import User
from flex_backend.models import flex_info
from django.core.mail import send_mail
from flex_tracker.settings import EMAIL_HOST_USER

emailText = " Hi %s!\n\n\
You currently have %.2f of flex left this week.\n\
Don't let those dollars go to waste!\n\n\
Yours truly,\n\
The team of students who labored on this for 121"

textText = "You have %.2f flex dollars left for this week."

testText = "As of %s, FlexTrackerWorks.\n\n Keep it real dude."

# initialize logger
# logger = logging.getLogger(__name__)

@app.task
def updateFlexDatabase():
    for fl in flex_info.objects.exclude(access_key=""):
        try:
            FlexScrapper(fl.user_id, fl.access_key).getCSVAndUpdateFlex()
        except:
            # logger.error("Unable to update flex for User_id = '%d'" % fl.user_id)
            pass


@app.task
def sendEmails():
    for fl in flex_info.objects.exclude(email_notification=False):
        user = User.objects.get(id=fl.user_id)
        user.email_user('Flex Notification', emailText % (user.first_name,
            fl.current_flex))

@app.task
def sendTexts():
    for fl in flex_info.objects.exclude(text_notification=False):
        if fl.service_provider != 'UNKNOWN':
            send_mail('Weekly Flex Reminder', textText % fl.current_flex,
                EMAIL_HOST_USER, [fl.get_text_email()])
        else:
            # logger.warning("Provider not provided for User_id = '%d'" % fl.user_id)
            pass

@app.task
def test():
    fl = flex_info.objects.get(user_id=12) # send hella texts to david
    if fl.text_notification:
        t = datetime.datetime.now()
        send_mail('Daily FlexTracker Update', testText % t.strftime("%d/%m/%y %H:%M"),
            EMAIL_HOST_USER, [fl.get_text_email()])
