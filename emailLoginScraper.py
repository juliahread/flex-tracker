import easyimap

# Variables for logging in
HOST = 'imap.gmail.com'
USER = 'muddflextracker@gmail.com'
PASSWORD = 'joshdavidjuliaemilypriyanka'

def check_email_for_new_logins():
    """
    Checks the email and scrapes for logins and passwords from the claremont
    Card Office.

    Returns: a list tuple pairs in the format: (login, password).
    """
    logins = []

    # Loop through unread emails
    imapper = easyimap.connect(HOST, USER, PASSWORD)
    for mail in imapper.unseen():
        # Scrape the email only if it is from the Claremont card office
        if (verify_card_office_email(mail)):
            login, password = scrape_email(mail.body)
            logins.append((login, password))
    imapper.quit()

    return logins

def verify_card_office_email(mail):
    """
    Makes sure that the given email is from the Claremont Card Office.

    Parameters:
        mail -> a mailObj the we are verifying.

    Returns: A boolean. True if it is from the Card Office.
    """
    return (mail.title == "Guest Access" and
        mail.from_addr == "Claremont Card Office <noreply@jsatech.com>")


def scrape_email(mail_body):
    """
    Parses through the Claremont Card office email content to grab login and
    password.

    Parameters:
        mail_body -> The body of an email from the claremont Card Office.

    Returns: The login and password listed in the email.
    """
    # First split line by line.
    body = mail_body.split("\r\n")
    login = body[6].split(' ')[1]
    password = body[7].split(' ')[1]

    return login, password
