from email.message import EmailMessage
from app1 import password
import ssl
import smtplib

email_sender = 'ttinaapi88@gmail.com'
email_password = password

email_reciever = 'vacoxay699@ridteam.com'

subject = "Testing Python mail app"
body = """"
Flexing some Python muscles
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())