class AbstractPotion:
    def __init__(self):
        self.name = "Abstract Potion"
        self.description = "This is an abstract potion description."
        self.potency = 0
        self.price = 0

    def __str__(self):
        return self.name

    def getPotency(self):
        return self.potency

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def use(self, character):
        pass