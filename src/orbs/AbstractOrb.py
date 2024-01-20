# 导入所需库
import math



from .Lightning import Lightning





class AbstractOrb:

    def __init__(self):
        self.name = ""
        self.ID = ""
        self.evokeAmount = 0
        self.passiveAmount = 0
        self.baseEvokeAmount = 0
        self.basePassiveAmount = 0




    def onEvoke(self):
        raise NotImplementedError

    @staticmethod
    def getRandomOrb(useCardRng):
        orbs = [Dark(), Frost(), Lightning(), Plasma()]
        if useCardRng:
            return orbs[AbstractDungeon.cardRandomRng.random(len(orbs) - 1)]
        else:
            return orbs[math.random(len(orbs) - 1)]

    def onStartOfTurn(self):
        pass

    def onEndOfTurn(self):
        pass

    # 集中
    def applyFocus(self):
        power = AbstractDungeon.player.getPower("Focus")
        if power is not None and self.ID != "Plasma":
            self.passiveAmount = max(0, self.basePassiveAmount + power.amount)
            self.evokeAmount = max(0, self.baseEvokeAmount + power.amount)
        else:
            self.passiveAmount = self.basePassiveAmount
            self.evokeAmount = self.baseEvokeAmount

    # 瞄准靶心，追踪锁定效果
    def applyLockOn(target, dmg):
        retVal = dmg
        if hasattr(target, "hasPower") and target.hasPower("Lockon"):
            retVal = int(dmg * 1.5)
        return retVal

    def makeCopy(self):
        raise NotImplementedError

    def update(self):
        pass




