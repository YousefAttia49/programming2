class Animal:
    def speak(self):
        pass

    def __str__(self):
        return 'animals'


class Dog(Animal):
    def speak(self):
        return 'Weof'

    def __str__(self):
        return 'Dog'


class Cat(Animal):
    def speak(self):
        return 'Meow'

    def __str__(self):
        return 'Cat'


class Bird(Animal):
    def speak(self):
        return 'Souw'

    def __str__(self):
        return 'Bird'


def display(animals):
    for animal in animals:
        print(f' the sound of {animal} is :{animal.speak()}')


animals = [Dog(), Cat(), Bird()]
display(animals)
