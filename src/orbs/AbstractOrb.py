# finished
from ..badlogic.math.MathUtils import MathUtils


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

    def onStartOfTurn(self):
        pass

    def onEndOfTurn(self):
        pass

    # 集中
    def applyFocus(self):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        power = AbstractDungeon.player.getPower("Focus")
        if power is not None and self.ID != "Plasma":
            self.passiveAmount = max(0, self.basePassiveAmount + power.amount)
            self.evokeAmount = max(0, self.baseEvokeAmount + power.amount)
        else:
            self.passiveAmount = self.basePassiveAmount
            self.evokeAmount = self.baseEvokeAmount

    # 瞄准靶心，追踪锁定效果
    def applyLockOn(target, dmg):
        ret_val = dmg
        if hasattr(target, "hasPower") and target.hasPower("Lockon"):
            ret_val = int(float(dmg) * 1.5)
        return ret_val

    def makeCopy(self):
        raise NotImplementedError

    def update(self):
        pass


def getRandomOrb(useCardRng):
    from ..dungeons.AbstractDungeon import AbstractDungeon
    from .Lightning import Lightning
    from .Dark import Dark
    from .Frost import Frost
    from .Plasma import Plasma
    orbs = [Dark(), Frost(), Lightning(), Plasma()]
    if useCardRng:
        return orbs[AbstractDungeon.cardRandomRng.random(len(orbs) - 1)]
    else:
        return orbs[MathUtils.randomInt(len(orbs) - 1)]
