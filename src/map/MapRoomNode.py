from src.rooms.AbstractRoom import AbstractRoom
class MapRoomNode:
    _IMG_WIDTH = 0
    OFFSET_X = 0
    _OFFSET_Y = 0
    _SPACING_X = 0
    _JITTER_X = 0
    _JITTER_Y = 0
    AVAILABLE_COLOR = None
    _NOT_TAKEN_COLOR = None
    _OUTLINE_COLOR = None
    _W = 128
    _O_W = 192
    _ANIM_WAIT_TIME = 0.25

    def __init__(self, x, y):
        # instance fields found by Java to Python Converter:
        self.offsetX = 0
        self.offsetY = 0
        self.color = None
        self._oscillateTimer = 0
        self.hb = None
        self._scale = 0
        self._angle = 0
        self._parents = None
        self._fEffects = None
        self._flameVfxTimer = 0
        self.x = 0
        self.y = 0
        self.room:AbstractRoom = None
        self._edges = None
        self.taken = False
        self.highlighted = False
        self._animWaitTimer = 0
        self.hasEmeraldKey = False

    def getRoom(self):
        return self.room

