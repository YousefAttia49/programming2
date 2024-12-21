
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Drive')
       

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('Sail')


class Plane:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print('fly')


car1 = Car('BMW', 'M_Serious')
boat1 = Boat('Mercides', 'M5')
plan1 = Plane('EgyptionAir', 'AirBus')

for i in car1, boat1, plan1:
    print(i.move())
