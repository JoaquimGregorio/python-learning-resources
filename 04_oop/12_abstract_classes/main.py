"""
OOP - Abstract Classes
"""
from classes.savings_account import SavingsAccount
from classes.checking_account import CheckingAccount

acc1 = SavingsAccount(1111, 3333, 0)
acc1.deposit(1000)
acc1.withdraw(300)

print("#################################")

acc2 = CheckingAccount(agency=1234, number=1978, balance=0, limit=500)
acc2.deposit(100)
acc2.withdraw(500)
acc2.withdraw(500)
