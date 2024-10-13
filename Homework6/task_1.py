import random
computer_number = random.randint(0,100)
counter = 0

while True:
    my_guess = int(input("Please enter your guess: "))
    if my_guess == computer_number:
        print("You are winner.")
        break
    elif my_guess > computer_number:
        print("High")
    else:
        print("Low")
    counter += 1
    if counter == 10:
        print("Computer wins.")
        break

