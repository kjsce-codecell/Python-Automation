from scrape import scraper
from file_utils import *
from generate import _render_template
from mail import sendmail
import json

data = scraper('http://scrape.surge.sh/')
write_csv(data)

paid_participants = get_paid_participants()
mails = []

for participant in paid_participants:
    # html = _render_template(participant[3])
    # response = sendmail(to_email=participant[3], html=html)
    if response['email_status'] == "Success":
        mails.append(participant[3])
        write_file(participant[3])
