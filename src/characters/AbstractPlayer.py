from ..core.AbstractCreature import AbstractCreature
from ..dungeons.AbstractDungeon import AbstractDungeon
from enum import Enum
from ..cards.CardGroup import CardGroup
from ..relics.AbstractRelic import AbstractRelic
from ..blights import AbstractBlight
class PlayerClass(Enum):
    IRONCLAD = 0
    THE_SILENT = 1
    DEFECT = 2
    WATCHER = 3


class RHoverType(Enum):
    RELIC = 0
    BLIGHT = 1


class AbstractPlayer(AbstractCreature):
    chosenClass: PlayerClass = None
    gameHandSize: int = None

    masterHandSize: int = None
    startingMaxHP: int = None
    masterDeck: CardGroup = None
    drawPile: CardGroup = None
    hand: CardGroup = None
    discardPile: CardGroup = None
    exhaustPile: CardGroup = None
    limbo: CardGroup = None
    relics: [AbstractRelic] = None
    blights: [AbstractBlight] = None
    potionSlots:int = None
    potions:[AbstractRelic] = None
    energy = None
    isEndingTurn = False
    viewingRelics = False
    inspectMode = False
    inspectHb = None
    damagedThisCombat = 0
    title = None
    orbs = None
    masterMaxOrbs = 0
    maxOrbs = 0
    stance = None
    cardsPlayedThisTurn = 0
    _isHoveringCard = False
    isHoveringDropZone = False
    _hoverStartLine = 0
    _passedHesitationLine = False
    hoveredCard = None
    toHover = None
    cardInUse = None
    isDraggingCard = False
    _isUsingClickDragControl = False
    _clickDragTimer = 0
    inSingleTargetMode = False
    _hoveredMonster = None
    hoverEnemyWaitTimer = 0
    isInKeyboardMode = False
    _skipMouseModeOnce = False
    _keyboardCardIndex = 0
    _touchscreenInspectCount = 0
    img = None
    shoulderImg = None
    shoulder2Img = None
    corpseImg = None
    _arrowScale = 0
    _arrowScaleTimer = 0
    _arrowX = 0
    _arrowY = 0
    endTurnQueued = False
    _points = None
    _controlPoint = None
    _arrowTmp = None
    _startArrowVector = None
    _endArrowVector = None
    _renderCorpse = False

    def __init__(self, name, setClass):
        super().__init__()
        chosenClass = 0
        gameHandSize = 0
        masterHandSize = 0
        startingMaxHP = 0
        masterDeck = None
        drawPile = None
        hand = None
        discardPile = None
        exhaustPile = None
        limbo = None
        relics = None
        blights = None
        potionSlots = 0
        potions = None
        energy = None
        isEndingTurn = False
        viewingRelics = False
        inspectMode = False
        inspectHb = None
        damagedThisCombat = 0
        title = None
        orbs = None
        masterMaxOrbs = 0
        maxOrbs = 0
        stance = None
        cardsPlayedThisTurn = 0
        _isHoveringCard = False
        isHoveringDropZone = False
        _hoverStartLine = 0
        _passedHesitationLine = False
        hoveredCard = None
        toHover = None
        cardInUse = None
        isDraggingCard = False
        _isUsingClickDragControl = False
        _clickDragTimer = 0
        inSingleTargetMode = False
        _hoveredMonster = None
        hoverEnemyWaitTimer = 0
        isInKeyboardMode = False
        _skipMouseModeOnce = False
        _keyboardCardIndex = 0
        _touchscreenInspectCount = 0
        img = None
        shoulderImg = None
        shoulder2Img = None
        corpseImg = None
        _arrowScale = 0
        _arrowScaleTimer = 0
        _arrowX = 0
        _arrowY = 0
        endTurnQueued = False
        _points = None
        _controlPoint = None
        _arrowTmp = None
        _startArrowVector = None
        _endArrowVector = None
        _renderCorpse = False

        # self.masterDeck = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.MASTER_DECK)
        # self.drawPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.DRAW_PILE)
        # self.hand = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.HAND)
        # self.discardPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.DISCARD_PILE)
        # self.exhaustPile = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.EXHAUST_PILE)
        # self.limbo = com.megacrit.cardcrawl.cards.CardGroup(com.megacrit.cardcrawl.cards.CardGroup.CardGroupType.UNSPECIFIED)
        relics = []
        blights = []
        potionSlots = 3
        potions = []
        isEndingTurn = False
        viewingRelics = False
        inspectMode = False
        inspectHb = None
        damagedThisCombat = 0
        orbs = []
        # self.stance = com.megacrit.cardcrawl.stances.NeutralStance()
        cardsPlayedThisTurn = 0
        _isHoveringCard = False
        isHoveringDropZone = False

        hoveredCard = None
        toHover = None
        cardInUse = None
        isDraggingCard = False
        _isUsingClickDragControl = False
        inSingleTargetMode = False
        _hoveredMonster = None
        isInKeyboardMode = False
        _skipMouseModeOnce = False
        _keyboardCardIndex = -1
        _touchscreenInspectCount = 0
        endTurnQueued = False

        _renderCorpse = False
        name = name
        # self.title = self.getTitle(setClass)

        # self.chosenClass = setClass
        isPlayer = True
        # self.initializeStarterRelics(setClass)
        # self.loadPrefs()
        if AbstractDungeon.ascensionLevel >= 11:
            potionSlots -= 1
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

    def hasBlight(self, targetID: str) -> bool:
        for p in blights:
            if p.ID == targetID:
                return True

    def getBlight(self, targetID: str) -> AbstractBlight:
        for p in blights:
            if p.ID == targetID:
                return p
