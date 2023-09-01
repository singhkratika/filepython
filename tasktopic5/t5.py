#deposite()-thos method is used to deposite ()moneyin account.
#with draw()-this method is used to withdraw money from account
#enquiry()-this method provided balance enquiry
#bankaccount class


class Bank:
    def _init_(self, acno, name, balance):
        self.acno = acno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance =self.balance + amount
            print("Deposited",amount, "successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance-amount
            print("Withdrew", amount ,"successfully.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def enquiry(self):
        print("Account Number: ",self.acno)
        print("Account Holder: ",self.name)
        print("Balance: ",self.balance)

account = Bank(456,"juhi",5000)

account.enquiry()
account.deposit(1000)
account.withdraw(2000)
account.enquiry()