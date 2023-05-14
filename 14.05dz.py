#4
class Bank:
    def __init__(self, customer, blnce):
        self.customer = customer
        self.blnce = blnce
class BankAccount:
    def __init__(self, customers, balance):
        self.customers = customers
        self.balance = balance
    def get_total_balance(self, blnce, balance):
        x =  blnce + balance
        return x

name = Bank("Настя", 800)
name1 = Bank("Ната", 700)
name2 = Bank("Ростік", 100)

print(f"Клієнт: {name.customer}, Баланс {name.blnce} грн")
print(f"Клієнт: {name1.customer}, Баланс {name1.blnce} грн")
print(f"Клієнт: {name2.customer}, Баланс {name2.blnce} грн")

name_res = BankAccount("Назар", 300)
print(f"Новий клієнт: {name_res.customers}, Баланс {name_res.balance} грн")

print(f"Загальний баланс усіх клієнтів становить: {name_res.get_total_balance(blnce = 1600, balance = 300)} грн")
