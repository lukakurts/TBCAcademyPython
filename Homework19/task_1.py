import json


def calculating_avg_salary():
    avg_salary = {}
    try:
        with open("Homework19/homework_1.json", "r") as file:
            data = json.load(file)
            for k in data:
                counter = 0
                _sum = 0
                for values in data[k]["employees"]:
                        try:
                            _sum += int(values["salary"])
                            counter += 1
                        except ValueError as error:
                            values["salary"] = 0
                            _sum += values["salary"]
                            counter += 1
                            print(error)
                try:
                    average_salary = _sum / counter
                except ZeroDivisionError as error:
                    print(error)
                    average_salary = 0
                avg_salary[k] = average_salary
    except OSError as error:
        print(error)
    print(avg_salary)
    with open("Homework19/avg_salary.json", "w") as file:
        json.dump(avg_salary, file, indent=4)


def main():
    calculating_avg_salary()


if __name__ == "__main__":
    main()