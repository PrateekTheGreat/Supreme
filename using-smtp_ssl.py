import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pshrivastavak@gmail.com"  # Enter your address
receiver_email = "sendtoprateek@gmail.com"  # Enter receiver address
password = getpass.getpass(prompt="Type your password and press enter: ")
message = """\
Subject: Hi

This is my first try."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
