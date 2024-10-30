from task_2 import gcd_iteration

def lcm(a, b):
    result = (a * b) / gcd_iteration(a, b)
    return result



def main():
    first_number = int(input("Please enter first number: "))
    second_number = int(input("Please enter second number: "))
    if (first_number and second_number) > 10000 or (first_number and second_number) < 0:
        print("Please try again")
        exit(1)
    else:
        print(lcm(first_number, second_number))


if __name__ == "__main__":
    main()