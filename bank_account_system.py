class BankAccount:
    def __init__(self, holder_name, balance):
        self.name = holder_name
        self.bal = balance
        
    def deposit(self, amount):
       self.bal += amount
        
    def withdraw(self, amount):
        if (amount <= self.bal):
            self.bal -= amount
        else:
            print("Insufficient Balance")
        
    def show_balance(self):
        print(f"\nHolder: {self.name}, Balance: {self.bal}")
    
    
accounts = [] 
print("\n-----Welcome to our Banking System-----")  
n= int(input("\nHow many Accounts to create? "))

for i in range(n):
    name = input("\nEnter Account holder name: ")
    balance = float(input("Initial Balance: "))
    
    acc = BankAccount(name, balance)
    accounts.append(acc)
print("---Transactions---")
    
for acc in accounts:
    print(f"\nTransaction for {acc.name}: ")
    deposit_amount = float(input("Deposit amount: "))
    acc.deposit(deposit_amount)
    withdraw = float(input("Withdraw amount: "))
    acc.withdraw(withdraw)
    acc.show_balance()

