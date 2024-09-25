number = int(input("Please enter number: "))

if number < 0 or number > 50:
    print("Please try again.")
    exit(1)
else:
    for i in range (1, number + 1):
        count = 0
        print(i, " - ", end= " ")
        for l in range(1, number + 1):
            if(i % l == 0):
                count += 1
                if count > 3:
                    break
                print(l, end= " ")
        print()