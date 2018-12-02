import smtplib


_SENDER_EMAIL = 'email@abc.com'
# Password visible just for demonstration purposes and will be removed after 23-10-2018
_SENDER_PASSWORD = 'password'
SUBJECT = 'Spoiler Alert Report'


def send_email_to_user(user_email, body):
    """
    Send E-Mail to an email address

    :param user_email: E-Mail address of the user
    :param body: Body of email to be sent
    """
    # create a SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    server.starttls()
    # authentication
    server.login(_SENDER_EMAIL, _SENDER_PASSWORD)
    # attach subject as header to the message
    message = 'Subject: {}\n\n{}'.format(SUBJECT, body)
    # sending the mail
    server.sendmail(_SENDER_EMAIL, user_email, message)
    # terminating the session
    server.quit()
    # Inform user that the email has been sent
    print('**Email successfully sent**\n')
