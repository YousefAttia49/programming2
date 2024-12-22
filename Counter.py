class Counter:
    def __init__(self):
        self.count=0
    def __call__(self):
        self.count+=1
    def __str__(self):
        return f' the count of operation is {self.count}'
counter=Counter()
counter()  
counter()  
counter()  
print(counter)    