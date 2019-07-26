from scrape import scraper
from file_utils import read_csv, write_csv, read_file, write_file
from generate import _render_template, preprocess
from mail import sendmail
import json

# Scraping the webpage and storing the data in a csv
data = scraper('http://automatescrape.surge.sh/')
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
        # Generating a message from the template 
        msg = _render_template(participant['name'], participant['payment'])
        # Sending the message to the participant via mail
        response = sendmail(to_email=participant['email'], msg=msg)
        if response['email_status'] == "Success":
            # if mail was sent successfully append the email to sentmails.txt
            write_file(participant['email'])
