from collections import UserDict, namedtuple, ChainMap
import datetime, logging
import require_support
from account import BankAccountLogistics
import random

class Balance():
  def __init__(self, account_owner, daily_withdraw_limit, withdraw_deposit_userdict):
    self.balance = 0
    # sets balance for every instance of balance (usually one per account or potentially an account can have things like: checkings and saving, with different balances)
    self.daily_withdraw_limit = daily_withdraw_limit
    self.withdraw_deposit_userdict = withdraw_deposit_userdict

  def deposit(self, amount):
    #^ methode stores activity in withdraw_deposit_userdict and adjusts the balance here
    self.withdraw_deposit_userdict['deposit'] = amount
    self.balance += amount

  def check_balance(self, balance, amount):
    #^ called before making a withdraw to make sure it wont exceed the balance
      if amount > balance:
        raise require_support.WithdrawExceedsBalance()
  

class WithdrawsAndDeposits(UserDict):
  
  def __init__(self):
    self.data = {}
    self.id = 0
    #^ every withdraw or deposit will increment the id

    self.in_out_logger = logging.getLogger(__name__)
    self.in_out_logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format='[%(filename)s - %(funcName)s - %(levelname)s - %(lineno)s] \n%(message)s \n')

  def __setitem__(self, in_or_out, amount):
    #^ overriding method
    current_time = datetime.datetime.now().strftime('%A, %B %d, %Y')
    cash_or_online = ['cash', 'online']
    location = self.get_activity_location(cash_or_online[random.randint(0, 1)])
    #^ would not be random in real life but as its a simulation im making it random 
    Info = namedtuple('Info', ['in_or_out', 'amount', 'location', 'current_time'])
    #^ to hold withdraw or deposit info
    
    if in_or_out == 'deposit':
      self.data['deposit_{id}'.format(id=self.id)] = Info(in_or_out, amount, location, current_time)
      #^ key, value override format

      self.in_out_logger.info('Deposit_id: {id} \nInfo namedtuple contents:\n- In or out: {in_or_out} \n- Amount: ${amount} \n- Location: {location} \n- Time: {time}'.format(id=self.id, in_or_out=in_or_out, amount=amount, location=location, time=current_time))

      self.id += 1
      #^ increment id to ensure each withdraw and deposit has a unique id

    elif in_or_out == 'withdraw':
      self.data['withdraw_{id}'.format(id=self.id)] = Info(in_or_out, -1*amount, location, current_time)
      #^ same concept as deposit 

      self.in_out_logger.info('Withdraw_id: {id} \nInfo namedtuple contents:\n- In or out: {in_or_out} \n- Amount: ${amount} \n- Location: {location} \n- Time: {time}\n'.format(id=self.id, in_or_out=in_or_out, amount=-1*amount, location=location, time=current_time))

      self.id += 1
      #^ same concept as deposit 
      
    else:
      raise require_support.WithdrawOrDepositError(in_or_out, amount, location)
      

  def get_activity_location(self, cash_or_online):
      if cash_or_online == 'cash':
        # in a real sitaution would not be random 
        atm_locations = ['255 Johnson Road', 'Mayfair Mall', '280 Quadra Street', 'CIBC HQ']
        return atm_locations[random.randint(0, 3)]
      elif cash_or_online == 'online':
        #emualtes some sort of general location getter
        get_general_location = ['Canada, BC', 'South Africa, Johannesburd', 'Canada, Alberta', 'Italy']
        return get_general_location[random.randint(0, 3)]
      else:
        raise require_support.DepositLocationError()

   
      

 
