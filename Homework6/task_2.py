whole_number = int(input("Please enter number: "))
print(whole_number, end="->")

if whole_number < 0 or whole_number > 1000:
    print("Please try again.")
    exit(1)
while whole_number != 1:
    if whole_number % 2 == 0:
        whole_number = whole_number // 2
        if whole_number == 1:
            print(whole_number)
        else:
            print(whole_number, end="->")
    else:
        whole_number = whole_number * 3 + 1
        print(whole_number, end="->")
