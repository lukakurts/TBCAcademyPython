def prime_number(number):
    counter  = 0
    for i in range(number):
        if number % (i + 1) == 0:
            counter += 1
    if counter == 2:
        print(f"{number} is prime number.")
    else:
        print(f"{number} is not prime number.")

prime_number(2)
prime_number(4)
prime_number(37)
prime_number(85)
prime_number(97)
