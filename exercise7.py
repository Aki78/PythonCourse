#
## 1
#seasons = ("winter","sprint", "summer", "autumn")
#n = int(input("enter the month as number: "))
#years_defined = [12,1,2,3,4,5,6,7,8,9,10,11]
#print( "the season for that month is:", seasons[years_defined.index(n)//3])
#
#
## 2
#name_set = set()
#while 1:
#    n = input("enter your name ")
#
#    if n in name_set:
#        print("Existing name")
#    else:
#        name_set.add(n)
#
#    if n == "":
#        break
#print(name_set)


# 3

import mysql.connector
from colorama import Fore

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

def get_employees_byLast_name():
    sql = "SELECT name from airport"
    # sql += " WHERE Last_name='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return

print(get_employees_byLast_name())

def add_airport(x):
    print(x)

def find_airport_by_icao(icao):
    sql = 'SELECT name from airport'
    sql += ' WHERE ident = "' + icao + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print("Airport name is: " , Fore.RED, row[0] , Fore.RESET)
    return

while 1:
    choose = input("would you like to A: add, F:find or Q:Quit ")
    if choose == 'A' or  choose == 'a':
        add_airport()
    elif choose == 'F' or  choose == 'f':
        choose = input("Type icao code: ")
        find_airport_by_icao(choose)
    else:
        break


