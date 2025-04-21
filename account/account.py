import require_support, logging

class BankAccountLogistics:

  #initialize with name, balance set to 0 for all classes
  def __init__(self, account_owner, daily_withdraw_limit, purpose='General'):
    #user may name an account by ID number so casting to string
    self.__account_owner = str(account_owner)
    self.__daily_withdraw_limit = daily_withdraw_limit
    self.purpose = str(purpose)

    self.setter_logger = logging.getLogger(__name__)
    self.setter_logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.INFO, format='[%(filename)s - %(funcName)s.setter - %(levelname)s - %(lineno)s] \n%(message)s \n')


   #print user account info 
  def __repr__(self):
    return '''
    Account owner: {owner}\n
    Account type: {purpose}\n
    Daily withdraw limit: {daily_withdraw_limit:.2f}
    '''.format(owner=self.account_owner, daily_withdraw_limit=self.daily_withdraw_limit)

  #--- Getters & Setters ---#
  @property
  def account_owner(self):
    return self.__account_owner
  @account_owner.setter
  def account_owner(self, account_owner):
    account_owner = str(account_owner)


    self.setter_logger.info('self.__account_owner attempting to be set to: {owner}'.format(owner=account_owner))
    self.__account_owner = str(account_owner).strip()
    if self.account_owner == '':
      raise require_support.AccountOwnerEmpty(account_owner, self.account_owner)
    else: pass

  #the daily withdrawel limit must be above zero. If it is not we raise a cutom exception
  @property
  def daily_withdraw_limit(self):
    return self.__daily_withdraw_limit

  @daily_withdraw_limit.setter
  def daily_withdraw_limit(self, limit):
    self.setter_logger.info('self.__daily_withdraw_limit attempting to be set to: {limit}'.format(limit=str(limit)))
    self.__daily_withdraw_limit = float(limit)
    if self.daily_withdraw_limit < 0: 
      raise require_support.WithdrawlLimitBelowZero(limit)
    else: pass
  
# --- --- #
    
        
    

# account = BankAccount('Jogn', 0)
# account.account_owner = 'Halley'
# account.daily_withdraw_limit = -1
# print(account.account_owner)

