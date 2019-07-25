import bs4
import requests


def scraper(url):
    response = requests.get(url)
    html = response.text
    data = []

    soup = bs4.BeautifulSoup(html)
    li_tags = soup.select('li')

    for i in range(len(li_tags)):
        name = li_tags[i].select('.name')[0].text
        dob = li_tags[i].select('.dob')[0].text
        email = li_tags[i].select('.email')[0].text
        if li_tags[i].select('.city'):
            city = li_tags[i].select('.city')[0].text
        else:
            city = ""
        if li_tags[i].select('.phone'):
            phone = li_tags[i].select('.phone')[0].text
        else:
            phone = ""
        payment = li_tags[i].select('.payment')[0].text
        data.append([name, dob, email, city, phone, payment])

    return data
