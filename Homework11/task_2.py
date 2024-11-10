def gcd_iteration(a, b):
    m = min(a, b)
    result = 0
    while m > 0:
        if a % m == 0 and b % m == 0:
            result = m
            break
        m -= 1
    return result

def gcd_recursion(a, b):
    if b == 0:
        return a
    return gcd_recursion(b, a % b)


def main():
    first_number = int(input("Please enter first number: "))
    second_number = int(input("Please enter second number: "))
    if (first_number and second_number) > 10000 or (first_number and second_number) < 0:
        print("Please try again")
        exit(1)
    else:
        print(gcd_iteration(first_number, second_number))
        print(gcd_recursion(first_number, second_number))

if __name__ == "__main__":
    main()