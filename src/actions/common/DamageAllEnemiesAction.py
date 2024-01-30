# finished
from ..AbstractGameAction import AbstractGameAction

from ...cards.DamageInfo import DamageInfo


class DamageAllEnemiesAction(AbstractGameAction):

    def __init__(self, source, type, amount=None, baseDamage=None):
        super().__init__()
        self.baseDamage = 0
        self.firstFrame = True
        self.utilizeBaseDamage = False
        self.source = source
        self.actionType = AbstractGameAction.ActionType.DAMAGE
        self.damageType = type
        self.damage = []
        if amount is not None and baseDamage is None:
            self.damage = amount

        if amount is None and baseDamage is not None:
            self.baseDamage = baseDamage
            self.utilizeBaseDamage = True
            self.damage = []

    def update(self):
        from ...dungeons.AbstractDungeon import AbstractDungeon

        if self.firstFrame:
            if self.utilizeBaseDamage:
                self.damage = DamageInfo.createDamageMatrix(self.baseDamage)
            self.firstFrame = False

        self.tickDuration()

        if self.isDone:
            for p in AbstractDungeon.player.powers:
                p.onDamageAllEnemies(self.damage)

            for monster in AbstractDungeon.getCurrRoom().monsters.monsters:
                if not monster.isDeadOrEscaped():
                    monster.damage(DamageInfo(self.source, self.damage[monster.index], self.damageType))

            if AbstractDungeon.getCurrRoom().monsters.areMonstersBasicallyDead():
                AbstractDungeon.actionManager.clearPostCombatActions()
