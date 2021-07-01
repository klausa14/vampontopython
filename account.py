import datetime
import pytz


class Account:
    """Simple account class with Balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for "+ self.name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append(Account._current_time(), amount)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append(Account._current_time(),-amount)
        else:
            print("amount must be greater than zero and not more than acount balance")
            self.show_balance()

    def show_balance(self):
        print("balance is {} ".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'Deposited'
            else:
                tran_type = "Withdraw"
                amount *= -1
                print("{:6} {} on {} (local time {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim  = Account("Tim",0)
    tim.show_balance()
    tim.deposit(1000)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()
    tim.withdraw(2000)
    tim.show_transactions()

    steph = Account("steph", 0)
    steph.show_balance()
    steph.deposit(1000)
    steph.withdraw(2000)
    steph.