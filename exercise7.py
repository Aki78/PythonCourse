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
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

print(yhteys)
