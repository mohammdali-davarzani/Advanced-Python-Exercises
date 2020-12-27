from mysql import connector

cnx = connector.connect (user = 'root', password= '',
                        host= '127.0.0.1',
                        database= 'employee')

cursor = cnx.cursor()

query = 'SELECT * FROM info;'
cursor.execute(query)

data = list()
names = list()
heights = list()
weights = list()

for (name, weight, height) in cursor:

    data.append([name, height, weight])

    data.sort(key = lambda item: item[1])

item = -1
for i in data:
    print (*data[item])
    item -= 1


cnx.close()