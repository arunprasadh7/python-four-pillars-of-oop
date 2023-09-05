#Banking system problem
from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def displayBalance(self):
        return 0



class SavingsAccount:
    def __init__(self):
        # [key] [0] => name ; [key] [1] => balance
        self.savingsAccounts = {}

    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccounts[self.accountNumber] = [name,initialDeposit]
        print('Account creation successful. Your account number is',self.accountNumber)

    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.accountNumber[0] == name:
                print('Authentication Successfull')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authentication failed')
                return False
        else:
            print('Authentication failed')
            return False


    def withdraw(self, withdrawlAmount):
        if withdrawlAmount > self.savingsAccounts[self.accountNumber][1]:
            print('Insufficient Balance')
            return False
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawlAmount
            print('Withdrawl successful')
            self.displayBalance()

    def deposit(self,depositAmount):
        self.savingsAccounts[self.accountNumber] += depositAmount
        print('Amount successfully deposited')
        self.displayBalance()

    def displayBalance(self):
        print('Available balance is',self.savingsAccounts[self.accountNumber][1])

#objects creation

savingsAccount = SavingsAccount()
while True:
    print('Enter 1 to create new account.')
    print('Enter 2 to access existing account.')
    print('Enter 3 to exit.')
    userChoice = int(input())
        if userChoice == 1:
            name = input('Enter your name: ')
            deposit = int(input('Enter deposit amount: '))
            savingsAccount.createAccount(name,deposit)
        elif userChoice == 2:
            name = input('Enter acc name: ')
            accNumber = int(input('Enter acc number :'))
            authStatus = savingsAccount.authenticate(name,accNumber)
            if authStatus == True:
                while True:
                    print('Enter 1 to withdraw')
                    print('Enter 2 to deposit')
                    print('Enter 3 to display available balance.')
                    print('Enter 4 to go back to previous menu')
                    userChoice = int(input())
                    if userChoice == 1:
                        print('Enter withdrawl amount: ')
                        withdrawlAmount = int(input())
                        savingsAccount.withdraw(withdrawlAmount)
                    elif userChoice == 2:
                        print('Enter amount to be deposited.')
                        amtDeposit = int(input())
                        savingsAccount.deposit(amtDeposit)
                    elif userChoice == 3:
                        print(savingsAccount.displayBalance())
                    elif userChoice == 4:
                        break

        elif userChoice == 3:
            quit()


