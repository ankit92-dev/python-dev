"""#Create Account class eith 2 attributes-balance and accunt no.
#Create methodsfor debit,credit and printing the balance.
"""
class Account:
    def __init__(self, bal, acc): #Constructor
        self.balance = bal
        self.account_no = acc

    def debit(self, amount): #debit function
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount): #credit function
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance()) #Calling get_balance() function internally

    def get_balance(self): #Print function
        return self.balance


# Create account instance
acc1 = Account(10000, 12345)
#Multiple accounts can be added
# Print initial details
print("Initial Balance:", acc1.balance)
print("Account Number:", acc1.account_no)

# Perform transactions
acc1.debit(2000)
acc1.credit(1500)