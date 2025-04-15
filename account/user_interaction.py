import logging
from account import BankAccountLogistics
import require_support 
import balance 

class UserInteraction:
  def __init__(self):
    try:
      self.account = self.get_user_banking_info(False)
      self.withdraw_and_deposit = balance.WithdrawsAndDeposits()
      self.balance = balance.Balance(self.account.account_owner, self.account.daily_withdraw_limit, self.withdraw_and_deposit)
    except require_support.AccountNotWanted as e:
      pass

  
  def get_user_banking_info(self, reentry):
    no_account_wanted = 'Thank you for your time, feel free to come back and open an account at anytime!'
    opening_question = 'Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: '
    y_answers = ['yes', 'y', 'yse']
    n_answers = ['no', 'n']

    if reentry == False:
      opening_question = input('Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: ')
      
    if opening_question.lower() in n_answers:
      raise AccountNotWanted
      print(no_account_wanted)
      return

    if reentry == False:
      print('Great! To set your account up im going to need your first, middle, and last name as well as your daily withdrawl limit for your account.')

    name = input('\nFull name: ')
    daily_withdraw_limit = float(input('Daily withdrawl limit: '))
    user_confirmation = input('Please confirm your details:\nFull name: {full_name}\nDaily withdrawl limit (can be changed later): {daily_withdrawl}\n[Y/N]: '.format(full_name=name, daily_withdrawl=daily_withdraw_limit))


    if user_confirmation.lower() in y_answers:
      print('Thank you for creating an account!')
      return BankAccountLogistics(name, daily_withdraw_limit)
    elif user_confirmation.lower() in n_answers:
      print('Update your information')
      self.get_user_banking_info(True)

  # else:
  #   pass
  #   'raise some sort of approaprite error' 

# user = UserInteraction()
