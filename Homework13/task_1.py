from random import randint

def generating_numbers():
    numbers = [randint(10, 1000000000) for i in range(100)]
    return numbers

def finding_max(numbers):
    max_number = max(numbers)
    return max_number

def finding_min(numbers):
    min_number = min(numbers)
    return min_number

def ascending_sorting_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

def descending_sorting_numbers(numbers):
    reverse_sorted_numbers = sorted(numbers, reverse=True)
    return reverse_sorted_numbers

def printing_final_output(max_number, min_number, ascending_sorted_numbers, descending_sorted_numbers):
    print("Max number is:", max_number)
    print("Min number is:", min_number)
    print("Numbers in ascending order is:", ascending_sorted_numbers)
    print("Numbers in descending order is:", descending_sorted_numbers)

def main():
    numbers = generating_numbers()
    max_number = finding_max(numbers)
    min_number = finding_min(numbers)
    ascending_sorted_numbers = ascending_sorting_numbers(numbers)
    descending_sorted_numbers = descending_sorting_numbers(numbers)
    printing_final_output(max_number, min_number, ascending_sorted_numbers, descending_sorted_numbers)

if __name__ == "__main__":
    main()