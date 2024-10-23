from random import random
from math import sqrt

n = int(input("Please enter natural number: "))
counter = 0
if n < 1:
    print("Please try again")
    exit(1)
else:
    for i in range(n):
        a = random()
        b = random()
        if sqrt(a ** 2 + b **2) <= 1:
            counter += 1
    result = 4 * counter / n
    print(result)