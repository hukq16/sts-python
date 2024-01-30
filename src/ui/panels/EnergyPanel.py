class EnergyPanel:
    totalCount = 0

    @classmethod
    def setEnergy(cls, energy):
        cls.totalCount = energy

    @classmethod
    def addEnergy(cls, e: int):
        cls.totalCount += e

        if cls.totalCount > 999:
            cls.totalCount = 999

    @classmethod
    def useEnergy(cls, e: int):
        cls.totalCount -= e
        if cls.totalCount < 0:
            cls.totalCount = 0

    @classmethod
    def getCurrentEnergy(cls):
        from ...dungeons.AbstractDungeon import AbstractDungeon
        return 0 if AbstractDungeon.player is None else cls.totalCount
