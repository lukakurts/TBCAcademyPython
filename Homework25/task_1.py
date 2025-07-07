from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on():
        pass

    @abstractmethod
    def turn_off():
        pass

class WashingMachine(Appliance):
    @staticmethod
    def turn_on():
        print(f"Washing machine is now on")

    @staticmethod 
    def turn_off():
        print(f"Washing machine is now off")


class Refrigirator(Appliance):
    @staticmethod
    def turn_on():
        print(f"Refrigirator is now on")

    @staticmethod    
    def turn_off():
        print(f"Refrigirator is now off")


def operate_appliance(appliance):
        appliance.turn_on()
        appliance.turn_off()


def main():
    washing_machine = WashingMachine()
    refrigirator = Refrigirator()
    operate_appliance(washing_machine)
    operate_appliance(refrigirator)
    

if __name__ == "__main__":
    main()