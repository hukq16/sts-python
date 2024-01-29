class Settings:
    seed = 0
    isDev = False
    isBeta = False
    isAlpha = False
    isModded = False
    isControllerMode = False
    isMobile = False
    testFonts = False
    isDebug = False
    isInfo = False
    isTestingNeow = False
    usesTrophies = False
    isConsoleBuild = False
    usesProfileSaves = False
    isTouchScreen = False
    isDemo = False
    isShowBuild = False
    isPublisherBuild = False
    language = 0
    lineBreakViaCharacter = False
    usesOrdinal = True
    leftAlignCards = False
    manualLineBreak = False
    removeAtoZSort = False
    manualAndAutoLineBreak = False
    soundPref = None
    dailyPref = None
    gamePref = None
    isDailyRun = False
    hasDoneDailyToday = False
    dailyDate = 0
    totalPlayTime = 0
    isFinalActAvailable = False
    hasRubyKey = False
    hasEmeraldKey = False
    hasSapphireKey = False
    isEndless = False
    isTrial = False
    specialSeed = 0
    trialName = None
    IS_FULLSCREEN = False
    IS_W_FULLSCREEN = False
    IS_V_SYNC = False
    MAX_FPS = 0
    M_W = 0
    M_H = 0
    SAVED_WIDTH = 0
    SAVED_HEIGHT = 0
    WIDTH = 0
    HEIGHT = 0
    isSixteenByTen = False
    isFourByThree = False
    isTwoSixteen = False
    isLetterbox = False
    HORIZ_LETTERBOX_AMT = 0
    VERT_LETTERBOX_AMT = 0
    displayOptions = None
    displayIndex = 0
    scale:float = 1.0
    renderScale = 0
    xScale = 0
    yScale = 0
    FOUR_BY_THREE_OFFSET_Y = 0
    LETTERBOX_OFFSET_Y = 0
    seed = 0
    seedSet = False
    seedSourceTimestamp = 0
    isBackgrounded = False
    bgVolume = 0.0

    MASTER_VOLUME = 0
    MUSIC_VOLUME = 0
    SOUND_VOLUME = 0
    AMBIANCE_ON = False

    SHOW_DMG_SUM = False
    SHOW_DMG_BLOCK = False
    FAST_HAND_CONF = False
    FAST_MODE = False
    CONTROLLER_ENABLED = False
    TOUCHSCREEN_ENABLED = False
    DISABLE_EFFECTS = False
    UPLOAD_DATA = False
    SCREEN_SHAKE = False
    PLAYTESTER_ART_MODE = False
    SHOW_CARD_HOTKEYS = False
    USE_LONG_PRESS = False
    BIG_TEXT_MODE = False

    POST_ATTACK_WAIT_DUR = 0.1
    WAIT_BEFORE_BATTLE_TIME = 1.0
    ACTION_DUR_XFAST = 0.1
    ACTION_DUR_FASTER = 0.2
    ACTION_DUR_FAST = 0.25
    ACTION_DUR_MED = 0.5
    ACTION_DUR_LONG = 1.0
    ACTION_DUR_XLONG = 1.5
    CARD_DROP_END_Y = 0
    SCROLL_SPEED = 0
    MAP_SCROLL_SPEED = 0
    SCROLL_LERP_SPEED = 12.0
    SCROLL_SNAP_BACK_SPEED = 10.0
    DEFAULT_SCROLL_LIMIT = 0
    MAP_DST_Y = 0
    CLICK_SPEED_THRESHOLD = 0.4
    CLICK_DIST_THRESHOLD = 0
    POTION_W = 0
    POTION_Y = 0

    CARD_SNAP_THRESHOLD = 0
    UI_SNAP_THRESHOLD = 0

    HOVER_BUTTON_RISE_AMOUNT = 0

    OPTION_Y = 0
    EVENT_Y = 0
    MAX_ASCENSION_LEVEL = 20

    MAX_HAND_SIZE = 10
    NUM_POTIONS = 3
    NORMAL_POTION_DROP_RATE = 40
    ELITE_POTION_DROP_RATE = 40
    BOSS_GOLD_AMT = 100
    BOSS_GOLD_JITTER = 5
    ACHIEVEMENT_COUNT = 46
    NORMAL_RARE_DROP_RATE = 3
    NORMAL_UNCOMMON_DROP_RATE = 40
    ELITE_RARE_DROP_RATE = 10
    ELITE_UNCOMMON_DROP_RATE = 50
    UNLOCK_PER_CHAR_COUNT = 5
    hideTopBar = False
    hidePopupDetails = False
    hideRelics = False
    hideLowerElements = False
    hideCards = False
    hideEndTurn = False
    hideCombatElements = False
    SENDTODEVS = "sendToDevs"

    def __init__(self):
        self.seed = 1
        self.seedSet = False

    @classmethod
    def getseed(cls):
        return cls.seed