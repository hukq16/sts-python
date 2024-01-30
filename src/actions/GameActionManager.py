

class GameActionManager:
    totalDiscardedThisTurn = 0
    damageReceivedThisTurn = 0
    damageReceivedThisCombat = 0
    hpLossThisCombat = 0
    playerHpLastTurn = 0
    energyGainedThisCombat = 0
    turn = 0

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._nextCombatActions = []
        self.actions = []
        self.preTurnActions = []
        self.cardQueue = []
        self.monsterQueue = []
        self.cardsPlayedThisTurn = []
        self.cardsPlayedThisCombat = []
        self.orbsChanneledThisCombat = []
        self.orbsChanneledThisTurn = []
        self.uniqueStancesThisCombat = {}
        self.mantraGained = 0
        self.currentAction = None
        self.previousAction = None
        self.turnStartCurrentAction = None
        self.lastCard = None
        self.phase = 0
        self.hasControl = False
        self.turnHasEnded = False
        self.usingCard = False
        self.monsterAttacksQueued = False

        # self.phase = GameActionManager.Phase.WAITING_ON_USER
        # self.hasControl = True
        # self.turnHasEnded = False
        # self.usingCard = False
        # self.monsterAttacksQueued = True

    def addToTop(self, action):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        from ..rooms import AbstractRoom
        if AbstractDungeon.getCurrRoom().phase == AbstractRoom.RoomPhase.COMBAT:
            self.actions.insert(0, action)

    def addToBottom(self, action):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        from ..rooms import AbstractRoom
        if AbstractDungeon.getCurrRoom().phase == AbstractRoom.RoomPhase.COMBAT:
            self.actions.append(action)
        pass

    def clearPostCombatActions(self):
        for idx,i in self.actions:
            if isinstance(i,()):
                self.actions.remove(idx)

