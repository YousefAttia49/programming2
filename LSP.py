from abc import ABC, abstractmethod

class Flying(ABC):
    @abstractmethod
    def fly(self):
        pass


class NonFlying(ABC):
    @abstractmethod
    def walk(self):
        pass


class Papagi(Flying):
    def fly(self):
        return ' i can fly '


class Ostrich(NonFlying):
    def walk(self):
        return 'I can run fast'

print(Ostrich().walk())
print(Papagi().run())
