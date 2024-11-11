def getting_information():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    age = int(input("Please enter your age: "))
    city = input("Please enter city you were born: ")
    return first_name, last_name, age, city


def printing_final_output(first_name, last_name, age, city):
    print(f"Hello {first_name} {last_name}")
    print(f"Age: {age}")
    print(f"City: {city}")


def main():
    first_name, last_name, age, city = getting_information()
    printing_final_output(first_name, last_name, age, city)

if __name__ == "__main__":
    main()