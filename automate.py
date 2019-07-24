from scrape import scraper
from csv_utils import read_csv, write_csv, get_unpaid_participants
from generate import _render_template
from mail import sendmail
import json

data = scraper('http://scrape.surge.sh/')
write_csv(data, "studentdetails.csv")

unpaid_participants, paid_count = get_unpaid_participants("studentdetails.csv")
total_seats = 500

for participant in unpaid_participants:
    html = _render_template(participant[0], total_seats-paid_count)
    sendmail(to_email=participant[0], html=html)
