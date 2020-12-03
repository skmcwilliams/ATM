#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date, time
from random import randint


class Account():
    """Account has same attributes as sublcasses"""
    def __init__(self,current_bal,current_no,savings_bal,savings_no):
        Current.__init__(self)
        Savings.__init__(self)

    def deposit(self,amount,account):
        """method to deposit funds"""
        if account == 'current':
            print(f'Initiating Deposit to account# {self.current_no} - Prior balance of {self.current_bal} will be increased by {amount}.')
            self.current_bal = self.current_bal + amount
            print(f'Your New Balance is {self.current_bal}.')
            
        if account == 'savings':
            print(f'Initiating Deposit to account# {self.current_no} - Prior balance of {self.savings_bal} will be increased by {amount}.')
            self.savings_bal = self.savings_bal + amount
            print(f'Your New Balance is {self.savings_bal}.')
              
    def withdraw(self, amount, account):
        """withdraws from current or savings accounts"""
        if self.current_bal-amount > 0 and account == 'current':
            print(f'Initiating Withdraw from account# {self.current_no} - Prior balance of {self.current_bal} will be decreased by {amount}.\n')
            self.current_bal = self.current_bal - amount
            print(f'Transaction complete. Your new balance is: {self.current_bal}') 
        
        if account == 'savings' and self.savings_bal-amount > 0:
            print(f'Initiating Withdraw from account# {self.savings_no} - Prior balance of {self.savings_bal} will be decreased by {amount}.\n') 
            self.savings_bal = self.savings_bal-amount
            print(f'Transaction Complete. Your new balance is {self.savings_bal}')
            
        while account=='savings' and self.savings_bal - amount < 0:
            print('Insufficient funds, please try agian')
            break
        
        while account=='current' and self.current_bal - amount < 0:
            print('Insufficient funds, please try agian')
            break
        
        if account != 'savings' and account != 'current':
            print('please check account type and try again')
           
    def CreateTransaction(self,trans_type,amount,account):
        """User creates transaction when making deposit/withdraw, call within class"""
        if trans_type == "deposit":
           Account.deposit(self, amount,account)
        if trans_type == 'withdraw':
            Account.withdraw(self, amount,account)
            
    
class Savings(Account):
    """create base class Savings"""
    def __init__(self,**args):
        self.savings_no = 100238
        self.savings_bal = 25000
        self.args = args
        
    def withdraw(self,amount,account):
        Account.withdraw(self,amount,'savings')

        
class Current(Account):  
    """create base class Current"""
    def __init__(self,**args):
        self.current_no = 100239
        self.current_bal = 1000
        
    def withdraw(self, amount, account):
        """create method to withdraw from account"""
        Account.withdraw(self,self.current_bal,'current')
        
        if self.current_bal-amount > 0 and account == 'current':
            print(f'Initiating Withdraw from account# {self.current_no} - Prior balance of {self.current_bal} will be decreased by {amount}.\n')
            self.current_bal = self.current_bal - amount
            print(f'Transaction complete. Your new balance is: {self.current_bal}') 
        
        if account == 'savings' and self.savings_bal-amount > 0:
            print(f'Initiating Withdraw from account# {self.savings_no} - Prior balance of {self.savings_bal} will be decreased by {amount}.\n') 
            self.savings_bal = self.savings_bal-amount
            print(f'Transaction Complete. Your new balance is {self.savings_bal}')
            
        while account=='savings' and self.savings_bal - amount < 0:
            print('Insufficient funds, please try agian')
            break
        
        while account=='current' and self.current_bal - amount < 0:
            print('Insufficient funds, please try agian')
            break
        
        if account != 'savings' and account != 'current':
            print('please check account type and try again')
            
        

class ATM_Transactions(Account):
    """I'm not sure what the class does"""
    def __init__(self):
        self.trans_date = date.today()
        self.trans_id = randint(1000,1200)
        self.trans_type = 999 #  not sure what to do here 
        self.amount = 999 # not sure what to do here
        
    def modifies(self,trans_type,amount):
        """not sure what this is supposed to do"""
        pass


class Customer(Account):
    """Customer class uses attributes from Account, has additional attributes"""
    def __init__(self, name, pin, address='Mainville', dob='BDay', card='1234567890'):
        self.name = name
        self.address = address
        self.dob = dob
        self.card = card
        self.pin = pin
    
    def VerifyPassword(self):
        """Make sure that customer's pin number is correct"""
        if self.pin == 1234:
            return True
        else:
            print('Pin error, please try again')


class ATM(Account):
    """Simulates an ATM where it identifies itself to client and posts balances"""
    def __init__(self, current_bal,current_no,savings_bal,savings_no,location='North and Main', manager='TechCorp Bank',):
        super().__init__(current_bal,current_no,savings_bal,savings_no)
        self.location = location
        self.manager = manager
        self.current_bal = self.current_bal
        self.current_no = self.current_no
        self.savings_no = self.savings_no
        self.savings_bal = self.savings_bal
        
    def identifies(self):
        return print(f'Welcome to the {self.location} ATM managed by {self.manager}!')
        
    
    def transactions(self): # not sure what this method would be, a list of options for the user?
        pass
        
    def post_balance(self): # post balance is handled by printing balance when called
        self.current_bal = self.current_bal
        self.current_no = self.current_no
        self.savings_no = self.savings_no
        self.savings_bal = self.savings_bal
        print(f'Current Balance, Account# {self.current_no}: {self.current_bal}\nSavings Balance, Account# {self.savings_no}: {self.savings_bal}')


class Bank(ATM, Customer):
    """Bank class is designed to be facade for client. Bank class is Aggregation 
    of other classes and will run while pin (1234) is correct"""
    
    def __init__(self,pin,code=123445, address='Mainvill, WA'):
        self.code=code
        self.address=address
        self.customer = Customer('Client',pin)
        self.atm = ATM(0,0,0,0)
        

        while self.customer.VerifyPassword() is True:
            choices = ['View Balance', 'Withdraw', 'Deposit','Exit']
            choice = input(f'What would you like to do, {*choices,}?\n').lower()

            if choice == 'view balance':
                self.atm.post_balance()
                continue
                
            if choice == 'exit':
                print('Session Closed. Your final balance is:')
                self.atm.post_balance()
                break
            
            if choice == 'deposit' or choice == 'withdraw':
                acct = input('Which Account (Current or Savings)? ').lower()
                num = int(input(f'OK, how much to {choice}? '))
                self.atm.CreateTransaction(choice,num,acct)
                continue


    def manages(ATM): # not sure what this would do
        pass
    
    def maintains(Customer): # not sure what this would do
        pass
    
    
if __name__ == '__main__':
   pin = int(input('Please enter 4 digit pin: \n')) # pin number is 1234
   bank = Bank(pin)
   
   
   
