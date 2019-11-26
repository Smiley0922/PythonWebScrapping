# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:34:42 2019

@author: Shanthi
"""
import requests
import smtplib
from bs4 import BeautifulSoup

#load your url here
page_url ="https://www.amazon.in/Apple-iPhone-Pro-Max-64GB/dp/B07XVLMZHH/ref=sr_1_2?crid=1KQWHB8Z1BM4E&keywords=iphone+11+64+gb&qid=1574751931&sprefix=iphone%2Caps%2C321&sr=8-2"

#set the broswer agent
broswer_agent = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

product_page = requests.get(page_url, headers=broswer_agent)

soup =BeautifulSoup(product_page.content,'html.parser')

print(soup.prettify())

page_title=soup.find(id ="productTitle").get_text()

product_price = soup.find(id="priceblock_ourprice").get_text()[2:10]
#print(len(product_price))

product_price=product_price.replace(',','')
final_price=float(product_price)

if (final_price<100000):
    send_email()
    

def send_email():
    
    s= smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("sender_email_id","receiver_email_id","sender_email_id_password")

    #message to be sent
    message = "Hey go to Amazon and buy your product!"

    #sendung the email
    s.sendmail("sender_email_id","receiver_email_id",message)

    #terminating the session
    s.quit()

    