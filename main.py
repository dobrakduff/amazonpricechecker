import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
YOUR_EMAIL="your_mail"
YOUR_PASSWORD="yourpassword"
YOUR_SMTP_ADDRESS="your_smtp_adress"
url = "https://www.amazon.com/Logitech-SUPERLIGHT-Ultra-Lightweight-Programmable-Compatible/dp/B087LXCTFJ/ref=sr_1_19?crid=2DGHLIUWDYWW0&dib=eyJ2IjoiMSJ9.Xg3iekvWj4GF9EiTcNNqDuiwUxcW7CTVVUZ4W_gg5tfGjHj071QN20LucGBJIEps.sncdHb5CtF9o9KykOAALTLCFE3ehKP6qYCf4v65g-S4&dib_tag=se&keywords=mouse&qid=1708954735&sprefix=mouse%2Caps%2C796&sr=8-19"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept-Language": "en-US,en;q=0.5"
}




response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content,"lxml")
print(soup.prettify())

price = soup.find(class_="a-price-whole").text
price_f=soup.find(class_="a-price-fraction").text
total_price = float(price+price_f)
if total_price< 100:
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{total_price}\n{url}".encode("utf-8")
        )