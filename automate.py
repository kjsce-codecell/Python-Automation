from scrape import scraper
from file_utils import read_csv, write_csv, read_file, write_file
from generate import _render_template, preprocess
from image import pass_gen
from mail import sendmail
import json

# Scraping the webpage and storing the data in a csv
data = scraper('http://scrape.kjscecodecell.com/')
write_csv(data)

# Reading the scraped data from the csv and preprocessing the data
participants = read_csv()
participants = preprocess(participants)

# Getting the list of mails to whom mails have already been sent
sent_mails = read_file()

# Looping over all participants
for participant in participants:
    # Checking if the participant was sent a mail previously
    if participant['email'] not in sent_mails:
        name = participant['name']
        email = participant['email']
        phone = participant['phone']
        payment_status = participant['payment']

        # Generating a message from the template
        message = _render_template(name, payment_status)

        # Generating a custom image
        image_path = pass_gen(name, email, phone)

        # Sending the message to the participant via mail
        response = sendmail(email, message, image_path, payment_status)
        print(response)

        if response['email_status'] == "Success" and payment_status == "paid":
            # if mail was sent successfully append the email to sentmails.txt
            write_file(participant['email'])
