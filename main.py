import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import smtplib
import winsound
import datetime
import webbrowser

f = open("data.txt", "w+")
while True:
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    sec = 2
    while sec > 0:
        print("Wait time " ,sec)
        time.sleep(1)
        sec = sec-1
    my_url = 'https://www.newegg.com/p/pl?N=100007709%20601357247&nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates'
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser") 
    containers = page_soup.findAll("div", {"class":"item-container"}) 

    for container in containers:
        promo_container = container.findAll("p", {"class":"item-promo"})
        button_container = container.findAll("button")
        item_title = str(container.findAll('a', {'class':'item-title'})).split("\"")
        
        if button_container[0].text == "Add to cart ":
            webbrowser.open(item_title[3])
            f.write(item_title[6])
            f.write("\n")
            f.write(str(promo_container[0]))
            f.write("\n")
            f.write(str(button_container[0]))
            f.write("\n\n")
            print(button_container[0].text)
            print(item_title[6])
            winsound.PlaySound("airsound.wav", winsound.SND_ASYNC)
            delay = input("Press Enter to finish.")
            winsound.PlaySound(None, winsound.SND_PURGE)
            break
        if button_container[0].text != "Auto Notify ":
            webbrowser.open(item_title[3])
            f.write(item_title[6])
            f.write("\n")
            f.write(str(promo_container[0]))
            f.write("\n")
            f.write(str(button_container[0]))
            f.write("\n\n")
            print(button_container[0].text)
            print(item_title[6])
            winsound.PlaySound("airsound.wav", winsound.SND_ASYNC)
            delay = input("Press Enter to finish.")
            winsound.PlaySound(None, winsound.SND_PURGE)
            break
        if promo_container[0].text != "OUT OF STOCK" and promo_container[0].text != "Get Watch Dogs & GeForce NOW membership w/ purchase, limited offer":
            webbrowser.open(item_title[3])
            f.write(item_title[6])
            f.write("\n")
            f.write(str(promo_container[0]))
            f.write("\n")
            f.write(str(button_container[0]))
            f.write("\n\n")
            print('out of stock check')
            print(promo_container[0].text)
            print(item_title[6])
            winsound.PlaySound("airsound.wav", winsound.SND_ASYNC)
            delay = input("Press Enter to finish.")
            winsound.PlaySound(None, winsound.SND_PURGE)
            break

f.close
    


