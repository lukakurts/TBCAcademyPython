whole_number = int(input("Please enter number: "))
counter = 0
number_saver = whole_number + 1
if whole_number < 0 or whole_number > 10:
    print("Please try again.")
    exit(1)

while counter < whole_number + 1:
    counter2 = 0
    counter3 = counter
    print(" " * number_saver * 2, end=" ")
    while counter3 > 0:
        print(counter3, end=" ")
        counter3 -= 1
    while counter2 < counter + 1:
        print(counter2, end=" ")
        counter2 += 1
    print()
    number_saver -= 1
    counter += 1