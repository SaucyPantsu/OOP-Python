class Account:

    _ANNUAL_RATE = 3.5

    def __init__(self, holder, balance):
        self._balance = balance
        self._holder = holder
        print(self._holder, " Balance:", self._balance)

    def acc_holder(self):
        return self._holder

    def balance(self):
        return self._balance

    def deposit(self, amount):
        while amount < 0:
            print("negative value, please try again")
            amount = int(input("how much do you want to deposit? "))
        print("You are depositing :", amount)
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, amount):
        while amount > self._balance:
            print("insufficient funds, try again")
            amount = int(input("how much do you want to withdraw? "))
        print("You are withdrawing :", amount)
        self._balance = self._balance - amount
        return self._balance

    @staticmethod
    def simple_interest(years, self):
        final = ((years * self._balance * Account._ANNUAL_RATE)/100)+self._balance
        print("Your balance in ", years, "will be ", final)


class CurrentAccount(Account):
    __WITHDRAWAL_FEE = 15

    def withdraw(self, amount):
        while (amount+self.__WITHDRAWAL_FEE) > self._balance:
            print("insufficient funds, try again")
            amount = int(input("how much do you want to withdraw? "))
        print("You are withdrawing :", amount, "15 withdrawal fee applies")
        self._balance = self._balance - (amount+self.__WITHDRAWAL_FEE)
        return self._balance


bianca_acc = CurrentAccount("bianca", 0)
print(bianca_acc.deposit(int(input("How much do you want to deposit? "))))
print(bianca_acc.withdraw(int(input("How much do you wish to withdraw? "))))
print(bianca_acc.acc_holder())
print(bianca_acc.balance())
bianca_acc.simple_interest(2, bianca_acc)