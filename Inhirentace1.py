class Vichle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def info(self):
        print(f'the model is {self.model}')
        print(f'the brand is {self.brand}')
class Car(Vichle):
    def __init__(self,brand,model,type):
        super().__init__(brand,model)
        self.type=type
    def info(self):
        super().__init__()
        print(f'the type is {self.type}')
yousef=Car('Tesla',2025,'Model X',)
yousef.info()
