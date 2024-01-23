import math

from ..cards.DamageInfo import DamageInfo
from ..powers.AbstractPower import AbstractPower
from ..monsters.AbstractMonster import AbstractMonster
from ..dungeons.AbstractDungeon import AbstractDungeon
from ..core.Settings import Settings


class AbstractCreature:
    name: str = None
    id: str = None
    powers: [AbstractPower] = []
    isPlayer: bool = None
    isBloodied: bool = None
    gold: int = None
    displayGold: int = None
    isDying: bool = False
    isDead: bool = False
    halfDead: bool = False
    isEscaping: bool = False
    currentHealth: int = None
    maxHealth: int = None
    currentBlock: int = None

    def __init__(self):
        pass

    def damage(self, var1: DamageInfo):
        raise NotImplementedError

    def brokeBlock(self):
        if isinstance(self, AbstractMonster):
            for r in AbstractDungeon.player.relics:
                r.onLoseBlock(self)

    def decrementBlock(self, info: DamageInfo, damageAmount: int):
        if info.type != DamageInfo.DamageType.HP_LOSS and self.currentBlock > 0:
            if damageAmount > self.currentBlock:
                damageAmount -= self.currentBlock
                self.currentBlock = 0
                self.brokeBlock()
            elif damageAmount == self.currentBlock:
                damageAmount = 0
                self.currentBlock = 0
                self.brokeBlock()
            else:
                self.currentBlock -= damageAmount
                if self.currentBlock < 0:
                    self.currentBlock = 0
                damageAmount = 0

        return damageAmount

    def increaseMaxHp(self, amount: int):
        if (not Settings.isEndless) or not AbstractDungeon.player.hasBlight("FullBelly"):
            if amount < 0:
                pass
            self.maxHealth += amount
            self.heal(amount)

    def getPower(self, targetID):
        for p in self.powers:
            if p.ID == targetID:
                return p
        return None

    def hasPower(self, targetID):
        for p in self.powers:
            if p.ID == targetID:
                return True
        return False

    def isDeadOrEscaped(self):
        pass

    def heal(self, healAmount: int):
        if Settings.isEndless and self.isPlayer and AbstractDungeon.player.hasBlight("FullBelly"):
            healAmount = math.trunc(healAmount / float(2))
            if healAmount < 1:
                healAmount = 1

        if not self.isDying:
            for r2 in AbstractDungeon.player.relics:
                if self.isPlayer:
                    healAmount = r2.onPlayerHeal(healAmount)

            for p in self.powers:
                healAmount = p.onHeal(healAmount)

            self.currentHealth += healAmount
            if self.currentHealth > self.maxHealth:
                self.currentHealth = self.maxHealth

            if (float(self.currentHealth) > float(self.maxHealth) / 2.0) and self.isBloodied:
                self.isBloodied = False

                for r2 in AbstractDungeon.player.relics:
                    r2.onBloodied()

    def decreaseMaxHealth(self, amount: int):
        self.maxHealth -= amount

        if self.maxHealth <= 1:
            self.maxHealth = 1

        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth


    def addBlock(self, blockAmount: int):
        if blockAmount > 0:
            self.currentBlock += blockAmount
            if self.currentBlock > self.maxHealth:
                self.currentBlock = self.maxHealth
