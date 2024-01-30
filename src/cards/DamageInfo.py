# finished
from enum import Enum

from ..core.Settings import Settings
from ..core.AbstractCreature import AbstractCreature
import math


class DamageInfo:
    class DamageType(Enum):
        NORMAL = 0
        THORNS = 1
        HP_LOSS = 2

    def __init__(self, damageSource: AbstractCreature, base: int, type: DamageType = None):

        self.name = None
        self.isModified = False
        self.owner = damageSource

        self.base = base
        self.output = base

        if type is not None:
            self.type = type
        else:
            self.type = self.DamageType.NORMAL

    def applyPowers(self, owner: AbstractCreature, target: AbstractCreature):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        self.output = self.base
        self.isModified = False
        tmp = float(self.output)

        if not owner.isPlayer:
            if Settings.isEndless and AbstractDungeon.player.hasBlight("DeadlyEnemies"):
                mod = AbstractDungeon.player.getBlight("DeadlyEnemies").effectFloat()
                tmp *= mod
                if self.base != int(tmp):
                    self.isModified = True

            for p in owner.powers:
                tmp = p.atDamageGive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            for p in target.powers:
                tmp = p.atDamageReceive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            tmp = AbstractDungeon.player.stance.atDamageReceive(tmp, self.type)

            if self.base != int(tmp):
                self.isModified = True

            for p in owner.powers:
                tmp = p.atDamageFinalGive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            for p in target.powers:
                tmp = p.atDamageFinalReceive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            self.output = math.floor(tmp)
            if self.output < 0:
                self.output = 0
        else:
            for p in owner.powers:
                tmp = p.atDamageGive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            tmp = AbstractDungeon.player.stance.atDamageGive(tmp, self.type)

            if self.base != int(tmp):
                self.isModified = True

            for p in target.powers:
                tmp = p.atDamageReceive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            for p in owner.powers:
                tmp = p.atDamageFinalGive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            for p in target.powers:
                tmp = p.atDamageFinalReceive(tmp, self.type)
                if self.base != int(tmp):
                    self.isModified = True

            self.output = math.floor(tmp)
            if self.output < 0:
                self.output = 0

    @classmethod
    def createDamageMatrix(cls, baseDamage: int, isPureDamage: bool = False, isOrbDamage: bool = None):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        retVal = [0 for _ in range(len(AbstractDungeon.getMonsters().monsters))]
        if isOrbDamage is not None:
            i = 0
            while i < len(retVal):
                info = DamageInfo(AbstractDungeon.player, baseDamage)
                if isOrbDamage and (AbstractDungeon.getMonsters().monsters[i]).hasPower("Lockon"):
                    info.output = int((float(info.base) * 1.5))

                retVal[i] = info.output
                i += 1
        else:
            i = 0
            while i < len(retVal):
                info = DamageInfo(AbstractDungeon.player, baseDamage)
                if not isPureDamage:
                    info.applyPowers(AbstractDungeon.player,
                                     AbstractDungeon.getMonsters().monsters[i])

                retVal[i] = info.output
                i += 1
        return retVal
