def getting_number():
    number = int(input("Please enter number:" ))
    return number


def printing_final_output(number):
    if number < 10 or number > 5432:
        print("Wrong number")
        exit(1)
    else:
        counter = 0
        for i in range(1, number + 1):
            if i % 13 == 0:
                counter += 1
                print(i)
        print(f"amount is: {counter}")


def main():
    number = getting_number()
    printing_final_output(number)

if __name__ == "__main__":
    main()