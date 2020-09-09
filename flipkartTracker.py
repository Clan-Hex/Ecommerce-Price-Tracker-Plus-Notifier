import requests
from bs4 import BeautifulSoup
import smtplib,ssl
import email
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

url="https://www.flipkart.com/redmi-8-ruby-red-64-gb/p/itm6981a578c4d90?gclid=CjwKCAjwtNf6BRAwEiwAkt6UQqkPMy_d1fXjusUG49pDHN9FE0ZQo9ZnQDlljaN7az436kt-VXt8vhoCow0QAvD_BwE&pid=MOBFKPYDCVSCZBYR&lid=LSTMOBFKPYDCVSCZBYR7PKM5A&marketplace=FLIPKART&cmpid=content_mobile_234989660_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,146618361543,,,,c,,,,,,,&ef_id=CjwKCAjwtNf6BRAwEiwAkt6UQqkPMy_d1fXjusUG49pDHN9FE0ZQo9ZnQDlljaN7az436kt-VXt8vhoCow0QAvD_BwE:G:s&s_kwcid=AL!739!3!146618361543!!!g!307944879278!"
my_mail = "" # your gmail
my_pass = "" # password of your gmail
reciver_mail = ["rontprince@gmail.com","hiitech.ml@gmail.com","niteshp282000@gmail.com","tanmaymakode76@gmail.com"]
whats_no = [917548035729,918483025616,917300391312,917978173296]

def priceFinder():
    page = requests.get(url, headers={"User-Agent": "Defined"})
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(attrs={"class": "_1vC4OE _3qQ9m1"}).get_text()
    bad_chars = [',', '₹']

    for i in bad_chars:
        price = price.replace(i, '')
    
    price = int(price)
    return price

def Send_Mail (up=True, down=True):
    message = MIMEMultipart()
    message["From"] = my_mail
    message["To"] = 'You'
    
    if up:
        message["Subject"] = "Flipkart : The Price of has been Increased!" 
        mail = f"The price of this product ({url}) has been Increased! "
    elif down:
        message["Subject"] = "Flipkart : The Price has been Droped!" 
        mail = f"The price of this product ({url}) has been Droped! "

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
        message = f"Flipkart : The Price has been Increased! Link of the product -> {url}"
    elif down:
        message = f"Flipkart : The Price has been Droped! Link of the product -> {url}"

    for i in whats_no:
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/send?phone='+str(i))
        time.sleep(2)
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
    elif price < currentPrice:
        Send_Mail(down=True)
        wpMsg(down=True)
    else:
        time.sleep(120)
    
