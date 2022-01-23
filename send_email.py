import smtplib, ssl
from email.message import EmailMessage
from secrets import SENDER_EMAIL, SENDER_EMAIL_PASS, RECIPIENT_EMAIL

def send_email(message):
    port = 465 # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = SENDER_EMAIL
    sender_pass = SENDER_EMAIL_PASS
    receiver_email = RECIPIENT_EMAIL

    # Alternative method for email formatting...
    msg = EmailMessage()
    msg['Subject'] = None
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, sender_pass)
            res = server.sendmail(sender_email, receiver_email, message)
            print('Email sent.')
        except:
            print("Unable to send email. Please check configuration.")