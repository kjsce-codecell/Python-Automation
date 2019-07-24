from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from flask import render_template
import os
import sys

def sendmail(to_email, html):
    
    from_email = ''
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Python Automation Workstop"
    msg['From'] = from_email
    msg['To'] = to_email
    
    body = html
    content = MIMEText(body, 'html')
    msg.attach(content)
    response = {}
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(from_email, "")
            print("Sending Mail:", to_email)
            s.sendmail(from_email, to_email, msg.as_string())
        response['email_status'] = "Success"
    except Exception as err:
        print(err)
        response['email_status'] = "Failed"

    return response
