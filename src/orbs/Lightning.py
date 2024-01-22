# 导入必要的模块
# 根据实际情况，你可能需要创建或导入以下模块的Python版本
import math
import random
from .AbstractOrb import AbstractOrb
from ..dungeons.AbstractDungeon import AbstractDungeon
from ..cards.DamageInfo import DamageInfo
from ..actions.defect.LightningOrbEvokeAction import LightningOrbEvokeAction


class Lightning(AbstractOrb):
    ORB_ID = "Lightning"

    def __init__(self):
        super().__init__()
        self.ID = "Lightning"
        self.baseEvokeAmount = 8
        self.evokeAmount = self.baseEvokeAmount
        self.basePassiveAmount = 3
        self.passiveAmount = self.basePassiveAmount

    def onEvoke(self):
        # 实现激发效果
        if AbstractDungeon.player.hasPower("Electro"):
            AbstractDungeon.actionManager.addToTop(
                LightningOrbEvokeAction(
                    DamageInfo(AbstractDungeon.player, self.evokeAmount, DamageInfo.DamageType.THORNS),
                    True))
        else:
            AbstractDungeon.actionManager.addToTop(
                LightningOrbEvokeAction(
                    DamageInfo(AbstractDungeon.player,
                               self.evokeAmount,
                               DamageInfo.DamageType.THORNS),
                    False))
        pass

    def onEndOfTurn(self):
        # 回合结束时的行为
        pass

    def triggerPassiveEffect(self, info, hitAll):
        # 触发被动效果
        pass

    def makeCopy(self):
        return Lightning()
