from ..core.Settings import Settings
from sts_random import stsRandom as Random
from ..characters.AbstractPlayer import AbstractPlayer
from ..actions.GameActionManager import GameActionManager
from ..map.MapRoomNode import MapRoomNode
class AbstractDungeon:
    TEXT = None
    name = None
    levelNum = None
    id = None
    floorNum = 0
    actNum = 0
    player: AbstractPlayer = None
    unlocks = None
    shrineChance = 0
    cardUpgradedChance = 0
    transformedCard = None
    loading_post_combat = False
    is_victory = False
    ascensionLevel = 0
    monsterRng:Random = None
    mapRng:Random = None
    eventRng:Random = None
    merchantRng:Random = None
    cardRng:Random = None
    treasureRng:Random = None
    relicRng:Random = None
    potionRng:Random = None
    monsterHpRng:Random = None
    aiRng:Random = None
    shuffleRng:Random = None
    cardRandomRng:Random = None
    miscRng:Random = None
    srcColorlessCardPool = None
    srcCurseCardPool = None
    srcCommonCardPool = None
    srcUncommonCardPool = None
    srcRareCardPool = None
    colorlessCardPool = None
    curseCardPool = None
    commonCardPool = None
    uncommonCardPool = None
    rareCardPool = None
    commonRelicPool = None
    uncommonRelicPool = None
    rareRelicPool = None
    shopRelicPool = None
    bossRelicPool = None
    lastCombatMetricKey = None
    monsterList = None
    eliteMonsterList = None
    bossList = None
    bossKey = None
    eventList = None
    shrineList = None
    specialOneTimeEventList = None
    actionManager:GameActionManager = None
    topLevelEffects = None
    topLevelEffectsQueue = None
    effectList = None
    effectsQueue = None
    turnPhaseEffectActive = False
    colorlessRareChance = 0
    shopRoomChance = 0
    restRoomChance = 0
    eventRoomChance = 0
    eliteRoomChance = 0
    treasureRoomChance = 0
    smallChestChance = 0
    mediumChestChance = 0
    largeChestChance = 0
    commonRelicChance = 0
    uncommonRelicChance = 0
    rareRelicChance = 0
    scene = None
    currMapNode:MapRoomNode = None
    map = None
    leftRoomAvailable = False
    centerRoomAvailable = False
    rightRoomAvailable = False
    firstRoomChosen = False
    MAP_HEIGHT = 15
    MAP_WIDTH = 7
    MAP_DENSITY = 6
    FINAL_ACT_MAP_HEIGHT = 3
    rs = 0


    def __init__(self, name, levelId, p: AbstractPlayer):
        self.monsterRng = Random(Settings.seed)
        self.eventRng = Random(Settings.seed)
        self.merchantRng = Random(Settings.seed)
        self.cardRng = Random(Settings.seed)
        self.treasureRng = Random(Settings.seed)
        self.relicRng = Random(Settings.seed)
        self.monsterHpRng = Random(Settings.seed)
        self.potionRng = Random(Settings.seed)
        self.aiRng = Random(Settings.seed)
        self.shuffleRng = Random(Settings.seed)
        self.cardRandomRng = Random(Settings.seed)
        self.miscRng = Random(Settings.seed)
        name = ""
        levelNum = ""
        id = ""
        floorNum = 0
        actNum = 0
        player = p
        unlocks = []
        shrineChance = 0.25
        loading_post_combat = False
        is_victory = False
        pass

    def generateSeeds(self):
        self.monsterRng = Random(Settings.seed)
        self.eventRng = Random(Settings.seed)
        self.merchantRng = Random(Settings.seed)
        self.cardRng = Random(Settings.seed)
        self.treasureRng = Random(Settings.seed)
        self.relicRng = Random(Settings.seed)
        self.monsterHpRng = Random(Settings.seed)
        self.potionRng = Random(Settings.seed)
        self.aiRng = Random(Settings.seed)
        self.shuffleRng = Random(Settings.seed)
        self.cardRandomRng = Random(Settings.seed)
        self.miscRng = Random(Settings.seed)

    @classmethod
    def getCurrRoom(cls):
        return cls.currMapNode.getRoom()

    @classmethod
    def getRandomMonster(cls):
        pass

    @classmethod
    def getMonsters(cls):
        pass
    
    