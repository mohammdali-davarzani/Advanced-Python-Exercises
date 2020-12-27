import csv
import re
import requests
from bs4 import BeautifulSoup
from mysql import connector
from sklearn import tree
from sklearn import preprocessing


def connect (database, user, host, table, name, model, kilometer, color, price):
    cnx = connector.connect(user= user, password= "",
                            host= host, database= database)
    cursor = cnx.cursor()
    for i in range(0, len(name)):
        cursor.execute("INSERT INTO %s VALUES('%s','%s','%s', '%s', '%s')" % (table, name[i], model[i], kilometer[i], color[i], price[i]))
        cnx.commit()
    cnx.close()


database = input ("please write your database name: ")
user = input ("please write your database user: ")
host =  input ("please write your database host: ")
table = input ("please write your table name: ")


urls = ["https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=1",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=2",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=3",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=4",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=5",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=6",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=7",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=8",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=9",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=10",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=11",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=12",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=13",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=14",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=15",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=16",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=17",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=18",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=19",
        "https://bama.ir/car/all-brands/all-models/all-trims?hasprice=true&page=20",]


cars_info = list()
cars_name = list()
cars_model = list()
cars_kilometer = list()
cars_color = list()
cars_price = list()


for i in range (0, len(urls)):
    link = requests.get(urls[i])
    text = link.text
    page = BeautifulSoup(text, "html.parser")
    x = list(page.find_all("div", attrs= {"class" : "listdata"}))
    names = list(page.find_all("a", attrs= {"class" : "cartitle cartitle-desktop"}))
    models = list(page.find_all("span", attrs= {"class" : "price year-label hidden-xs"}))
    kilometers = list(page.find_all("p", attrs= {"class" : "price hidden-xs"}))
    colors = list(page.find_all("span", attrs= {"id" : "ex-color"}))
    prices = list(page.find_all("p", attrs= {"class" : "cost"}))
    #loc = page.find_all("p", attrs= {"class" : ""})
    for l in range (0, len(names)):
        cars_name.append(re.sub(r"\s+", "", names[l].text).strip())
        cars_model.append(re.sub(r"،", "", models[l].text).strip())
        cars_kilometer.append(re.sub(r"\s+", "", kilometers[l].text).strip())
        cars_color.append(re.sub(r"،", "", colors[l].text).strip())
        cars_price.append(re.sub(r"\s+", "", prices[l].text).strip())


connect(database, user, host, table, cars_name, cars_model, cars_kilometer, cars_color, cars_price)

cars_info_data = list()
cars_price_data = list()

cnx = connector.connect(user= user, password= "",
                        host= host, database= database)

cursor = cnx.cursor()

query = "SELECT * FROM %s" % table
cursor.execute(query)

for (name, model, kilometer, color, price) in cursor:
    cars_info_data.append([name, model, kilometer, color])
    cars_price_data.append(price)

cnx.close()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(cars_info_data, cars_price_data)

new_car = input("please write your ne car info: ").split(" ")
answer = clf.predict(new_car)
print(answer)
