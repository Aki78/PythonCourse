# 1
x = 1
while x < 1001:
    if x%3 == 0:
        print(x)
    x+=1

# 2
while 1:
    l = float(input("type in your inch value: "))
    if (l < 0):
        print("exeting...")
        break
    print("the value is", 2.54*l, "cm.")

# 3

largest = -10000000000000000000
smallest = 10000000000000000000

while 1:
    l = input("type in an integer: ")

    if (l.lstrip("-").isdigit()):
        l = int(l)
        if (l > largest):
            largest = l
        if (l < smallest):
            smallest = l
    else:
        print("largest number: ", largest, "smallest number: ", smallest)
        break

# 4
import random
r = random.randint(1,10)
while 1:
    l = int(input("guess a number between 1-10: "))
    if ( r> l):
        print("too low")
    elif (r < l):
        print("too high")
    else:
        print("correct")
        break

# 5
import hashlib
from getpass import getpass

l = 5
# user_name = "python"
# pass_word = "rules"
# using sha256 for security
while l > -1:
    h = hashlib.new('sha256')
    h.update("pythonrules".encode())
    print(h.hexdigest())

    my_hash = "fd7a4c43ad7c20dbea0dc6dacc12ef6c36c2c382a0111c92f24244690eba65a2"
    u = input("user name: ")
    p = getpass("password (chars will not show): ")

    h = hashlib.new('sha256')
    h.update((u + p).encode())

    if (my_hash == h.hexdigest()):
        print("access approved, welcome!")
        break
    else:
        print("access denied", l, "times left")
        if (l == 0):
            print("ACCOUNT TERMINATED, please contact the IT department to renew your account. (Phone number: (+1) 045-555-6390.")
    l -= 1

# 6
# a python loop is far too slow for this task, so I used numpy instead
# make sure to install numpy first

import numpy as np

n = int(input("type in a large integer (less than 100000000): "))
ps = np.random.uniform(-1,1, size = (n, 2))
print("Estimated pi value is: ", len(np.argwhere(np.linalg.norm(ps, axis=1) < 1))/n*4)
