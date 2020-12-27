import mysql.connector
import re 

username = input('please write your Gmail here: ')
Gmail = re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', username)
while len(Gmail) != 1:
    print("expression@string.string")
    username = input('please write your Gmail here: ')  
    Gmail = re.findall(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', username)

password = input('please write your password herer: ')
database_name = input('please write database name here: ')
user = input('please write your database user here: ')
host = input('please write your database host here: ')

cnx = mysql.connector.connect(user= user , password= '',
                                host= host,
                                database= database_name)

table = input('please write your table name here: ')

cursor = cnx.cursor()
cursor.execute('INSERT INTO %s VALUES(\'%s\',\'%s\')' %(table, username, password))
cnx.commit()

cnx.close()


