from .AbstractOrb import AbstractOrb

class Frost(AbstractOrb):
    def __init__(self):
        super().__init__()
        self.name = "Frost"
        self.desc = ""