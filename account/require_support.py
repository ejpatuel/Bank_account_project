import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING, format='[%(filename)s - %(funcName)s - %(levelname)s - %(lineno)s]\n - %(message)s\n')

class WithdrawlLimitBelowZero(Exception):
  def __init__(self, withdrawl_limit):
    logger.warning('WithdrawlLimitError exception raised with withdrawl_limit value of: {value}'.format(value=withdrawl_limit))
    self.withdrawl_limit = withdrawl_limit
      

class AccountOwnerEmpty(Exception):
  def __init__(self, new_owner, old_owner):
    self.new_owner = new_owner
    self.old_owner = old_owner
    logger.warning('AccountOwnerError exception raised with account_owner value of: {value}'.format(value=new_owner))

  def __str__(self):
    return 'Attempting to change account owner of {og_owner} to {new_owner}, but an issues was encountered'.format(og_owner=self.old_owner, new_owner=self.new_owner)

class WithdrawOrDepositError(Exception):
  def __init__(self, in_or_out, amount, location):
    pass
    self.in_or_out = in_or_out
    self.amount = amount
    self.location = location

  def __str__(self):
    return 'An error occured withing the WithdrawsAndDeposits userdict when attempting to log a {in_or_out} of ${amount}, at {location}'.format(in_or_out=self.in_or_out, amount=self.amount, location=self.location)


class AmountExceedsBalance(Exception):
  def __init__(self, amount, balance):
    self.amount = amount
    self.balance = balance

  def __str__(self):
    return 'You are attempting to withdraw an amount of ${amount}, with an insufficient balance of ${balanace}.'.format(amount=self.amount, balance=self.balance)


class UnknownRecognizedPaymentOrigin(Exception):
  def __init__(self):
    pass

    
