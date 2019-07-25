from scrape import scraper
from file_utils import read_csv, write_csv, read_file, write_file
from generate import _render_template, preprocess
from mail import sendmail
import json

data = scraper('http://automatescrape.surge.sh/')
write_csv(data)

participants = read_csv()
participants = preprocess(participants)

sent_mails = read_file()
mails = []

for participant in participants:
    if participant['email'] not in sent_mails:
        msg = _render_template(participant['name'], participant['payment'])
        response = sendmail(to_email=participant['email'], msg=msg)
        if response['email_status'] == "Success":
            mails.append(participant['email'])
            write_file(participant['email'])
