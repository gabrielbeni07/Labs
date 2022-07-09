# Decorator/alldecorators/pizza.py
# Pizza example using decorators
class EatComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Plate(EatComponent):
    cost = 0.0


class Decorator(EatComponent):
    def __init__(self, eatComponent):
        self.component = eatComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + EatComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + EatComponent.getDescription(self)


class Calabresa(Decorator):
    cost = 54

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


class Portuguesa(Decorator):
    cost = 58

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


class Frango(Decorator):
    cost = 62

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


class Brasileira(Decorator):
    cost = 60

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


class Paulista(Decorator):
    cost = 61

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


class Chocolate(Decorator):
    cost = 40

    def __init__(self, eatComponent):
        Decorator.__init__(self, eatComponent)


pizza1 = Frango(Plate())
print(pizza1.getDescription() + ": R$" + str(pizza1.getTotalCost()))

pizza2 = Chocolate(Plate())
print(pizza2.getDescription() + ": R$" + str(pizza2.getTotalCost()))
