whole_number = int(input("Please enter number: "))
reversed_number = 0
digits = 0
sum_of_digits = 0

if whole_number < 0 or whole_number > 10000:
    print("Please try again.")
    exit(1)
while whole_number > 0:
    digits = whole_number % 10
    reversed_number = reversed_number * 10 + digits
    sum_of_digits += digits
    whole_number //= 10
print(reversed_number)
print(sum_of_digits)