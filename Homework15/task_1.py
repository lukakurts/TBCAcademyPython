from random import randint

def generating_random_numbers():
    for _ in range(100):
        numbers = randint(1, 1000)
        yield numbers


def splitting_numbers(numbers):
    even_numbers_counter = 0
    odd_numbers_counter = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers_counter += 1
        else:
            odd_numbers_counter += 1
    splitted_numbers_amount = {"even": even_numbers_counter, "odd": odd_numbers_counter}
    return splitted_numbers_amount 


def main():
    numbers = generating_random_numbers()
    splitted_numbers_amount = splitting_numbers(numbers)
    print(splitted_numbers_amount)
    

if __name__ == "__main__":
    main()