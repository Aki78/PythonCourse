#l = input("how long was zander: ")
#
#if (l < 42)
#    print("It is too short, reliease it back into the lake.")
#else:
#    print("Keep it.")
#
#c = input("Enter your cabin class: ")
#
#if (c == "LUX"):
#    print("upper-deck cabin with a balcony.")
#
#elif (c == "A"):
#    print("above the car deck, equipped with a window.")
#elif (c == "B"):
#    print("windowless cabin above the car deck.")
#elif (c == "C"):
#    print("windowless cabin below the car deck.")
#else:
#    print("Invalid cabin class.")
#
#g,h = input("Enter the gender (f or m) hemoglobin level with spaces: ")
#h = int(h)
#
#if ( g== "f"):
#    if (117 > h):
#        print("hemoglobin level too low.")
#    elif (155 < h):
#        print("hemoglobin level too heigh.")
#    else:
#        print("hemoglobin level normal.")
#elif ( g== "m"):
#    if (134 > h):
#        print("hemoglobin level too low.")
#    elif (167 < h):
#        print("hemoglobin level too heigh.")
#    else:
#        print("hemoglobin level normal.")
#else:
#    print("not a gender")

def is_leap_year():
    y = int(input("input year: " ))
    if y % 4 != 0:
        return ("Not Leap year: ")
    if y % 400 == 0:
        return ("Leap year: ")
    if y % 100 == 0:
        return("Not Leap year: ")
    return ("Leap Year.")
print(is_leap_year())
