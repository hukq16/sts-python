from ...dungeons.AbstractDungeon import AbstractDungeon


class EnergyPanel:
    totalCount = 0

    def setEnergy(self, energy):
        self.totalCount = energy

    def addEnergy(self, e: int):
        self.totalCount += e

        if self.totalCount > 999:
            self.totalCount = 999

    def useEnergy(self, e: int):
        self.totalCount -= e
        if self.totalCount < 0:
            self.totalCount = 0

    def getCurrentEnergy(self):
        return 0 if AbstractDungeon.player is None else self.totalCount
