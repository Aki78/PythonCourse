import random

name = input("Type your name: ")
print("Hello, " + name + "!")

r = float(input("type in radius: "))
print("the area of the circle is: ", str(3.1416*float(r)*float(r)))


x, y = input("type width and height of the rectangle with a space inbetween: ").split()
print("the parimeter of the rectangle is: " + str(2*float(x) + 2*float(y)))


x, y, z = input("type 3 integers in a row with spaces inbetween").split()
print("the sum of given 3 numbers is " + str(int(x)+int(y)+int(z)))

t = float(input("Enter talents: "))
print("\n")
p = float(input("Enter pounds: "))
print("\n")
l = float(input("Enter lots: "))
print("\n")

#t1 = 20*p
#p1 = 32*l
#g1 = l / 13.3
total = 20*32*13.3 * t + 32*13.3*p +  13.3*l 
k = int(total/1000)
g = (total/1000 - int(total/1000)) * 1000
print("The weight in modern units:\n")
print(k , "kilograms and", "{:.2f}".format(g), "grams.")

print(random.randint(0,9), random.randint(0,9), random.randint(0,9))
print(random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6))
