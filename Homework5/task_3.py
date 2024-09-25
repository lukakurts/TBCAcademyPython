number = int(input("Please enter number: "))
number1 = 0
number2 = 1
count = 0
if number < 0 or number >= 20:
    print("Please try again")
    exit(1)
elif number == 0:
    print(number1)
else:
    print(number1, end=" ")
    while count < number:
        fibonacci_number = number1 + number2
        number2 = number1
        number1 = fibonacci_number
        count += 1
        print(fibonacci_number, end=" ")