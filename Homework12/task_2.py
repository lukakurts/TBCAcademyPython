from random import randint

def generating_numbers():
    numbers = []
    for i in range(50):
        numbers.append(randint(1, 30))
    return numbers

def creating_new_list(numbers: list):
    new_list = []
    for elements in numbers:
        for i in range(elements):
            new_list.append(elements)
    return new_list

def final_result_output(new_list: list):
    print(new_list)
    print("Length of new list is:", len(new_list))



def main():
    numbers = generating_numbers()
    new_list = creating_new_list(numbers)
    final_result_output(new_list)

if __name__ == "__main__":
    main()