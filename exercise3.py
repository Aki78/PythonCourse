l = input("how long was zander: ")

if (l < 42)
    print("It is too short, reliease it back into the lake.")
else:
    print("Keep it.")



c = input("Enter your cabin class: ")

if (c == "LUX"):
    print("upper-deck cabin with a balcony.")

elif (c == "A"):
    print("above the car deck, equipped with a window.")
elif (c == "B"):
    print("windowless cabin above the car deck.")
elif (c == "C"):
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


g,h = input("Enter the gender (f or m) hemoglobin level with spaces: ")
h = int(h)

if ( g== "f"):
    if (117 > h):
        print("hemoglobin level too low.")
    elif (155 < h):
        print("hemoglobin level too heigh.")
    else:
        print("hemoglobin level normal.")
elif ( g== "m"):
    if (134 > h):
        print("hemoglobin level too low.")
    elif (167 < h):
        print("hemoglobin level too heigh.")
    else:
        print("hemoglobin level normal.")

else:
    print("not a gender")


g = input("input iy")
