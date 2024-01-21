from .AbstractOrb import AbstractOrb

class Plasma(AbstractOrb):
    def __init__(self):
        super().__init__()
        self.name = 'Plasma'
