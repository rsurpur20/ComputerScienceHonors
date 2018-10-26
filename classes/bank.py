#withdraw, transfer, deposits, closing an account

class Account:
    def __init__(self,balance):
        self.balance=balance

    def checkbalance(self):
        return self.balance
    def withdraw(self,withdrawamt):
        if withdrawamt<self.balance:
            self.balance=self.balance-withdrawamt
        return self.balance
    def deposit(self):

open=input("Would you like to open a bank account? Type 'yes' or 'no'.\n")
if open=="yes" or open=="Yes":
    balance=float(input("How much would you like to put into your bank account?\n$"))
    account1=Account(balance)
    print("Your current balance: $"+str(account1.checkbalance()))
    while True:
        option=input("What would you like to do with your account. Options: 'withdraw' 'check balance' 'deposit' ")
        #WITHDRAW:
        if option=="withdraw" or option=="Withdraw":
            withdrawamt=float(input("How much would you like to withdraw?\n$"))
            if withdrawamt>balance:
                print("You do not have enough money in your account to withdraw $"+str(withdrawamt))
            print("Your current balance: $"+str(account1.withdraw(withdrawamt)))
        #CHECK BALANCE
        elif option=="check balance" or option=="Check Balance":
            print("Your current balance: $"+str(account1.checkbalance()))
        #DEPOSIT
        elif option=="deposit" or option=="Deposit":
