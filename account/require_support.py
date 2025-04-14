import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING, format='[%(filename)s - %(funcName)s - %(levelname)s - %(lineno)s]\n - %(message)s\n')

class WithdrawlLimitBelowZero(Exception):
  def __init__(self, withdrawl_limit):
    logger.warning('WithdrawlLimitError exception raised with withdrawl_limit value of: {value}'.format(value=withdrawl_limit))
    self.withdrawl_limit = withdrawl_limit
      

class AccountOwnerEmpty(Exception):
  def __init__(self, account_owner):
    self.account_owner = account_owner
    logger.warning('AccountOwnerError exception raised with account_owner value of: {value}'.format(value=account_owner))

class WithdrawOrDepositError(Exception):
  def __init__(self, in_or_out, amount, location):
    pass
    self.in_or_out = in_or_out
    self.amount = amount
    self.location = location

  def track_issue(self):
    if self.in_or_out != 'deposit' and self.in_or_out != 'withdraw':
      raise DepositOrWithDrawError(self.in_or_out)
    # elif self.amount

class DepositLocationError(Exception):
  def __init__(self):
    pass

class WithdrawExceedsBalance(Exception):
  def __init__(self):
    pass

class AccountNotWanted(Exception):
 def __init__(self):
    pass


    
