# finished

from ..AbstractGameAction import AbstractGameAction


class DamageAction(AbstractGameAction):
    DURATION = 0.1
    POST_ATTACK_WAIT_DUR = 0.1

    def __init__(self, target, info, stealGoldAmount=None):
        super().__init__()
        self.goldAmount = 0
        self.skipWait = False
        self.muteSfx = False
        self.info = info
        self.setValues(target, info)
        self.actionType = AbstractGameAction.ActionType.DAMAGE
        self.duration = 0.1

        if stealGoldAmount is not None:
            self.goldAmount = stealGoldAmount

    def update(self):
        from ...dungeons.AbstractDungeon import AbstractDungeon
        from ...cards.DamageInfo import DamageInfo
        if self.shouldCancelAction() and self.info.type != DamageInfo.DamageType.THORNS:
            self.isDone = True
        else:
            if self.duration == 0.1:
                if self.info.type != DamageInfo.DamageType.THORNS and (
                        self.info.owner.isDying or self.info.owner.halfDead):
                    self.isDone = True
                    return
                if self.goldAmount != 0:
                    self.stealGold()

            self.tickDuration()
            if self.isDone:
                self.target.damage(self.info)
                if AbstractDungeon.getCurrRoom().monsters.areMonstersBasicallyDead():
                    AbstractDungeon.actionManager.clearPostCombatActions()

    def stealGold(self):
        if self.target.gold != 0:
            if self.target.gold < self.goldAmount:
                self.goldAmount = self.target.gold

            var10000 = self.target
            var10000.gold -= self.goldAmount
