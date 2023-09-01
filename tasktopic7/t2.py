#Write a program in python to create a class with name Bank. In Bank class create a method interest() which return 0 value. Now override interest method in class Sbi and Pnb.

class Bank:
    def interest(self):
        return 0

class Sbi(Bank):
    def interest(self):
        return 5.0  # SBI Bank's interest rate is 5%

class Pnb(Bank):
    def interest(self):
        return 4.5  # PNB Bank's interest rate is 4.5%

# Create instances of Sbi and Pnb classes
sbi_bank = Sbi()
pnb_bank = Pnb()

# Calculate and display the interest rates
print("SBI Bank Interest Rate:", sbi_bank.interest())
print("PNB Bank Interest Rate:", pnb_bank.interest())