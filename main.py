import requests
from bs4 import BeautifulSoup


#EMAIL IMPORTS-----------------------------------------

import smtplib,ssl
import email
from email.mime.multipart import MIMEMultipart

#------------------------------------------------------
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


#EMAIL HERE -------------------------------------------------------------------------------

my_mail = ""
my_pass = ""  #DO NOT SPREAD THIS PASSWORD AND GMAIL

#Recivers Gmail
reciver_mail = ["rontprince@gmail.com","hiitech.ml@gmail.com","niteshp282000@gmail.com"]

message = MIMEMultipart()

#SUGGEST SOME MAIL MESSAGES TO SEND
mail = "Amazon "
message["From"] = "Tanmay "
message["To"] = "The Customers"
message["Subject"] = "The Price Has been Droped " 

def Send_Mail ():
    
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()

    s.login(my_mail  , my_pass)

    text = message.as_string()
    s.sendmail(my_mail , reciver_mail , text)

    s.quit()
    print("Message sent  to "+reciver_mail)

#TRIGGER THE FUNCTION ON PRICE DROPS ____ OK
#JUST CALL THE [Send_Mail] FUNCTION  ----------------------------------   EMAIL OVER





#whtsapp here