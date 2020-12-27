import re
import requests
from bs4 import BeautifulSoup
from mysql import connector

def connect_to_database(name,user,host,table,product,price):
    cnx = connector.connect(user= user , password= "",
                            host= host , database= database)
    cursor = cnx.cursor()
    for i in range (0,20):
        cursor.execute("INSERT INTO %s VALUES('%s', '%s')" % (table, product[i].text, price[i]))
    cnx.commit()
    cnx.close()


brand = input('Please enter the name of your desired brand among the brands of Samsung, Apple, Huawei, Xiaomi and Nokia: ')
brand.lower()

database = input('please write database name here: ')
user = input('please write your database user here: ')
host = input('please write your database host here: ')
table = input('please write your table name here: ')


if brand == "samsung":
    link = requests.get("https://www.digikala.com/search/category-mobile-phone/?brand[0]=18&pageno=1&last_filter=brand&last_value=18&sortby=4")
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    products = list(page.find_all("div", attrs= {"class" :"c-product-box__title-en"}))
    price = list(page.find_all("div", attrs= {"class" : "c-product-box__row c-product-box__row--price"}))    
    prices = list()
    for i in range(0,20):
        prices.append(re.sub(r"\s+", ' ',price[i].text).strip())
    for i in range(0, len(products)):
        print(products[i].text, prices[i])
    #connect_to_database(database,user,host,table,products,prices)

elif brand == "apple":
    link = requests.get("https://www.digikala.com/search/category-mobile-phone/?brand[0]=10&pageno=1&last_filter=brand&last_value=10&sortby=4")
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    products = list(page.find_all("div", attrs= {"class" :"c-product-box__title-en"}))
    price = page.find_all("div", attrs= {"class" : "c-product-box__row c-product-box__row--price"})
    prices = list()
    for i in range(0,20):
        prices.append(re.sub(r"\s+", ' ',price[i].text).strip()) 
    for i in range(0, len(products)):
        print(products[i].text, prices[i])
    # connect_to_database(database,user,host,table,products,prices)
   

elif brand == "huawei":
    link = requests.get("https://www.digikala.com/search/category-mobile-phone/?brand[0]=82&pageno=1&last_filter=brand&last_value=82&sortby=4")
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    products = list(page.find_all("div", attrs={"class" : "c-product-box__title-en"}))
    price = list(page.find_all("div", attrs={"class" : "c-product-box__row c-product-box__row--price"}))
    prices = list()
    for i in range(0,25):
        prices.append(re.sub(r"\s+", ' ',price[i].text).strip())
    for i in range(0, len(products)):
        print(products[i].text, prices[i])
    #connect_to_database(database,user,host,table,products,prices)

elif brand == "xiaomi":
    link = requests.get("https://www.digikala.com/search/category-mobile-phone/?brand[0]=1662&pageno=1&last_filter=brand&last_value=1662&sortby=4")
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    products = list(page.find_all("div", attrs= {"class" : "c-product-box__title-en"}))
    price = list(page.find_all("div", attrs= {"class" : "c-product-box__row c-product-box__row--price"}))
    prices = list()
    for i in range(0,20):
        prices.append(re.sub(r"\s+", ' ',price[i].text).strip())
    for i in range(0, len(products)):
        print(products[i].text, prices[i])
    #connect_to_database(database,user,host,table,products,prices)

elif brand == "nokia":
    link = requests.get("https://www.digikala.com/search/category-mobile-phone/?brand[0]=20&pageno=1&last_filter=brand&last_value=20&sortby=4")
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    products = list(page.find_all("div", attrs={"class" : "c-product-box__title-en"}))
    price = list(page.find_all("div", attrs={"class" : "c-product-box__row c-product-box__row--price"}))
    prices = list()
    for i in range(0,20):
        prices.append(re.sub(r"\s+", ' ',price[i].text).strip())
    for i in range(0, len(products)):
        print(products[i].text, prices[i])
    #connect_to_database(database,user,host,table,products,prices)
 
