class CardGroup:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self.group = []
        self.HAND_START_X = 0
        self.HAND_OFFSET_X = 0
        self.type = 0
        self.handPositioningMap = None
        self._queued = None
        self._inHand = None

    _LOGGER = org.apache.logging.log4j.LogManager.getLogger(CardGroup.__name__)
    _HAND_HOVER_PUSH_AMT = 0.4F
    _PUSH_TAPER = 0.25F
    _TWO_CARD_PUSH_AMT = 0.2F
    _THREE_FOUR_CARD_PUSH_AMT = 0.27F
    DRAW_PILE_X = 0
    DRAW_PILE_Y = 0
    DISCARD_PILE_X = 0
    DISCARD_PILE_Y = 0

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public CardGroup(CardGroupType type)
    def __init__(self, type):
        self._initialize_instance_fields()

        self.HAND_START_X = float(com.megacrit.cardcrawl.core.Settings.WIDTH) * 0.36F
        self.HAND_OFFSET_X = AbstractCard.IMG_WIDTH * 0.35F
        self.handPositioningMap = {}
        self._queued = []
        self._inHand = []
        self.type = type

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public CardGroup(CardGroup g, CardGroupType type)
    def __init__(self, g, type):
        self._initialize_instance_fields()

        self.HAND_START_X = float(com.megacrit.cardcrawl.core.Settings.WIDTH) * 0.36F
        self.HAND_OFFSET_X = AbstractCard.IMG_WIDTH * 0.35F
        self.handPositioningMap = {}
        self._queued = []
        self._inHand = []
        self.type = type
        var3 = g.group.iterator()

        while var3.hasNext():
            c = var3.next()
            self.group.append(c.makeSameInstanceOf())