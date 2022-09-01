# section 1
import random

n = int(input("how many times do you want to roll the dice?: "))
accum = 0

for i in range(n):
    accum += random.randint(1,6)

print("the sum is: ", accum)

# section 2

arr = []
while 1:
    n = input("how many times do you want to roll the dice?: ")
    if (not n.isdigit()):
        break
    arr.append(int(n))
arr.sort(reverse=True)
print("the top 5 values are: ", arr[:5])

# section 3
all_prime_numbers = [2,3]
n = int(input("type in a number to check if its prime: "))
for i in range(2,n+1):
    has_mod = 0
    for j in all_prime_numbers: 
        if (i % j == 0):
            has_mod = 1
    if (has_mod != 1):
        all_prime_numbers.append(i)
        has_mod = 0

if  (n in all_prime_numbers):
    print("The number is a prime")
else:
    print("The number is not a prime")

# section 4
arr = []
for i in range(5):
    n = input("type in a city name: ")
    arr.append(n)
print("Tye cities you typed are:")
for i in arr:
    print(i)

