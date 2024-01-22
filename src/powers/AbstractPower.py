

from enum import Enum


class PowerType(Enum):
    BUFF = 0
    DEBUFF = 1
class AbstractPower():

    atlas = None
    _RAW_W = 32
    POWER_STACK_FONT_SCALE = 8.0
    _FONT_LERP = 10.0
    _FONT_SNAP_THRESHOLD = 0.05
    DESCRIPTIONS = None

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.region48 = None
        self.region128 = None
        self.fontScale = 1.0
        # self._color = com.badlogic.gdx.graphics.Color(1.0F, 1.0F, 1.0F, 0.0F)
        # self._redColor = com.badlogic.gdx.graphics.Color(1.0F, 0.0F, 0.0F, 1.0F)
        # self._greenColor = com.badlogic.gdx.graphics.Color(0.0F, 1.0F, 0.0F, 1.0F)
        self._effect = []
        self.owner = None
        self.name = None
        self.description = None
        self.ID = None
        self.img = None
        self.amount = -1
        self.priority = 5
        self.type = 0
        self.isTurnBased = False
        self.isPostActionPower = False
        self.canGoNegative = False

        self.type = PowerType.BUFF
        self.isTurnBased = False
        self.isPostActionPower = False
        self.canGoNegative = False


