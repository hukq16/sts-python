from ..AbstractGameAction import AbstractGameAction
from ...dungeons.AbstractDungeon import AbstractDungeon
from ...orbs.AbstractOrb import AbstractOrb
from ...cards.DamageInfo import DamageInfo
from ...actions.common.DamageAllEnemiesAction import DamageAllEnemiesAction
from ...actions.common.DamageAction import DamageAction


class LightningOrbEvokeAction(AbstractGameAction):

    def __init__(self, info: DamageInfo, hitAll: bool):
        super().__init__()
        self.info = info
        self.actionType = AbstractGameAction.ActionType.DAMAGE
        self.hitAll = hitAll

    def update(self):
        if not self.hitAll:
            m = AbstractDungeon.getRandomMonster()
            if m is not None:
                self.info.output = AbstractOrb.applyLockOn(m, self.info.base)
                self.addToTop(DamageAction(m, self.info))
        else:
            self.addToTop(DamageAllEnemiesAction(source=AbstractDungeon.player,
                                                 amount=DamageInfo.createDamageMatrix(self.info.base, True, True),
                                                 type=DamageInfo.DamageType.THORNS))

        self.isDone = True
