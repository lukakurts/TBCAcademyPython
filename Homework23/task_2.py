class BankAccount():
    def __init__(self, balance):
        self.balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, amount):
        print(f"Adding {amount} in your balance")
        self._balance += amount
    
    def withdraw(self, amount):
        print(f"Withdrawing {amount} from your balance")
        if self._balance < amount:
            print(f"Not enough money!")
        else:
            self.balance -= amount
    
    def get_balance(self):
        return f"Your balance is: {self._balance}"
    

def main():
    account1 = BankAccount(12456)
    account1.deposit(100)
    print(account1.get_balance())
    account1.withdraw(13000)
    print(account1.get_balance())
    account1.withdraw(120)
    print(account1.get_balance())

if __name__ == "__main__":
    main()