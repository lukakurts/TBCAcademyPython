whole_number = int(input("Please enter number: "))
counter = 1
number_saver = whole_number
if whole_number < 0 or whole_number > 10:
    print("Please try again.")
    exit(1)

while counter < whole_number * 2:
    counter2 = 1
    if counter <= whole_number:
        while counter2 < counter + 1:
            print(counter2, end=" ")
            counter2 +=1
        print()
    else:
        while counter2 < number_saver:
            print(counter2, end=" ")
            counter2 +=1
        print()
        number_saver -= 1
    counter += 1
    