n = int(input("Please enter natural number: "))
result = 0
temp_result = 0
counter = 1
if n < 1:
    print("Please try again")
    exit(1)
else: 
    while counter <= n:
        if counter % 2 != 0:
            temp_result += 1/((2 * counter) - 1)
        else:
            temp_result -= 1/((2 * counter) - 1)
        counter +=1
    result = 4 * temp_result
    print(result)