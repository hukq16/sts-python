from enum import Enum
from ..dungeons.AbstractDungeon import AbstractDungeon

class AbstractGameAction:
    DEFAULT_DURATION = 0.5

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.duration = 0
        self.startDuration = 0
        self.actionType = 0
        self.attackEffect = 0
        self.damageType = 0
        self.isDone = False
        self.amount = 0
        self.target = None
        self.source = None

        self.attackEffect = AbstractGameAction.AttackEffect.NONE
        self.isDone = False

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def setValues(self, target, info):
        self.target = target
        self.source = info.owner
        self.amount = info.output
        self.duration = 0.5

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def setValues(self, target, source, amount):
        self.target = target
        self.source = source
        self.amount = amount
        self.duration = 0.5

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def setValues(self, target, source):
        self.target = target
        self.source = source
        self.amount = 0
        self.duration = 0.5

    def isDeadOrEscaped(self, target):
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
        pass

    def tickDuration(self):
        self.duration -= com.badlogic.gdx.Gdx.graphics.getDeltaTime()
        if self.duration < 0.0:
            self.isDone = True


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
