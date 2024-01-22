
from ..AbstractGameAction import AbstractGameAction
from ...dungeons.AbstractDungeon import AbstractDungeon
from ...cards.DamageInfo import DamageInfo
from ...core.Settings import Settings
class DamageAllEnemiesAction(AbstractGameAction):


    def __init__(self, source, type, amount = None, baseDamage = None):
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
        i = 0
        if self.firstFrame:

            i = len(AbstractDungeon.getCurrRoom().monsters.monsters)
            if self.utilizeBaseDamage:
                self.damage = DamageInfo.createDamageMatrix(self.baseDamage)
            self.firstFrame = False

        self.tickDuration()
        if self.isDone:
            var4 = AbstractDungeon.player.powers.iterator()

            while var4.hasNext():
                p = var4.next()
                p.onDamageAllEnemies(self.damage)

            temp = len(AbstractDungeon.getCurrRoom().monsters.monsters)

            for i in range(0, temp):
                (AbstractDungeon.getCurrRoom().monsters.monsters[i]).damage(DamageInfo(self.source, self.damage[i], self.damageType))

            if AbstractDungeon.getCurrRoom().monsters.areMonstersBasicallyDead():
                AbstractDungeon.actionManager.clearPostCombatActions()

