# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance      # Private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print("Balance:", self.__balance)


# acc = BankAccount(1000)

# acc.deposit(500)

# acc.show_balance()




#Using @property decorator 

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Enter a valid amount")
        self._balance += amount
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Enter a valid amount")
        if amount> self._balance:
            raise ValueError("Amount Exceeds balance.")
        self._balance -= amount


acc = BankAccount()
print(acc.balance)
acc.deposit(100)
print(acc.balance)
acc.withdraw(50)
print(acc.balance)
  
