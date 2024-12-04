def getting_number():
    number = int(input("Please enter number: "))
    return number


def fibonacci_sequence(number):
    first_number = 0
    second_number = 1
    fibonacci_number = 0
    yield 0
    for i in range(number):
        fibonacci_number += second_number
        second_number = first_number
        first_number = fibonacci_number
        yield fibonacci_number


def main():
    number = getting_number()
    fibonacci_number = fibonacci_sequence(number)
    for fibonacci in fibonacci_number:
        print(fibonacci)



if __name__ == "__main__":
    main()