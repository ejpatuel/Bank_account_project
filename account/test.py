import unittest, logging
from account import BankAccountLogistics
import require_support 
import balance 
from unittest.mock import patch
import atm_store
# import user_interaction 
# import curse_ui
# import curses

testing_logger = logging.getLogger(__name__)
testing_logger.setLevel(logging.INFO)
#^ set logging level for file
logging.basicConfig(level=logging.INFO, format='[%(filename)s - %(funcName)s - %(levelname)s - %(lineno)s]\n%(message)s \n ')

class TestAccountCreation(unittest.TestCase):

  def setUp(self):
    #^ runs before every test 
    self.test_account = BankAccountLogistics('John Doe', 1000, purpose='Emergency fund')
    #^ all these parameters are valid 
  

  @patch('builtins.input', side_effect=['John Doe', 7686, '7664'])
  def test_account_owner_setting(self, mock_input):
    #^ with the for side_effect and for loop runs 3 time with each input 
    # all tests should pass
    for i in range(3):
      user_input = str(input())
      self.test_account.account_owner = user_input
      assert self.test_account.account_owner == user_input
      #^ check to see if the input is allocated to the .account_owner correctly
      # potential for a AccountOwnerEmpty exception in real scenario
      
  #test the values that should raise errors
  @patch('builtins.input', side_effect=['    ', ''])
  def test_AccountOwnerError(self, mock_input):
    #^ testing for the AccountOwnerEmpty owner empty exception with should be raised by both empty strings
    for i in range(2):
      #^ i in 2 for the 2 values in side_effect
      with self.assertRaises(require_support.AccountOwnerEmpty):
        self.test_account.account_owner = input()

 
  @patch('builtins.input', side_effect=[-1, -2, -3, -5, -6])
  def test_WithdrawlLimitError(self, mock_input):
    #^ a user cannor input a negative number
    for i in range(5):
      with self.assertRaises(require_support.WithdrawlLimitBelowZero):
        self.test_account.daily_withdraw_limit = input()

class TestBalance(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    #^ sets up once before all tests to initialize classes
    self.test_account = BankAccountLogistics('John', 1000)
    self.test_withdraw_and_deposit = balance.WithdrawsAndDeposits()
    self.test_balance = balance.Balance(self.test_account.account_owner, self.test_account.daily_withdraw_limit, self.test_withdraw_and_deposit)
    

  @patch('builtins.input', side_effect = [15, 200, 650])
  def test_deposit(self, mock):
    for i in range(3):
      self.test_balance.deposit(input())
      #^ method to add the deposits to the balance
      print('Balance: '+ str(self.test_balance.balance))
    testing_logger.debug(self.test_balance.withdraw_deposit_userdict)
    
      
  @patch('builtins.input', side_effect = [10, 100, 50])
  def test_withdraw(self, mock):
    for i in range(3):
      withdraw_amount = input()
      self.test_balance.check_balance(self.test_balance.balance, withdraw_amount)
      #^ method to make sure withdraw doesnt excees balance
      # in the deposit test right before this one we ensure the balance is high enough to make all withdrawls in side_effect
      self.test_withdraw_and_deposit['withdraw'] = withdraw_amount
    testing_logger.debug(self.test_balance.withdraw_deposit_userdict)


class TestDepositWithdrawInteraction(unittest.TestCase):

  def reset_classes(self):
    self.test_account = BankAccountLogistics('John', 0)
    self.test_withdraw_and_deposit = balance.WithdrawsAndDeposits()
    self.test_balance = balance.Balance(self.test_account.account_owner, self.test_account.daily_withdraw_limit, self.test_withdraw_and_deposit)

  def test_balance_update(self):
    deposit_withdraw_balance = [[100, 40, 60], [1000, 20, 980], [50, 48, 2]]
    for values in deposit_withdraw_balance:
      self.reset_classes()
      with self.subTest(values):
        with patch('builtins.input', side_effect = values) as ptch:
          deposit = input()
          withdraw = input()
          self.test_balance.deposit(deposit)
          self.test_balance.withdraw(withdraw)
          testing_logger.debug('Deposit: {deposit}\nWithdraw: {withdraw}\nBalance: {balance}'.format(deposit=deposit, withdraw=withdraw, balance=self.test_balance.balance))
          self.assertEqual(self.test_balance.balance, input())

class TestBalanceExceptions(unittest.TestCase):
  #This test class and TestBalance are very similar but for clarity the test in this class has its own class otherwise I would have to add unnecessary confusing logic to adjust the balances to test for the withdra excpetion
  @classmethod
  def setUpClass(self):
    #^ exact same setup as TestBalance
    self.test_account = BankAccountLogistics('John', 1000)
    self.test_withdraw_and_deposit = balance.WithdrawsAndDeposits()
    self.test_balance = balance.Balance(self.test_account.account_owner, self.test_account.daily_withdraw_limit, self.test_withdraw_and_deposit)

  def test_WithdrawExceedsBalance(self):
      with self.assertRaises(require_support.AmountExceedsBalance):
        #^ testing for the exception above
        self.test_withdraw_and_deposit['deposit'] = 100
        withdraw_amount = 5000
        self.test_balance.check_balance(self.test_balance.balance, withdraw_amount)
        self.test_withdraw_and_deposit['withdraw'] = withdraw_amount


# class TestTransactionsAndShopping(unittest.TestCase):

#   @classmethod
#   def setUpClass(self):
#     self.store = atm_store.Store()

#   def test_store_and_transactions_dict(self):
#     for test in range(4):
#       item, price = self.store.purchase_and_display()
#       with self.subTest(price):
#         self.assertIn(price, self.store.purchases.values().Transaction.amount)



    



    

unittest.main()
    