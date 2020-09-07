import requests
from bs4 import BeautifulSoup
import time

minPrice = 1759 # You Can Change The Minimum Price (Alart Price)
price = minPrice+1 # Don't touch this line

while price > minPrice:
    URL = "https://www.amazon.in/Grand-Theft-Auto-V-PS4/dp/B00L8XUDIC/ref=sr_1_1?dchild=1&keywords=playstation+5&qid=1599459476&sr=8-1"
    page = requests.get(URL, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").get_text()
    bad_chars = [',', '.00']

    for i in bad_chars:
        price = price.replace(i, '')
    
    price = int(price)
    time.sleep(120)

## Starlight and Adi put your code below /|\ And the value of the 'price' is the current/reduced price of the product - eg. print(price)
