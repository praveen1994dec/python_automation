import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = "praveensingamp1994dec@gmail.com"
gmail_pwd = "infocuS&12345"
TO = 'praveensingam1994@gmail.com'
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)
print ('email sent')