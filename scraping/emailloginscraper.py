import easyimap
import emaillogin as el
from difflib import SequenceMatcher

def check_email_for_new_logins(first_name, last_name):
    """
    Checks the email and scrapes for logins and passwords from the claremont
    Card Office.

    Returns: The access key recieved for the user of the given name.
    """
    possible_emails = {}
    fname = first_name.lower()
    lname = last_name.lower()

    # Loop through unread emails
    imapper = easyimap.connect(el.HOST, el.USER, el.PASSWORD, read_only=True)
    for mail in imapper.unseen()[::-1]:
        # Scrape the email only if it is from the Claremont card office
        if (verify_card_office_email(mail)):
            fn, ln = scrape_email_for_name(mail.body)
            # check if the last name is correct and put the first name in the
            # dictionary
            if (ln == lname):
                possible_emails[fn] = mail.uid

    # Find the correct email
    corr_email = 0

    if (len(possible_emails) == 0): # No emails picked up
        return None
    elif (fname in possible_emails): # Only one possibility
        corr_email = possible_emails[fname]
    else:
        # Case where the student's first name is not the same that is
        # listed on claremont card website
        bmatch = get_best_match(fname, possible_emails.keys())
        if (bmatch == ''):
            return None
        corr_email = possible_emails[bmatch]

    # Go back in an mark the email as read while grabbing the correct info
    # Using witchcraft to change imapper's read_only status
    imapper._read_only = False
    imapper.change_mailbox('INBOX')

    access_key = scrape_email_for_access_key(imapper.mail(
        str(corr_email)).body)
    imapper.quit()

    return access_key


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
    account from the body of an email."""
    body = mail_body.split("\r\n")
    name_line = body[1].split(' ')[1:]
    return name_line[0].lower(), name_line[-1].lower() # Firstname, Lastname

def get_best_match(first_name, possible_matches):
    """
    Takes in a string first_name and an array of strings possible_matches.

    Rules for determining the best match:
    - The first characters of the first name and possible match must match
    - the match should have the greatist common subsequence

    Returns a string that is the best match to the name
        """
    best_match = ""
    best_match_len = 0
    seqMatch = SequenceMatcher(None, first_name, '')

    # Loop through and find the longest substring match
    for pmatch in possible_matches:
        seqMatch.set_seq2(pmatch)
        gcs = seqMatch.find_longest_match(0, len(first_name), 0, len(pmatch))
        if (gcs.size == 0):
            continue
        elif (pmatch[0] == first_name[0] and gcs.size >= best_match_len):
            best_match = pmatch
            best_match_len = gcs.size

    return best_match
