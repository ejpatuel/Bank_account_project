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
    amount = float(amount)
    self.withdraw_deposit_userdict['deposit'] = amount
    self.balance += amount

  def withdraw(self, amount):
    try:
      amount = float(amount)
      self.check_balance(self.balance, amount)
      self.withdraw_deposit_userdict['withdraw'] = amount
      self.balance -= amount
    except require_support.AmountExceedsBalance as e:
      print(e)



  def check_balance(self, balance, amount):
    #^ called before making a withdraw or transaction to make sure it wont exceed the balance
      if amount > balance:
        raise require_support.AmountExceedsBalance()
  

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


class Transactions(UserDict):
#^ A userdict to hold a history of the users transactions. 

  def __init__(self):
    self.data = {}
    self.id = 0

    self.transaction_logger = logging.getLogger(__name__)
    self.transaction_logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format='[%(filename)s - %(funcName)s - %(levelname)s - %(lineno)s] \n%(message)s \n')

  def __setitem__(self, payment_type, amount):
    current_time = datetime.datetime.now().strftime('%A, %B %d, %Y')
    origin = self.get_transaction_origin(payment_type)
    Transaction = namedtuple('Transaction', ['payment_type', 'amount', 'origin', 'current_time'])
    #^ to store the transaction detials 

    self.data[self.id] = Transaction(payment_type, -1*amount, origin, current_time)
    #^ adds entry to dict
    self.transaction_logger.info('Transaction: {id} \nInfo namedtuple contents:\n- Payment type: {payment_type} \n- Amount: ${amount} \n- Origin: {origin} \n- Time: {time}'.format(id=str(self.id), payment_type=payment_type, amount=str(amount), origin=origin, time=current_time))
    self.id += 1


  def get_transaction_origin(self, payment_type):
    #^ helper method to generate a random location to assign to a purchase (would be a real loation but this is just a simulation)
    origions = ['Save on Foods', 'Costco', 'Best Buy', 'Lululemon', 'Sketchy store', 'Sketchy website']
    if payment_type in {'online', 'electronic_wallet', 'physical_card'}:
      return origions[random.randint(0, 3)]
    else:
      raise require_support.UnknownRecognizedPaymentOrigin
     
    
   
      

 
