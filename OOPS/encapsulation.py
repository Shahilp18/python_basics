
#! Encapsulation
#* Wrapping data & functions inot single unit 
#* _ protected | __ private

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #? Private

    def get_balance(self):
        return self.__balance;

    def set_balace(self, newBalance):
        self.__balance = newBalance

a1 = BankAccount("Shah Rukh Khan", 500_000)

a1.set_balace(4000)
print(a1.name, a1.get_balance())

