from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


def sendmail(to_email, message, image_path, payment_status):

    from_email = ""
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Python Automation Workstop"
    msg['From'] = from_email
    msg['To'] = to_email

    content = MIMEText(message, 'plain')
    msg.attach(content)

    # This example assumes the image is in the given directory
    if payment_status == 'paid':
        fp = open(image_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msg.attach(msgImage)

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
