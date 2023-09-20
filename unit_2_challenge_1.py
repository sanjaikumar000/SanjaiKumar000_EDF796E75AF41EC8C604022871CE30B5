class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount} into account {self.__account_number}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount} from account {self.__account_number}"
        else:
            return "Invalid withdrawal amount or insufficient balance"

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}"


account = BankAccount(905673518152, "gold.d.roger", 50000)

print(account.display_balance())    
print(account.deposit(1000))        
print(account.withdraw(20000))      
print(account.display_balance())  