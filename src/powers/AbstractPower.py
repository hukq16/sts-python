# finished
from enum import Enum
from ..core.AbstractCreature import AbstractCreature
from ..dungeons.AbstractDungeon import AbstractDungeon
from ..actions.AbstractGameAction import AbstractGameAction
from ..cards.DamageInfo import DamageInfo
from ..cards.AbstractCard import AbstractCard
import math


class PowerType(Enum):
    BUFF = 0
    DEBUFF = 1


class AbstractPower:
    owner: AbstractCreature = None
    name: str = None
    description: str = None
    ID: str = None
    amount: int = -1
    priority: int = 5
    type: PowerType = None
    isTurnBased: bool = None
    isPostActionPower: bool = None
    canGoNegative: bool = None
    DESCRIPTIONS: [str] = None

    def __init__(self):
        self.type = PowerType.BUFF
        self.isTurnBased = False
        self.isPostActionPower = False
        self.canGoNegative = False

    def __str__(self):
        return "[" + self.name + "]:" + self.description

    def toString(self):
        return "[" + self.name + "]:" + self.description

    def updateParticles(self):
        pass

    def addToBot(self, action: AbstractGameAction):
        AbstractDungeon.actionManager.addToBottom(action)

    def addToTop(self, action: AbstractGameAction):
        AbstractDungeon.actionManager.addToTop(action)

    def updateDescription(self):
        pass

    def stackPower(self, stackAmount: int):
        if self.amount != -1:
            self.amount += stackAmount

    def reducePower(self, reduceAmount: int):
        if self.amount - reduceAmount <= 0:
            self.amount = 0
        else:
            self.amount -= reduceAmount

    def atDamageGive(self, damage: float, type: DamageInfo.DamageType, card: AbstractCard = None):
        return damage

    def atDamageFinalGive(self, damage: float, type: DamageInfo.DamageType, card: AbstractCard = None):
        return damage

    def atDamageFinalReceive(self, damage: float, type: DamageInfo.DamageType, card: AbstractCard = None):
        return damage

    def atDamageReceive(self, damage: float, damageType: DamageInfo.DamageType):
        return damage

    def atStartOfTurn(self):
        pass

    def duringTurn(self):
        pass

    def atStartOfTurnPostDraw(self):
        pass

    def atEndOfTurn(self, isPlayer: bool):
        pass

    def atEndOfTurnPreEndTurnCards(self, isPlayer: bool):
        pass

    def atEndOfRound(self):
        pass

    def onScry(self):
        pass

    def onDamageAllEnemies(self, damage):
        pass

    def onHeal(self, healAmount):
        return healAmount

    def onAttacked(self, info: DamageInfo, damageAmount: int):
        return damageAmount

    def onAttack(self, info, damageAmount: DamageInfo, target: int):
        pass

    def onAttackedToChangeDamage(self, info: DamageInfo, damageAmount: int):
        return damageAmount

    def onAttackToChangeDamage(self, info: DamageInfo, damageAmount: int):
        return damageAmount

    def onInflictDamage(self, info: DamageInfo, damageAmount: int, target: AbstractCreature):
        pass

    def onEvokeOrb(self, orb):
        pass

    def onCardDraw(self, card):
        pass

    def onPlayCard(self, card, m):
        pass

    def onUseCard(self, card, action):
        pass

    def onAfterUseCard(self, card, action):
        pass

    def wasHPLost(self, info, damageAmount):
        pass

    def onSpecificTrigger(self):
        pass

    def triggerMarks(self, card):
        pass

    def onDeath(self):
        pass

    def onChannel(self, orb):
        pass

    def atEnergyGain(self):
        pass

    def onExhaust(self, card):
        pass

    def onChangeStance(self, oldStance, newStance):
        pass

    def modifyBlock(self, blockAmount, card):
        return blockAmount

    def modifyBlockLast(self, blockAmount):
        return blockAmount

    def onGainedBlock(self, blockAmount):
        pass

    def onPlayerGainedBlock(self, blockAmount):
        return math.floor(blockAmount)

    def onGainCharge(self, chargeAmount):
        pass

    def onRemove(self):
        pass

    def onEnergyRecharge(self):
        pass

    def onDrawOrDiscard(self):
        pass

    def onAfterCardPlayed(self, usedCard):
        pass

    def onInitialApplication(self):
        pass

    def compareTo(self, other):
        return self.priority - other.priority

    def onApplyPower(self, power, target, source):
        pass

    def getLocStrings(self):
        powerData = {}
        powerData["name"] = self.name
        powerData["description"] = AbstractPower.DESCRIPTIONS
        return powerData

    def onLoseHp(self, damageAmount):
        return damageAmount

    def onVictory(self):
        pass

    def canPlayCard(self, card):
        return True
