class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f'Name :  {self.name} , Balance : {self.balance}'
    
    def __eq__(self,other):
        return self.balance== other.balance
    def __gt__(self,other):
        return self.balance>other.balance
    def __lt__(self,other):
        return self.balance<other.balance
    
    def __add__(self,other):
        return self.balance + other.balance
    
    def __sub__(self,other):
        return self.balance - other.balance
    
    
    
customer1=Customer('yousef', 20000)
customer2=Customer('hossam', 50000)

print(customer1 == customer2)    
print(customer1 > customer2)    
print(customer1 < customer2)    
print(customer1 + customer2)    
print(customer1 - customer2)    

    
    
