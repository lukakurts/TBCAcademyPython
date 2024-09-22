number = int(input("Please enter number: "))
number1 = 0
number2 = 1
if number < 0 or number >= 20:
    print("Please try again")
    exit(1)
elif number == 0:
    print(number1)
else:
    for i in range(number):
        fibonacci_number = number1 + number2
        number2 = number1
        number1 = fibonacci_number
    print(fibonacci_number)