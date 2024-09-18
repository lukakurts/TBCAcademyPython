whole_number = int(input("please enter Whole number: "))
if whole_number > 0 and whole_number <= 10:
    if whole_number % 2 == 0 and whole_number % 3 == 0 and whole_number % 5 == 0:
        print(2, 3, 5)
    elif whole_number % 2 == 0 and whole_number % 5 == 0:
        print(2, 5)
    elif whole_number % 2 == 0 and whole_number % 3 == 0:
        print(2, 3)
    elif whole_number % 5 == 0:
        print(5)
    elif whole_number % 3 == 0:
        print(3)
    elif whole_number % 2 == 0:
        print(2)
    