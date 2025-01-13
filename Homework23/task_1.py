class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, v):
        self._name = v

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, v):
        self._age = v
    
    def get_info(self):
        return f"name is {self._name}, age is {self._age}"


def main():
    p1 = Person("luka", 21)
    print(p1.get_info())
    p2 = Person("nika", 45)
    print(p2.get_info())
    p3 = Person("jon", 125)
    p3.name = "jane"
    print(p3.get_info())


if __name__ == "__main__":
    main()