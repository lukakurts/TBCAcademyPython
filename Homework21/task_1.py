import json


def reading_files(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(error)


def employees_data(department_name, data):
    employees = data[department_name]["employees"]
    return employees


class Department:
    def __init__(self, department_name, data):
        self.name = data[department_name]["name"]
        self.description = data[department_name]["description"]
        self.employees = data[department_name]["employees"]
    
    def __str__(self):
        return f"Name is {self.name} {"\n"}Description of department is '{self.description}' {"\n"}Employees of {self.name} are {self.employees}"
        

    def average(self, employees):
        try:
            return f"Average salary of {self.name} is {sum(int(data["salary"]) for data in employees) / len(employees)}"
        except ZeroDivisionError as error:
            return f"Average salary of {self.name} is 0"


    def max_salary(self, employees):
        try:
            return f"Max salary of {self.name} is {max(int(data["salary"]) for data in employees)}"
        except Exception as error:
            return f"Max salary of {self.name} is 0"
    

    def min_salary(self, employees):
        try:
            return f"Min salary of {self.name} is {min(int(data["salary"]) for data in employees)}"
        except Exception as error:
            return f"Min salary of {self.name} is 0"
    

    def positions(self, employees):
        positions = {}
        counter = 1
        for data in employees:
            temp_counter = 1
            if data["position"] in positions:
                counter += 1
                positions[data["position"]] = counter
            else:
                positions[data["position"]] = temp_counter
        return f"Positions in {self.name} are {positions}"


class Employee:
    def __init__(self, number, data):
        try:
            self.name = data[number]["name"]
            self.position = data[number]["position"]
            self.salary = data[number]["salary"]
        except IndexError as error:
            print(f"{error}, please enter number between 0 and {len(data) - 1}")
            exit(1)
    

    def __str__(self):
        return f"Name is {self.name} {"\n"}Position is {self.position} {"\n"}Salary is {self.salary}"
    

def main():
    department_name = "department_3"
    data = reading_files("Homework21/homework_1.json")
    employees = employees_data(department_name, data)
    department = Department(department_name, data)
    print(department)
    print(department.average(employees))
    print(department.max_salary(employees))
    print(department.min_salary(employees))
    print(department.positions(employees))
    employee = Employee(5, employees)
    print(employee)
    
    
if __name__ == "__main__":
    main()