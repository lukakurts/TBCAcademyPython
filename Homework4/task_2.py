import random
number = int(input("Please enter number: "))
max_number = 0
if number < 0 or number > 30:
    print("Please try again")
    exit(1)
else:
    for i in range(number):
        numbers_random = random.randint(0, 1000)
        if numbers_random > max_number:
            max_number = numbers_random
    print(max_number)

    
