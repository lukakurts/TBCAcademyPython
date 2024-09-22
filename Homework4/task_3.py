number = int(input("Plese enter number: "))

if number < 0 or number > 1000:
    print("Please try again")
    exit(1)
else:
    for i in range(1, number + 1):
        if number % i == 0:
            print(i , end= " ")
