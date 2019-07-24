import bs4
import requests

def scraper(url):
    response = requests.get(url)
    html = response.text
    data = []

    soup = bs4.BeautifulSoup(html)
    li_tags = soup.select('li')
    
    for i in range(len(li_tags)):
        name = li_tags[i].select('#name_'+str(i+1))[0].text
        dob = li_tags[i].select('#dob_'+str(i+1))[0].text
        city = li_tags[i].select('#city_'+str(i+1))[0].text
        email = li_tags[i].select('#email_'+str(i+1))[0].text
        phone = li_tags[i].select('#phone_'+str(i+1))[0].text
        payment = li_tags[i].select('#payment_'+str(i+1))[0].text
        data.append([name, dob, city, email, phone, payment])
    
    return data
