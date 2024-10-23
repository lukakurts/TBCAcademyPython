number = int(input("Please enter number: "))

if number < 0 or number > 50:
    print("Please try again.")
    exit(1)
else:
    print(" " * (number), "*")
    for i in range(1, number):
        print(" " * (number - i), "/" * i + "|" + chr(92) * i)
    print(" " * (number), "|")