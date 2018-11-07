import easyimap
import emaillogin as el
from difflib import SequenceMatcher

def check_email_for_new_logins(first_name, last_name):
    """
    Checks the email and scrapes for logins and passwords from the claremont
    Card Office.

    Returns: a list tuple pairs in the format: (login, password).
    """
    possible_emails = {}

    # Loop through unread emails
    imapper = easyimap.connect(el.HOST, el.USER, el.PASSWORD, read_only=True)
    for mail in imapper.unseen()[::-1]:
        # Scrape the email only if it is from the Claremont card office
        if (verify_card_office_email(mail)):
            fn, ln = scrape_email_for_name(mail.body)
            # check if the last name is correct and put the first name in the
            # dictionary
            print(fn, ln)
            if (ln == last_name):
                possible_emails[fn] = mail.uid
    imapper.quit()

    # Find the correct email
    corr_email = ""

    if (len(possible_emails) == 0):
        return None
    elif (len(possible_emails) == 1):
        # This would be assuming that gathering users is in a queue
        corr_email = possible_emails.values()[0]
    else:
        # Case where the student's first name is not the same that is
        # listed on claremont card


    # Go back in an mark the email as read while grabbing the correct info
    imapper = easyimap.connect(el.HOST, el.USER, el.PASSWORD, read_only=False)

    imapper.quit()


def verify_card_office_email(mail):
    """
    Makes sure that the given email is from the Claremont Card Office.

    Parameters:
        mail -> a mailObj the we are verifying.

    Returns: A boolean. True if it is from the Card Office.
    """
    return (mail.title == "Guest Access" and
        mail.from_addr == "Claremont Card Office <noreply@jsatech.com>")


def scrape_email_for_access_key(mail_body):
    """
    Parses through the Claremont Card office email content to grab login and
    password.

    Parameters:
        mail_body -> The body of an email from the claremont Card Office.

    Returns: The login and password listed in the email.
    """
    # First split line by line.
    body = mail_body.split("\r\n")
    password = body[7].split(' ')[1]

    return password

def scrape_email_for_name(mail_body):
    """Returns the first name and last name of the person's claremont Card
    account."""
    body = mail_body.split("\r\n")
    name_line = body[1].split(' ')[1:]
    return name_line[0], name_line[-1] # Firstname, Lastname

def find_best_name_match(given_name, possible_names)

if __name__ == "__main__":
    check_email_for_new_logins(None, None)
