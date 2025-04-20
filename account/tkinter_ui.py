from tkinter import *
from tkinter import ttk

import logging
from account import BankAccountLogistics
import require_support 
import balance, atm_store

class AccountHomeUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Bank of Banking')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.login_frame = ttk.Frame(self.root, padding='3 3 12 12')
        self.account = self.create_account_ui()
        self.withdraw_and_deposit = balance.WithdrawsAndDeposits()
        self.balance = balance.Balance(self.account.account_owner, self.account.daily_withdraw_limit, self.withdraw_and_deposit)
        self.store = atm_store.Store()
       
        self.root.mainloop()
   
    def create_account_ui(self):
        self.login_frame.grid(column=0, row=0, sticky=(N, W, E, S))
      
        name = StringVar()
        name_entry = ttk.Entry(self.login_frame, width = 7, textvariable = name)
        name_entry.grid(column = 2, row = 1, sticky = (W, E))
        ttk.Label(self.login_frame, text='First, middle, last name').grid(column = 3, row = 1, sticky = (W))

        daily_withdrawl_limit = StringVar()
        daily_withdrawl_entry = ttk.Entry(self.login_frame, width = 7, textvariable = daily_withdrawl_limit)
        daily_withdrawl_entry.grid(column = 2, row = 2, sticky = (W, E))
        ttk.Label(self.login_frame, text='Daily withdrawl limit').grid(column = 3, row = 2, sticky = (W))

        ttk.Button(self.login_frame, text = 'Create Account', command=self.account_home_ui).grid(column = 2 , row = 3, sticky = (W, E))

        return BankAccountLogistics(name, daily_withdrawl_limit)

    def account_home_ui(self):
        self.login_frame.destroy()
        
        self.account_home_frame = ttk.Frame(self.root, padding='3 3 12')
        self.account_home_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.account_home_frame, text='Balance').grid(column=1, row=1, sticky=(W))
        ttk.Label(self.account_home_frame, text='$'+str(self.balance.balance)).grid(column=2, row=1, sticky=(W))

        ttk.Button(self.account_home_frame, text='Transactions', command=self.transactions_ui).grid(column=2, row=3, sticky=(W))

        ttk.Button(self.account_home_frame, text='ATM', command=self.atm_ui).grid(column=2, row=4, sticky=(W))
        ttk.Button(self.account_home_frame, text='Store', command=self.store_ui).grid(column=3, row=4, sticky=(W))
        ttk.Button(self.account_home_frame, text='ATM History', command=self.atm_history_ui).grid(column=4, row=4, sticky=(W))

        ttk.Button(self.account_home_frame, text='Logout').grid(column=2, row=6, sticky=(W))

    def store_ui(self):
        self.account_home_frame.destroy()
        
        self.store_frame = ttk.Frame(self.root, padding='3 3 12 12')
        self.store_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        item, price = self.store.display_item()

        ttk.Label(self.store_frame, text='Would you like to purchase {item} for ${price}'.format(item=item, price=price)).grid(column=1, row=1, sticky=(W))

        ttk.Button(self.store_frame, text='Yes', command=lambda: self.store.purchase(item, price)).grid(column=1, row=2, sticky=(W, E))
        ttk.Button(self.store_frame, text='No, next item', command = self.store_ui).grid(column=2, row=2, sticky=(W, E))

        self.return_home(self.store_frame).grid(column=1, row=3, sticky=(W, E))

    def return_home(self, frame):
        def destroy_current_frame():
            frame.destroy()
            self.account_home_ui()

        return ttk.Button(frame, text='Return Home', command=destroy_current_frame)

    def transactions_ui(self):
        self.account_home_frame.destroy()
        self.transactions_frame = ttk.Frame(self.root, padding='3 3 12 12')
        self.transactions_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.return_home(self.transactions_frame).grid(column=1, row=1, sticky=(W, E))
        
        row_num = 2
        for purchase in self.store.purchases.values():
            print(purchase)
            ttk.Label(self.transactions_frame, text=str(purchase)).grid(column=1, row=row_num, sticky=(W, E))
            row_num += 1

    def atm_ui(self):
        self.account_home_frame.destroy()
        atm_frame = ttk.Frame(self.root, padding='3 3 12 12')
        atm_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        amount = StringVar()
        amount_entry = ttk.Entry(atm_frame, width=10, textvariable=amount)
        amount_entry.grid(column=1, row=1, sticky=(W, E))

        ttk.Button(atm_frame, text='Deposit', command=lambda: self.balance.deposit(amount.get())).grid(column=1, row=2, sticky=(W, E))
        ttk.Button(atm_frame, text='Withdraw', command=lambda: self.balance.withdraw(amount.get())).grid(column=2, row=2, sticky=(W, E))

        self.return_home(atm_frame).grid(column=1, row=3, sticky=(W, E))

    def atm_history_ui(self):
        self.account_home_frame.destroy()
        atm_history_frame = ttk.Frame(self.root, padding='3 3 12 12')
        atm_history_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.return_home(atm_history_frame).grid(column=1, row=1, sticky=(W, E))

        row_num_start = 2
        for entry in self.balance.withdraw_deposit_userdict.values():
            print(entry)
            ttk.Label(atm_history_frame, text=str(entry)).grid(column=1, row=row_num_start, sticky=(W, E))
            row_num_start += 1



account = AccountHomeUI()


