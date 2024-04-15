import os

# display balance
# display owner
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount # withdraw the amount from balance
        else:
            print(f"insufficient funds -> your balance is: {self.balance} and you trying to get {amount}")

    def display_balance(self):
        print(f"Your balance is: {self.balance}")

    def display_owner(self):
        print(f"The owner of the account is: {self.owner}")





def main():
    # in Main Create a bank account with owner (your name ) and balance 0.0
    account1 = BankAccount("John", 200.0)
    # Deposit money to the bank account :
    # 	Deposit 100
    account1.deposit(100)
    # 	Deposit 200
    account1.deposit(200)
    # 	print balance
    account1.display_balance()
    # Withdraw money from account
    # 	withdraw 150
    account1.withdraw(150)
    # 	print balance
    account1.display_balance() #150
    # 	withdraw 200
    account1.withdraw(200)
    # 	check that the action could not be done
    # 	print balance and check that it is still the same.
    account1.display_balance()
    # print owner
    account1.display_owner()

    # os.remove("file.txt")




if __name__ == '__main__':
    main()