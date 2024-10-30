from turtle import *
from random import random
from math import sqrt

n = int(input("Please enter number: "))
a = random()
b = random()
speed(10)
for i in range(4):
    pendown()
    right(90) 
    forward(100)
    penup()
    right(180)
    forward(100)
for i in range(n):
        a = random()
        b = random()
        if sqrt(a ** 2 + b **2) <= 1:
            color('red')
        else:
            color('green')
        penup()
        forward(a * 100)
        left(90)
        forward(b * 100)
        left(90)
        pendown()
        dot()
        penup()
        forward(a * 100)
        left(90)
        forward(b * 100)
        left(90)
done()
 