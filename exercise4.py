## 1
#x = 1
#while x < 1001:
#    if x%3 == 0:
#        print(x)
#    x+=1
#
## 2
#while 1:
#    l = float(input("type in your inch value: "))
#    print("the value is", 2.54*l, "cm.")
#    if (l < 0):
#        break
#
## 3
#
#largest = -10000000000000000000
#smallest = 10000000000000000000
#
#while 1:
#    l = input("type in an integer: ")
#
#    if (l.lstrip("-").isdigit()):
#        l = int(l)
#        if (l > largest):
#            largest = l
#        if (l < smallest):
#            smallest = l
#    else:
#        print("largest number: ", largest, "smallest number: ", smallest)
#        break

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



