from abc import ABC, abstractmethod


class Deposit(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass


class Withdraw(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass


class BalanceInfo(ABC):
    @abstractmethod
    def balance_info(self):
        pass


class Bank(Deposit, Withdraw, BalanceInfo):
    def __init__(self, acno, name, balance):
        self.name = name
        self.balance = balance
        self.acno = acno

    def deposit(self, amount):
        self.balance += amount
        print(f'MR: {self.name} : {amount}$ is added to your balance')

    def withdraw(self, amount):
        if amount > self.balance:
            print(
                f'MR: {self.name} : Your current balance is lower than {amount}')
        else:
            self.balance -= amount
            print(f'MR: {self.name} : Operation is successful')

    def balance_info(self):
        print(f'MR: {self.name} : Your current balance is {self.balance}')


class SavingsAccount(Bank):
    def __init__(self, acno, name, balance, interest_rate):
        super().__init__(acno, name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f'MR: {self.name} : Your interest is {interest}$')


class TransactionProcessor:
    def __init__(self, bank_account: Bank):
        self.bank_account = bank_account

    def process_deposit(self, amount):
        self.bank_account.deposit(amount)

    def process_withdrawal(self, amount):
        self.bank_account.withdraw(amount)

    def display_balance(self):
        self.bank_account.balance_info()


emp1 = Bank(305124005, 'Ahmed Amr', 4000)
emp2 = Bank(302211402, 'Osama Hassan', 5201)

emp1.deposit(2000)
print('='*40)
emp2.withdraw(6000)
print('='*40)
emp2.withdraw(400)
print('='*40)
emp2.balance_info()

print('='*40)


emp3 = SavingsAccount(305124006, 'Mona Ali', 10000, 5)
emp3.deposit(2000)
emp3.calculate_interest()
emp3.balance_info()
