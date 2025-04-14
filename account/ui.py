class Ui:
  def __init__(self):
    self.account = BankAccountLogistics('John', 1000)
    self.withdraw_and_deposit = balance.WithdrawsAndDeposits()
    self.balance = balance.Balance(self.test_account.account_owner, self.test_account.daily_withdraw_limit, self.test_withdraw_and_deposit)

  