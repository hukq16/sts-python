
from ..core.AbstractCreature import AbstractCreature
from ..dungeons.AbstractDungeon import AbstractDungeon
class AbstractPlayer(AbstractCreature):
    MSG = None
    LABEL = None
    poisonKillCount = 0
    customMods = None
    HOVER_CARD_Y_POSITION = 0

    def __init__(self, name, setClass):
        #instance fields found by Java to Python Converter:
        self.chosenClass = 0
        self.gameHandSize = 0
        self.masterHandSize = 0
        self.startingMaxHP = 0
        self.masterDeck = None
        self.drawPile = None
        self.hand = None
        self.discardPile = None
        self.exhaustPile = None
        self.limbo = None
        self.relics = None
        self.blights = None
        self.potionSlots = 0
        self.potions = None
        self.energy = None
        self.isEndingTurn = False
        self.viewingRelics = False
        self.inspectMode = False
        self.inspectHb = None
        self.damagedThisCombat = 0
        self.title = None
        self.orbs = None
        self.masterMaxOrbs = 0
        self.maxOrbs = 0
        self.stance = None
        self.cardsPlayedThisTurn = 0
        self._isHoveringCard = False
        self.isHoveringDropZone = False
        self._hoverStartLine = 0
        self._passedHesitationLine = False
        self.hoveredCard = None
        self.toHover = None
        self.cardInUse = None
        self.isDraggingCard = False
        self._isUsingClickDragControl = False
        self._clickDragTimer = 0
        self.inSingleTargetMode = False
        self._hoveredMonster = None
        self.hoverEnemyWaitTimer = 0
        self.isInKeyboardMode = False
        self._skipMouseModeOnce = False
        self._keyboardCardIndex = 0
        self._touchscreenInspectCount = 0
        self.img = None
        self.shoulderImg = None
        self.shoulder2Img = None
        self.corpseImg = None
        self._arrowScale = 0
        self._arrowScaleTimer = 0
        self._arrowX = 0
        self._arrowY = 0
        self.endTurnQueued = False
        self._points = None
        self._controlPoint = None
        self._arrowTmp = None
        self._startArrowVector = None
        self._endArrowVector = None
        self._renderCorpse = False

        # self.masterDeck = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.MASTER_DECK)
        # self.drawPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.DRAW_PILE)
        # self.hand = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.HAND)
        # self.discardPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.DISCARD_PILE)
        # self.exhaustPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.EXHAUST_PILE)
        # self.limbo = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.UNSPECIFIED)
        self.relics = []
        self.blights = []
        self.potionSlots = 3
        self.potions = []
        self.isEndingTurn = False
        self.viewingRelics = False
        self.inspectMode = False
        self.inspectHb = None
        self.damagedThisCombat = 0
        self.orbs = []
        # self.stance = com.megacrit.cardcrawl.stances.NeutralStance()
        self.cardsPlayedThisTurn = 0
        self._isHoveringCard = False
        self.isHoveringDropZone = False


        self.hoveredCard = None
        self.toHover = None
        self.cardInUse = None
        self.isDraggingCard = False
        self._isUsingClickDragControl = False
        self.inSingleTargetMode = False
        self._hoveredMonster = None
        self.isInKeyboardMode = False
        self._skipMouseModeOnce = False
        self._keyboardCardIndex = -1
        self._touchscreenInspectCount = 0
        self.endTurnQueued = False

        self._renderCorpse = False
        self.name = name
        # self.title = self.getTitle(setClass)

        # self.chosenClass = setClass
        self.isPlayer = True
        # self.initializeStarterRelics(setClass)
        # self.loadPrefs()
        if AbstractDungeon.ascensionLevel >= 11:
            self.potionSlots -= 1
        #
        # self.potions.clear()

        # i = 0
        # i = 0
        # while i < self.potionSlots:
        #     self.potions.append(com.megacrit.cardcrawl.potions.PotionSlot(i))
        #     i += 1
        #
        # i = 0
        # while i < len(self._points):
        #     self._points[i] = com.badlogic.gdx.math.Vector2()
        #     i += 1
