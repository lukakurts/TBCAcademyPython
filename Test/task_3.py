from random import choice

def generating_symbols_randomly():
    symbols = ["R", "P", "S"]
    random_symbol = choice(symbols)
    return random_symbol


def main():
    for i in range(2):
        random_symbol = generating_symbols_randomly()
        user_choice = input("Please enter R, P or S: ")
        if user_choice.upper() != "R" and user_choice.upper() != "P" and user_choice.upper() != "S":
            print("try again")
            exit(1)
        else:
            if random_symbol == "R" and user_choice.upper() == "S":
                print("You lost!")
                break
            elif random_symbol == "S" and user_choice.upper() == "P":
                print("You lost!")
                break
            elif random_symbol == "P" and user_choice.upper() == "R":
                print("You lost!")
                break
            elif random_symbol == "P" and user_choice.upper() == "P" or random_symbol == "R" and user_choice.upper() == "R" or random_symbol == "S" and user_choice.upper() == "S":
                print("Draw")
                print("Try again!")
            else:
                print("You win!")
                break    

if __name__ == "__main__":
    main()