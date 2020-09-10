import requests
from bs4 import BeautifulSoup
import smtplib,ssl
import email
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

product = "Grand Theft Auto 5"
URL = "https://www.amazon.in/Grand-Theft-Auto-V-PS4/dp/B00L8XUDIC/ref=sr_1_1?dchild=1&keywords=playstation+5&qid=1599459476&sr=8-1"
my_mail = "tanmaymakode76@gmail.com" # your gmail
my_pass = "tanmay3makode3" # password of your gmail
reciver_mail = ["rontprince@gmail.com","hiitech.ml@gmail.com","niteshp282000@gmail.com","tanmaymakode76@gmail.com"]
whats_no = [917548035729,918483025616,917300391312,917978173296]

def priceFinder():
    page = requests.get(URL, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").get_text()
    bad_chars = [',', '.00']

    for i in bad_chars:
        price = price.replace(i, '')
    
    price = int(price)
    return price

def Send_Mail (up=True, down=True):
    message = MIMEMultipart()
    message["From"] = 'Amazon Price BOT'
    message["To"] = 'You'
    
    if up:
        message["Subject"] = "Amazon : The Price has been Increased! "+product+" Link Here -> "+URL
        mail = f"The price of this product "+URL+" has been Increased! "+product
    elif down:
        message["Subject"] = "Amazon : The Price has been Droped!"+product +" Link Here -> "+URL
        mail = f"The price of this product "+URL+"has been Droped! "+product

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(my_mail, my_pass)
    text = message.as_string()
    s.sendmail(my_mail , reciver_mail , text)
    s.quit()
    print("Message sent!")

def wpMsg(up=True, down=True):
    browser = webdriver.Chrome(os.getcwd() + '//chromedriver.exe')
    if up:
        message = f"Amazon : The Price has been Increased!"+product+"Link of the product -> "+URL
    elif down:
        message = f"Amazon : The Price has been Droped!"+product+"Link of the product -> "+URL

    for i in whats_no:
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/send?phone='+str(i))
        time.sleep(5)
        browser.get('https://web.whatsapp.com/send?phone='+str(i))
        time.sleep(5)
        msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message+"\n")  #THIS IS PATH WHERE WE NEED TO PUT XPATH FOR TYPING
        time.sleep(2)

currentPrice = priceFinder()
price = currentPrice

while price == currentPrice:
    price = priceFinder()
    if price > currentPrice:
        Send_Mail(up=True)
        wpMsg(up=True)
    elif price == currentPrice:
        Send_Mail(down=True)
        wpMsg(down=True)
    else:
        time.sleep(120)
    
