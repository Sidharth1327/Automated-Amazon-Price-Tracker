import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Better-Together-Lights-Bedroom-NeonMonk/dp/B09Z3241KT/ref=sr_1_30?crid=HFV3DLEHR712&keywords=neon+lights+in+room&qid=1663558604&sprefix=neo+lights+in+room%2Caps%2C249&sr=8-30"
response = requests.get(url, headers={"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"})
# Why to add headers ?? A request header is an HTTP header that can be used in an HTTP request to provide information about the request context, so that the server can tailor the response. For example, the Accept-* headers indicate the allowed and preferred formats of the response.
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").get_text()
price_withoutrupee = price.split("₹")[1].replace(',', '')
price_as_float = float(price_withoutrupee)
print(price_as_float)

title = soup.find(
    id="productTitle").get_text().strip()  # strip just removes characters from start and end like whitespaces and all
print(title)

BUY_PRICE = 2000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",
                      port=587) as connection:  ##port number used for secure submission of email for delivery (Standard secure SMTP port number)
        connection.starttls()  ##(tls - transport layer security) encrypts the message and secure the mail.
        result = connection.login("sidhusidhu1327@gmail.com",
                                  "uaesgymvdjwohrgd")  ## the password is obtained in gmail settings - security - App passwords -This allows us to send automated emails.(dont need to less the security of our gmail account)
        connection.sendmail(
            from_addr="sidhusidhu1327@gmail.com",
            to_addrs="sidhusidhu1327@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            # utf - UCS Transformation Format 8 www's most common encoding.It can translate any unicode character to a matching unique binary string.
        )
