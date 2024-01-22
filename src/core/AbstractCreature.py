from ..powers.AbstractPower import AbstractPower

class AbstractCreature:

    TIP_X_THRESHOLD = 0
    MULTI_TIP_Y_OFFSET = 0
    TIP_OFFSET_R_X = 0
    TIP_OFFSET_L_X = 0
    TIP_OFFSET_Y = 0
    _uiStrings = None
    TEXT = None
    _BLOCK_ANIM_TIME = 0.7
    _BLOCK_OFFSET_DIST = 0
    _SHOW_HB_TIME = 0.7
    _HB_Y_OFFSET_DIST = 0
    BLOCK_ICON_X = 0
    BLOCK_ICON_Y = 0
    _BLOCK_W = 64
    _HEALTH_BAR_PAUSE_DURATION = 1.2
    _HEALTH_BAR_HEIGHT = 0
    _HEALTH_BAR_OFFSET_Y = 0
    _HEALTH_TEXT_OFFSET_Y = 0
    _POWER_ICON_PADDING_X = 0
    _HEALTH_BG_OFFSET_X = 0
    sr = None
    _SHAKE_THRESHOLD = 0
    _SHAKE_SPEED = 0
    SLOW_ATTACK_ANIM_DUR = 1.0
    STAGGER_ANIM_DUR = 0.3
    FAST_ATTACK_ANIM_DUR = 0.4
    HOP_ANIM_DURATION = 0.7
    _STAGGER_MOVE_SPEED = 0
    _RETICLE_W = 36
    _RETICLE_OFFSET_DIST = 0

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.name = None
        self.id = None
        self.powers = []
        self.isPlayer = False
        self.isBloodied = False
        self.drawX = 0
        self.drawY = 0
        self.dialogX = 0
        self.dialogY = 0
        self.hb = None
        self.gold = 0
        self.displayGold = 0
        self.isDying = False
        self.isDead = False
        self.halfDead = False
        self.flipHorizontal = False
        self.flipVertical = False
        self.escapeTimer = 0.0
        self.isEscaping = False
        self.tips = []
        self.healthHb = None
        self._healthHideTimer = 0.0
        self.lastDamageTaken = 0
        self.hb_x = 0
        self.hb_y = 0
        self.hb_w = 0
        self.hb_h = 0
        self.currentHealth = 0
        self.maxHealth = 0
        self.currentBlock = 0
        self._healthBarWidth = 0
        self._targetHealthBarWidth = 0
        self._hbShowTimer = 0.0
        self._healthBarAnimTimer = 0.0
        self._blockAnimTimer = 0.0
        self._blockOffset = 0.0
        self._blockScale = 1.0
        self.hbAlpha = 0.0
        self._hbYOffset = 0
        self._hbBgColor = None
        self._hbShadowColor = None
        self._blockColor = None
        self._blockOutlineColor = None
        self._blockTextColor = None
        self._redHbBarColor = None
        self._greenHbBarColor = None
        self._blueHbBarColor = None
        self._orangeHbBarColor = None
        self._hbTextColor = None
        self.tint = None
        self._shakeToggle = False
        self.animX = 0
        self.animY = 0
        self.vX = 0
        self.vY = 0
        self.animation = 0
        self.animationTimer = 0
        self.atlas = None
        self.skeleton = None
        self.state = None
        self.stateData = None
        self.reticleAlpha = 0
        self._reticleColor = None
        self._reticleShadowColor = None
        self.reticleRendered = False
        self._reticleOffset = 0
        self._reticleAnimTimer = 0

        # self._hbYOffset = com.megacrit.cardcrawl.core.AbstractCreature._HB_Y_OFFSET_DIST * 5.0F
        # self._hbBgColor = com.badlogic.gdx.graphics.Color(0.0F, 0.0F, 0.0F, 0.0F)
        # self._hbShadowColor = com.badlogic.gdx.graphics.Color(0.0F, 0.0F, 0.0F, 0.0F)
        # self._blockColor = com.badlogic.gdx.graphics.Color(0.6F, 0.93F, 0.98F, 0.0F)
        # self._blockOutlineColor = com.badlogic.gdx.graphics.Color(0.6F, 0.93F, 0.98F, 0.0F)
        # self._blockTextColor = com.badlogic.gdx.graphics.Color(0.9F, 0.9F, 0.9F, 0.0F)
        # self._redHbBarColor = com.badlogic.gdx.graphics.Color(0.8F, 0.05F, 0.05F, 0.0F)
        # self._greenHbBarColor = com.badlogic.gdx.graphics.Color.valueOf("78c13c00")
        # self._blueHbBarColor = com.badlogic.gdx.graphics.Color.valueOf("31568c00")
        # self._orangeHbBarColor = com.badlogic.gdx.graphics.Color(1.0F, 0.5F, 0.0F, 0.0F)
        # self._hbTextColor = com.badlogic.gdx.graphics.Color(1.0F, 1.0F, 1.0F, 0.0F)
        # self.tint = com.megacrit.cardcrawl.vfx.TintEffect()
        self._shakeToggle = True
        self.animationTimer = 0.0
        self.atlas = None
        self.reticleAlpha = 0.0
        # self._reticleColor = com.badlogic.gdx.graphics.Color(1.0F, 1.0F, 1.0F, 0.0F)
        # self._reticleShadowColor = com.badlogic.gdx.graphics.Color(0.0F, 0.0F, 0.0F, 0.0F)
        self.reticleRendered = False
        self._reticleOffset = 0.0
        self._reticleAnimTimer = 0.0

    def getPower(self,targetID):
        for p in self.powers:
            if p.ID == targetID:
                return p
        return None

    def hasPower(self,targetID):
        for p in self.powers:
            if p.ID == targetID:
                return True
        return False
