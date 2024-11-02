from random import randint

def generating_numbers():
    numbers = []
    for i in range(50):
        numbers.append(randint(1, 30))
    return numbers

def deleting_duplicate_numbers(numbers: list):
    unique_numbers = []
    for elements in numbers:
        if elements not in unique_numbers:
            unique_numbers.append(elements)
    return unique_numbers

def final_result_output(unique_numbers: list):
    print(unique_numbers)
    print("Length is:", len(unique_numbers))

def main():
    numbers = generating_numbers()
    unique_numbers= deleting_duplicate_numbers(numbers)
    final_result_output(unique_numbers)

if __name__ == "__main__":
    main()