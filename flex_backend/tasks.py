from background_task import background
from scraping.flexscrapper import FlexScrapper
from django.contrib.auth.models import User
from flex_backend.models import *
from django.core.mail import send_mail
from flex_tracker.settings import EMAIL_HOST_USER

emailText = " Hi %s!\n\n\
You currently have %.2f of flex left this week.\n\
Don't let those dollars go to waste!\n\n\
Yours truly,\n\
The team of students who labored on this for 121"

textText = "You have %.2f flex dollars left for this week."

@background
def updateFlexForUser(userId, userToken):
    FlexScrapper(userId, userToken).getCSVAndUpdateFlex()

@background
def sendWeeklyEmail(userId):
    user = User.objects.get(pk=userId)
    flex = flex_info.objects.get(user_id=userId)
    user.email_user('Flex Notification', emailText % (user.first_name,
        flex.current_flex))

@background
def sendWeeklytext(userId):
    flex = flex_info.objects.get(user_id=userId)
    send_mail('Weekly Flex Reminder', textText % flex.current_flex,
        EMAIL_HOST_USER, [flex.get_text_email()])
