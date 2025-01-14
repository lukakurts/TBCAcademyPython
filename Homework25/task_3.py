import datetime
class TimestampMixin():
    @staticmethod
    def get_creation_time():
        return datetime.datetime.now()
    
    @staticmethod
    def get_modification_time():
        return datetime.datetime.now()


class File(TimestampMixin):
    def __init__(self, name):
        self.name = name
        print(f"file was created on {self.get_creation_time()}")
    
    def changing_name(self, name):
        self.name = name
        print(f"file name changed! to {name}")
        print(f"last modification was on {self.get_modification_time()}")
    

    
class User(TimestampMixin):
    def __init__(self, user_name):
        self.name = user_name
        print(f"user was created on {self.get_creation_time()}")

    def changing_name(self, name):
        self.name = name
        print(f"username changed to {name}!")
        print(f"last modification was on {self.get_modification_time()}")
    



def main():
    file = File("test")
    user = User("lukak")
    file.changing_name("rame")
    user.changing_name("luka123")
    


if __name__ == "__main__":
    main()
