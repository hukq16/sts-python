# nearly finished
from enum import Enum
from ..dungeons.AbstractDungeon import AbstractDungeon
from ..cards.DamageInfo import DamageInfo
from ..core.AbstractCreature import AbstractCreature


class AbstractGameAction:
    # DEFAULT_DURATION = 0.5
    # duration: float = 0
    # startDuration: float = 0
    damageType: DamageInfo.DamageType = None
    isDone: bool = False
    amount: int = 0
    target: AbstractCreature = None
    source: AbstractCreature = None

    def __init__(self):
        self.isDone = False

    def setValues(self, target: AbstractCreature, source: AbstractCreature, amount: int = None,
                  info: DamageInfo = None):
        if amount is None and info is not None:
            self.target = target
            self.source = info.owner
            self.amount = info.output
            # self.duration = 0.5
        elif amount is not None and info is None:
            self.target = target
            self.source = source
            self.amount = amount
            # self.duration = 0.5
        elif amount is None and info is None:
            self.target = target
            self.source = source
            self.amount = 0
            # self.duration = 0.5

    def isDeadOrEscaped(self, target: AbstractCreature) -> bool:
        if (not target.isDying) and not target.halfDead:
            if not target.isPlayer:
                m = target
                if m.isEscaping:
                    return True
            return False
        else:
            return True

    def addToBot(self, action):
        AbstractDungeon.actionManager.addToBottom(action)

    def addToTop(self, action):
        AbstractDungeon.actionManager.addToTop(action)

    def update(self):
        raise NotImplementedError

    # def tickDuration(self):
    #     self.duration -= getDeltaTime()
    #     if self.duration < 0.0:
    #         self.isDone = True

    def shouldCancelAction(self):
        return self.target is None or self.source is not None and self.source.isDying or self.target.isDeadOrEscaped()

    class ActionType(Enum):
        BLOCK = 0
        POWER = 1
        CARD_MANIPULATION = 2
        DAMAGE = 3
        DEBUFF = 4
        DISCARD = 5
        DRAW = 6
        EXHAUST = 7
        HEAL = 8
        ENERGY = 9
        TEXT = 10
        USE = 11
        CLEAR_CARD_QUEUE = 12
        DIALOG = 13
        SPECIAL = 14
        WAIT = 15
        SHUFFLE = 16
        REDUCE_POWER = 17

        def __int__(self):
            return self.value

    class AttackEffect(Enum):
        BLUNT_LIGHT = 0
        BLUNT_HEAVY = 1
        SLASH_DIAGONAL = 2
        SMASH = 3
        SLASH_HEAVY = 4
        SLASH_HORIZONTAL = 5
        SLASH_VERTICAL = 6
        NONE = 7
        FIRE = 8
        POISON = 9
        SHIELD = 10
        LIGHTNING = 11

        def __int__(self):
            return self.value
