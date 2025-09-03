class Account:
     
     def __init__(self, bal, acc ):
          self.balance = bal
          self.account_no = acc 
      
   # debit method   
     def debit(self, amount):
        self.balance -= amount
        print("RS", amount, "was debited.")
        print("Total balance = ", self.get_balance())
      
      # credit method 
     def credit(self, amount):
        self.balance += amount
        print("RS", amount, "was credit.")
        print("Total balance = ", self.get_balance())
        
     def get_balance(self):
         return self.balance
    
    
acc1 = Account(150000, 1068231)
acc1.debit(45000)
acc1.credit(55000)
acc1.credit(85000)

