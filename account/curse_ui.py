import curses
import time
from account import BankAccountLogistics
import require_support 
import balance 

class UserInteraction:
  def __init__(self):
    try:
      self.screen = curses.initscr()
      self.screen.clear()
      self.begin_x = 0; self.begin_y = 0
      self.height = curses.LINES - 1
      self.width = curses.COLS - 1
      self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
      self.win.keypad(True)
      self.win.box()

      self.account = self.get_user_banking_info(False)
      self.withdraw_and_deposit = balance.WithdrawsAndDeposits()
      self.balance = balance.Balance(self.account.account_owner, self.account.daily_withdraw_limit, self.withdraw_and_deposit)
    except require_support.AccountNotWanted as e:
      pass

    

  def get_user_banking_info(self, reentry):
    y_answers = {'yes', 'y', 'yse'}
    n_answers = {'no', 'n'}
    opening_question = 'Y'

    if reentry == False:
      self.win.addstr(1, 1, 'Welcome, I see you are new to our bank, would you like to create a bank account?\n [Y/N]: ')
      opening_question = self.win.getstr().decode(encoding='utf-8').lower()
      self.win.refresh()
      

    if opening_question in n_answers or opening_question not in y_answers:
      #^ the or sectuon needs to be givien its own if block as it is a different circumstance to saying no
      self.win.clear()
      self.win.addstr('Have a great day you are always welcome to open an account at a later date.')
      self.win.refresh()
      time.sleep(5)
      return
    
    if reentry == False:
      self.win.clear()
      self.win.addstr('Great! To set your account up im going to need your first, middle, and last name \nas well as your daily withdrawl limit for your account.\n')
      
    self.win.refresh()
    self.win.addstr('' \
    '\nFirst, middle, and last name: ')
    name = self.win.getstr().decode(encoding='utf-8')

    self.win.addstr('\nDaily withdrawl limit: ')
    daily_withdrawl_limit = float(self.win.getstr().decode(encoding='utf-8'))

    self.win.clear()
    self.win.addstr('Please confirm your details:\nFull name: {full_name}\nDaily withdrawl limit (can be changed later): {daily_withdrawl}\n[Y/N]: '.format(full_name=name, daily_withdrawl=daily_withdrawl_limit))
    user_confirmation = self.win.getstr().decode(encoding='utf-8')
    self.win.clear()

    if user_confirmation.lower() in y_answers:
      self.win.addstr('Thank you for creating an account!')
      return BankAccountLogistics(name, daily_withdrawl_limit)
    elif user_confirmation.lower() in n_answers:
      self.win.addstr('Update your information')
      self.get_user_banking_info(True)

  def account_homepage(self):
    
    self.win.refresh()
    current_cursor_location = {'y': 0, 'x': 2}
    logout_btn_location = (self.begin_y + 5, self.begin_x + 2)

    attributes = {'tranaction': curses.A_NORMAL, 'logout': curses.A_NORMAL}

    self.win.box()
    self.win.addstr(self.begin_y + 1, self.begin_x + 1, 'Balance: {balance}'.format(balance=self.balance.balance))
    self.win.addstr(self.begin_y + 3, self.begin_x + 2, 'Transactions')
    self.win.addstr(logout_btn_location[0], logout_btn_location[1], 'Logout')
    self.win.move(1, 1)

    while self.win.getyx != logout_btn_location:
  
      get_input = self.win.getch()
      print('here '+ str(get_input))

      cursor_y, cursor_x = self.win.getyx()

      if self.height >= cursor_y >= self.begin_y and self.width >= cursor_x >= self.begin_x:
        if get_input == curses.KEY_DOWN:
          current_cursor_location['y'] += 1
          print('down')
          self.win.move(current_cursor_location['y'], current_cursor_location['x'])
          self.win.refresh()
        elif get_input == curses.KEY_UP:
          current_cursor_location['y'] -= 1
          self.win.move(current_cursor_location['y'], current_cursor_location['x'])
          self.win.refresh()

  # def test_wrapper(self):
  #   self.win.addstr('Hello')

  # def underline_selection(addstr):
  #   def wrapper(*args, **kwargs):
  #     addstr(*args, *kwargs, curses.A_UNDELINE)
  #   return wrapper



      


    

ui = UserInteraction()

ui.account_homepage()




