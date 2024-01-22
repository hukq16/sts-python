from enum import Enum



class DamageInfo:

    class DamageType(Enum):
        NORMAL = 0
        THORNS = 1
        HP_LOSS = 2


    def __init__(self, damageSource, base, type = None):

        self.name = None
        self.isModified = False
        self.owner = damageSource

        self.base = base
        self.output = base

        if type != None:
            self.type = type
        else:
            self.type = self.DamageType.NORMAL



