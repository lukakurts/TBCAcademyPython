class Student():
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, values):
        self._grades = values

    def add_scores(self, score):
        if score < 0 or score > 100:
            print(f"{score} is incorrect score")
        else:
            self._grades.append(score)
        
    def get_average(self):
        _sum = sum(self._grades)
        average = _sum / len(self._grades)
        return f"average of the scores is {average:.2f}"
    
    def get_scores(self):
        return f"Scores of student {self._name} are {self._grades}"

def main():
    student = []

    student1 = Student("luka")
    student1.add_scores(90)
    student1.add_scores(76)
    student1.add_scores(58)
    student1.add_scores(104)
    student2 = Student("nika")
    student2.add_scores(59)
    student2.add_scores(78)
    student2.add_scores(59)
    student2.add_scores(64)


    student.append(student1)
    student.append(student2)
    for students in student:
        print(f"student name is {students.name}, {students.get_average()}, {students.get_scores()}")

if __name__ == "__main__":
    main()