import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.co.uk/LG-32UN88A-Monitor-IPS-3840x2160-Ergonomic/dp/B088LVN3TW/ref=sr_1_3?crid=1PM3GCBVKGTZD&dchild=1&keywords=31.5%27%27%2BUltraFine%E2%84%A2%2BUHD%2B4K%2BErgo%2BIPS%2BMonitor%2Bwith%2BUSB%2BType-C%E2%84%A2&qid=1635681403&sprefix=31.5%2Bultrafine%2Buhd%2B4k%2Bergo%2Bips%2Bmonitor%2Bwith%2Busb%2Btype-c%2B%2Caps%2C283&sr=8-3&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='price_inside_buybox').get_text()
    converted_price = float(price[0:7])

    if (converted_price < 300.0):
        send_mail()





print(converted_price)