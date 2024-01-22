
from enum import Enum


class RoomType(Enum):
    SHOP = 0
    MONSTER = 1
    SHRINE = 2
    TREASURE = 3
    EVENT = 4
    BOSS = 5


class RoomPhase(Enum):
    COMBAT = 0
    EVENT = 1
    COMPLETE = 2
    INCOMPLETE = 3

class AbstractRoom():
    _uiStrings = None
    TEXT = None
    _logger = None
    _END_TURN_WAIT_DURATION = 1.2
    blizzardPotionMod = 0
    _BLIZZARD_POTION_MOD_AMT = 10
    waitTimer = 0
    phase: RoomPhase = None

    def __init__(self):
        self.potions = []
        self.relics = []
        self.rewards = []
        # self.souls = SoulGroup()
        self.phase =  0
        self.event = None
        self.monsters = None
        self._endBattleTimer = 0.0
        self.rewardPopOutTimer = 1.0
        self.mapSymbol = None
        self.mapImg = None
        self.mapImgOutline = None
        self.isBattleOver = False
        self.cannotLose = False
        self.eliteTrigger = False
        self.mugged = False
        self.smoked = False
        self.combatEvent = False
        self.rewardAllowed = True
        self.rewardTime = False
        self.skipMonsterTurn = False
        self.baseRareCardChance = 3
        self.baseUncommonCardChance = 37
        self.rareCardChance = 0
        self.uncommonCardChance = 0

        self.rareCardChance = self.baseRareCardChance
        self.uncommonCardChance = self.baseUncommonCardChance






