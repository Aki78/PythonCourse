import random
import math

def roll_dice6():
    return random.randint(1,6)


def roll_diceN(n):
    return random.randint(1,n)

def convert_gallon_to_liter(l):
        return  3.785411784*l

def sum_int_list(arr):
    accum = 0
    for i in arr:
        accum += i
    return accum

def elimiate_even_list(arr):
    return [i for i in arr if i % 2 != 0]

def pizza_price_density(d,p):
    r = d/200
    a = math.pi * r**2
    return p/a


if __name__ == "__main__":
# 1
    print("dice number: ", roll_dice6())

# 2
    n = int(input("number of dice faces: "))
    print("dice number: ", roll_diceN(n))

# 3
while 1:
    l = float(input("type in amount in gallons (negative exists): "))
    if (l < 0):
        print("exeting...")
        break
    print("thevalue in liters is", convert_gallon_to_liter(l), "liters.")

# 4
some_list = [1,2,3,4,5,6,7,8,9,10]
print("the sum of the list is: ", sum_int_list(some_list))

# 5
some_list = [1,2,3,4,5,6,7,8,9]
print("original list is:", some_list)
print("even number eliminated list,:", elimiate_even_list(some_list))

# 6
    p1 = int(input("Type price of first pizza in dollars: "))
    d1 = int(input("Type diameter of first pizza in cm: "))
    p2 = int(input("Type price of second pizza in dollars: "))
    d2 = int(input("Type diameter of second pizza in cm: "))
    pizza1 = pizza_price_density(d1, p1)
    pizza2 = pizza_price_density(d2, p2)
    print("the value of first pizza per m^2 is: ",pizza1, " dollars.")
    print("the value of second pizza per m^2 is: ", pizza2, " dollars.")
    if (pizza1 < pizza2):
        print("choose the first pizza,")
    else:
        print("choose the second pizza,")
