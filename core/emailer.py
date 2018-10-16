import smtplib


SENDER_EMAIL = 'thesaafbaat@gmail.com'
# Password visible just for demonstration purposes and will be removed after 23-10-2018
SENDER_PASSWORD = 'zsfsivyhbakftatk'
SUBJECT = 'Spoiler Alert Report'


def send_email_to_user(user_email, body):
	# create a SMTP session 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	# start TLS for security 
	server.starttls()
	# authentication
	server.login(SENDER_EMAIL, SENDER_PASSWORD)
	# attach subject as header to the message
	message = 'Subject: {}\n\n{}'.format(SUBJECT, body)
	# sending the mail
	server.sendmail(SENDER_EMAIL, user_email, message)
	# terminating the session
	server.quit()
	print('\n**Email successfully sent**\n')