import random

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
