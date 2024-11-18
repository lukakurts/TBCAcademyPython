from random import randint

def creating_lists(first_list_size, second_list_size, third_list_size):
    first_list = [randint(10, 100) for i in range(first_list_size)]
    second_list = [randint(10, 100) for i in range(second_list_size)]
    third_list = [randint(10, 100) for i in range(third_list_size)]
    return first_list, second_list, third_list

def calculating_sum(first_list, second_list, third_list):
    new_list = list(map(lambda a, b, c: (a + b +c), first_list, second_list, third_list))
    return new_list
    

def main():
    first_list, second_list, third_list = creating_lists(12, 24, 5)
    print(calculating_sum(first_list, second_list, third_list))

if __name__  == "__main__":
    main()