
# 1
seasons = ("winter","sprint", "summer", "autumn")
n = int(input("enter the month as number: "))
years_defined = [12,1,2,3,4,5,6,7,8,9,10,11]
print( "the season for that month is:", seasons[years_defined.index(n)//3])


# 2
name_set = set()
while 1:
   n = input("enter your name ")

   if n in name_set:
       print("Existing name")
   else:
       name_set.add(n)

   if n == "":
       break
print(name_set)


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

def get_airport_names():
    sql = "SELECT name from airport order by name desc"
    # sql += " WHERE Last_name='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)

print(get_airport_names())

def add_airport(icao, airport_name):
    sql = 'insert into airport (ident, name, iso_country)'
    sql += ' values ("' + icao + '","' + airport_name + '","AD")'
    print(sql)
    print("Added")
    cursor = connection.cursor()
    cursor.execute(sql)


def check_if_it_exists(icao):
    sql = ' SELECT COUNT(1) FROM airport '
    sql += 'WHERE ident = "' + icao + '" '
    print(sql)
    print("Checking...")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return(result[0][0])

def find_airport_by_icao(icao):
    sql = 'SELECT name from airport'
    sql += ' WHERE ident = "' + icao + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print("Airport name is: " , Fore.BLUE, row[0] , Fore.RESET)

while 1:
    choose = input("would you like to A: add, F:find or Q:Quit ")
    if choose == 'A' or  choose == 'a':
        icao = input("Type new icao code: ")
        name = input("Type new airport name: ")
        does_exist = check_if_it_exists(icao)
        if does_exist < 1:
            add_airport(icao, name)
        else:
            print( Fore.RED,  "Airport already exists...", Fore.RESET)

    elif choose == 'F' or  choose == 'f':
        choose = input("Type icao code: ")
        find_airport_by_icao(choose)
    else:
        break
