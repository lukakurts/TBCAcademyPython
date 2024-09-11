import math

a = int(input("გთხოვთ შეიყვანოთ პირველი გვერდი"))
b = int(input("გთხოვთ შეიყვანოთ მეორე გვერდი"))
c = int(input("გთხოვთ შეიყვანოთ მესამე გვერდი"))
p = a + b + c
p1 = p / 2
s = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - c))
print("პერიმეტრი არის ", p)
print("ფართობი არის ", s)
