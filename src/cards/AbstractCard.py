from enum import Enum
from uuid import UUID, uuid4
from .DamageInfo import DamageInfo
from .DescriptionLine import DescriptionLine
from ..dungeons import AbstractDungeon
from ..core.Settings import Settings

from ..rooms.AbstractRoom import AbstractRoom
import math


class CardTags(Enum):
    HEALING = 0
    STRIKE = 1
    EMPTY = 2
    STARTER_DEFEND = 3
    STARTER_STRIKE = 4

    def __int__(self):
        return self.value


class CardType(Enum):
    ATTACK = 0
    SKILL = 1
    POWER = 2
    STATUS = 3
    CURSE = 4

    def __int__(self):
        return self.value


class CardRarity(Enum):
    BASIC = 0
    SPECIAL = 1
    COMMON = 2
    UNCOMMON = 3
    RARE = 4
    CURSE = 5

    def __int__(self):
        return self.value


class CardColor(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    PURPLE = 3
    COLORLESS = 4
    CURSE = 5

    def __int__(self):
        return self.value


class CardTarget(Enum):
    ENEMY = 0
    ALL_ENEMY = 1
    SELF = 2
    NONE = 3
    SELF_AND_ENEMY = 4
    ALL = 5

    def __int__(self):
        return self.value


def compare_to(str1: str, str2: str):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0


class AbstractCard:
    card_type: CardType = None
    cost: int = None
    costForTurn: int = None
    price: int = None
    chargeCost: int = None
    isCostModified: bool = None
    isCostModifiedForTurn: bool = None
    retain: bool = None
    selfRetain: bool = None
    dontTriggerOnUseCard: bool = None
    rarity: CardRarity = None
    color: CardColor = None
    isInnate: bool = None
    isLocked: bool = None
    showEvokeValue: bool = None
    showEvokeOrbCount: int = None
    keywords: [str] = None
    isUsed: bool = None
    upgraded: bool = None
    timesUpgraded: int = None
    misc: int = None
    energyOnUse: int = None
    ignoreEnergyOnUse: int = None
    isSeen: int = None
    upgradedCost: int = None
    upgradedDamage: int = None
    upgradedBlock: int = None
    upgradedMagicNumber: int = None
    uuid: UUID = None
    isSelected: bool = None
    exhaust: bool = None
    returnToHand: bool = None
    shuffleBackIntoDrawPile: bool = None
    isEthereal: bool = None
    tags: [CardTags] = None
    multiDamage: [int] = None
    isMultiDamage: bool = None
    baseDamage: int = None
    baseBlock: int = None
    baseMagicNumber: int = None
    baseHeal: int = None
    baseDraw: int = None
    baseDiscard: int = None
    damage: int = None
    block: int = None
    magicNumber: int = None
    heal: int = None
    draw: int = None
    discard: int = None
    isDamageModified: bool = None
    isBlockModified: bool = None
    isMagicNumberModified: bool = None
    damageType: DamageInfo.DamageType = None
    damageTypeForTurn: DamageInfo.DamageType = None
    target: CardTarget = None
    purgeOnUse: bool = None
    exhaustOnUseOnce: bool = None
    exhaustOnFire: bool = None
    freeToPlayOnce: bool = None
    isInAutoplay: bool = None

    # typeWidthAttack: float = None
    # typeWidthSkill: float = None
    # typeWidthPower: float = None
    # typeWidthCurse: float = None
    # typeWidthStatus: float = None
    # typeOffsetAttack: float = None
    # typeOffsetSkill: float = None
    # typeOffsetPower: float = None
    # typeOffsetCurse: float = None
    # typeOffsetStatus: float = None

    originalName: str = None
    name: str = None
    rawDescription: str = None
    cardID: str = None
    description: [DescriptionLine] = None
    cantUseMessage: str = None
    inBottleFlame = None
    inBottleLightning = None
    inBottleTornado = None

    TEXT: [str] = None

    def __init__(self, id: str, name: str, cost: int, rawDescription: str, card_type: CardType, color: CardColor,
                 rarity: CardRarity, target: CardTarget, dType: DamageInfo.DamageType = DamageInfo.DamageType.NORMAL):
        # 初始化卡片的基本属性
        self.chargeCost = -1
        self.isCostModified = False
        self.isCostModifiedForTurn = False
        self.retain = False
        self.selfRetain = False
        self.dontTriggerOnUseCard = False
        self.isInnate = False
        self.isLocked = False
        self.showEvokeValue = False
        self.showEvokeOrbCount = 0
        self.keywords = []
        self.isUsed = False
        self.upgraded = False
        self.timesUpgraded = 0
        self.misc = 0
        self.ignoreEnergyOnUse = False
        self.isSeen = True
        self.upgradedCost = False
        self.upgradedDamage = False
        self.upgradedBlock = False
        self.upgradedMagicNumber = False
        self.isSelected = False
        self.exhaust = False
        self.returnToHand = False
        self.shuffleBackIntoDrawPile = False
        self.isEthereal = False
        self.tags = []
        self.isMultiDamage = False
        self.baseDamage = -1
        self.baseBlock = -1
        self.baseMagicNumber = -1
        self.baseHeal = -1
        self.baseDraw = -1
        self.baseDiscard = -1
        self.damage = -1
        self.block = -1
        self.magicNumber = -1
        self.heal = -1
        self.draw = -1
        self.discard = -1
        self.isDamageModified = False
        self.isBlockModified = False
        self.isMagicNumberModified = False
        self.target = CardTarget.ENEMY
        self.purgeOnUse = False
        self.exhaustOnUseOnce = False
        self.exhaustOnFire = False
        self.freeToPlayOnce = False
        self.isInAutoplay = False
        self.description = []
        self.inBottleFlame = False
        self.inBottleLightning = False
        self.inBottleTornado = False

        self.originalName = name
        self.name = name
        self.cardID = id

        self.cost = cost
        self.costForTurn = cost
        self.rawDescription = rawDescription
        self.card_type = card_type
        self.color = color
        self.rarity = rarity
        self.target = target
        self.damageType = dType
        self.damageTypeForTurn = dType

        self.uuid = uuid4()

    # def dedupeKeyword(self, keyword: str) -> str:

    # def initializeDescription(self):
    #     self.keywords.clear()
    #     if Settings.lineBreakViaCharacter is False:
    #         self.description.clear()
    #         num_lines = 1
    #         sbuilder = ""
    #         current_width = 0.0
    #
    #         for word in self.rawDescription.split(" "):
    #             is_keyword = False
    #             sbuilder2 = " "
    #             if word and not word[-1].isalnum() and word[-1] != ']':
    #                 sbuilder2 = word[-1] + sbuilder2
    #                 word = word[:-1]
    #
    #             keyword_tmp = self.dedupe_keyword(word.lower())
    #             if keyword_tmp in self.game_dictionary_keywords:
    #                 if keyword_tmp not in self.keywords:
    #                     self.keywords.append(keyword_tmp)
    #
    #                 tmp = len(sbuilder2)  # Simplified width calculation
    #                 current_word_width = len(word) + tmp
    #                 is_keyword = True
    #             elif word and word[0] == '[':
    #                 tmp = len(sbuilder2) + self.CARD_ENERGY_IMG_WIDTH
    #                 if self.color == "RED" and "[R]" not in self.keywords:
    #                     self.keywords.append("[R]")
    #                 # Repeat for other colors
    #             elif word not in ["!D", "!B", "!M"]:
    #                 if word == "NL":
    #                     current_word_width = 0
    #                     self.description.append((sbuilder.strip(), current_width))
    #                     current_width = 0
    #                     num_lines += 1
    #                     sbuilder = ""
    #                     continue
    #                 else:
    #                     current_word_width = len(word + sbuilder2)
    #             else:
    #                 current_word_width = len(word)
    #
    #             if current_width + current_word_width > self.DESC_BOX_WIDTH:
    #                 self.description.append((sbuilder.strip(), current_width))
    #                 num_lines += 1
    #                 sbuilder = ""
    #                 current_width = current_word_width
    #             else:
    #                 current_width += current_word_width
    #
    #             if is_keyword:
    #                 sbuilder += '*'
    #             sbuilder += word + sbuilder2
    #
    #         if sbuilder.strip():
    #             self.description.append((sbuilder.strip(), current_width))
    #
    #         if self.settings.is_dev and num_lines > 5:
    #             self.logger.info(f"WARNING: Card {self.name} has lots of text")

    def hasTag(self, tagToCheck: CardTags):
        return tagToCheck in self.tags

    def canUpgrade(self):
        if self.card_type == CardType.CURSE:
            return False
        elif self.card_type == CardType.STATUS:
            return False
        else:
            return not self.upgraded

    def upgrade(self):
        raise NotImplementedError

    def displayUpgrades(self):
        if self.upgradedCost:
            self.isCostModified = True

        if self.upgradedDamage:
            self.damage = self.baseDamage
            self.isDamageModified = True

        if self.upgradedBlock:
            self.block = self.baseBlock
            self.isBlockModified = True

        if self.upgradedMagicNumber:
            self.magicNumber = self.baseMagicNumber
            self.isMagicNumberModified = True

    def upgradeDamage(self, amount: int):
        self.baseDamage += amount
        self.upgradedDamage = True

    def upgradeBlock(self, amount: int):
        self.baseBlock += amount
        self.upgradedBlock = True

    def upgradeMagicNumber(self, amount: int):
        self.baseMagicNumber += amount
        self.magicNumber = self.baseMagicNumber
        self.upgradedMagicNumber = True

    def upgradeName(self):
        self.timesUpgraded += 1
        self.upgraded = True
        self.name = self.name + "+"

    def upgradeBaseCost(self, newBaseCost: int):
        diff = self.costForTurn - self.cost
        self.cost = newBaseCost
        if self.costForTurn > 0:
            self.costForTurn = self.cost + diff

        if self.costForTurn < 0:
            self.costForTurn = 0

        self.upgradedCost = True

    def makeSameInstanceOf(self):
        card = self.makeStatEquivalentCopy()
        card.uuid = self.uuid
        return card

    def makeStatEquivalentCopy(self):
        card = self.makeCopy()

        i = 0
        while i < self.timesUpgraded:
            card.upgrade()
            i += 1

        card.name = self.name
        card.target = self.target
        card.upgraded = self.upgraded
        card.timesUpgraded = self.timesUpgraded
        card.baseDamage = self.baseDamage
        card.baseBlock = self.baseBlock
        card.baseMagicNumber = self.baseMagicNumber
        card.cost = self.cost
        card.costForTurn = self.costForTurn
        card.isCostModified = self.isCostModified
        card.isCostModifiedForTurn = self.isCostModifiedForTurn
        card.inBottleLightning = self.inBottleLightning
        card.inBottleFlame = self.inBottleFlame
        card.inBottleTornado = self.inBottleTornado
        card.isSeen = self.isSeen
        card.isLocked = self.isLocked
        card.misc = self.misc
        card.freeToPlayOnce = self.freeToPlayOnce
        return card

    def onRemoveFromMasterDeck(self):
        pass

    def cardPlayable(self, m):
        if (self.target != CardTarget.ENEMY and self.target != CardTarget.SELF_AND_ENEMY or m is None or (
                not m.isDying)) and not AbstractDungeon.AbstractDungeon.getMonsters().areMonstersBasicallyDead():
            return True
        else:
            self.cantUseMessage = None
            return False

    def hasEnoughEnergy(self):
        if AbstractDungeon.AbstractDungeon.actionManager.turnHasEnded:
            # self.cantUseMessage = self.TEXT[9]
            return False
        else:
            for p in AbstractDungeon.AbstractDungeon.player.powers:
                if not p.canPlayCard(self):
                    # self.cantUseMessage = self.TEXT[13]
                    return False

            if AbstractDungeon.AbstractDungeon.player.hasPower("Entangled") and self.card_type == CardType.ATTACK:
                # self.cantUseMessage = self.TEXT[10]
                return False

            for r in AbstractDungeon.AbstractDungeon.player.relics:
                if not r.canPlay(self):
                    return False

            for b in AbstractDungeon.AbstractDungeon.player.blights:
                if not b.canPlay(self):
                    return False

            for c in AbstractDungeon.AbstractDungeon.player.hand.group:
                if not c.canPlay(self):
                    return False

            if EnergyPanel.totalCount < self.costForTurn and not self.freeToPlay() and not self.isInAutoplay:
                # self.cantUseMessage = self.TEXT[11]
                return False

            return True

    def tookDamage(self):
        pass

    def didDiscard(self):
        pass

    def switchedStance(self):
        pass

    def useBlueCandle(self, p):
        pass

    def useMedicalKit(self, p):
        pass

    def canPlay(self, card):
        return True

    def canUse(self, p, m):
        if self.card_type == CardType.STATUS and self.costForTurn < -1 and not AbstractDungeon.AbstractDungeon.player.hasRelic(
                "Medical Kit"):
            return False
        elif self.card_type == CardType.CURSE and self.costForTurn < -1 and not AbstractDungeon.AbstractDungeon.player.hasRelic(
                "Blue Candle"):
            return False
        else:
            return self.cardPlayable(m) and self.hasEnoughEnergy()

    def use(self, var1, var2):
        raise NotImplementedError

    def getPrice(rarity):
        if rarity == CardRarity.BASIC:
            return 9999
        elif rarity == CardRarity.SPECIAL:
            return 9999
        elif rarity == CardRarity.COMMON:
            return 50
        elif rarity == CardRarity.UNCOMMON:
            return 75
        elif rarity == CardRarity.RARE:
            return 150
        else:
            return 0

    def updateCost(self, amt: int):
        if self.color == CardColor.CURSE and (
                self.cardID != "Pride") or self.card_type == CardType.STATUS and self.cardID != "Slimed":
            pass
        else:
            tmpCost = self.cost
            diff = self.cost - self.costForTurn
            tmpCost += amt
            if tmpCost < 0:
                tmpCost = 0

            if tmpCost != self.cost:
                self.isCostModified = True
                self.cost = tmpCost
                self.costForTurn = self.cost - diff
                if self.costForTurn < 0:
                    self.costForTurn = 0

    def setCostForTurn(self, amt: int):
        if self.costForTurn >= 0:
            self.costForTurn = amt
            if self.costForTurn < 0:
                self.costForTurn = 0

            if self.costForTurn != self.cost:
                self.isCostModifiedForTurn = True

    def modifyCostForCombat(self, amt: int):
        if self.costForTurn > 0:
            self.costForTurn += amt
            if self.costForTurn < 0:
                self.costForTurn = 0

            if self.cost != self.costForTurn:
                self.isCostModified = True

            self.cost = self.costForTurn
        elif self.cost >= 0:
            self.cost += amt
            if self.cost < 0:
                self.cost = 0

            self.costForTurn = 0
            if self.cost != self.costForTurn:
                self.isCostModified = True

    def resetAttributes(self):
        self.block = self.baseBlock
        self.isBlockModified = False
        self.damage = self.baseDamage
        self.isDamageModified = False
        self.magicNumber = self.baseMagicNumber
        self.isMagicNumberModified = False
        self.damageTypeForTurn = self.damageType
        self.costForTurn = self.cost
        self.isCostModifiedForTurn = False

    def getCost(self) -> str:
        if self.cost == -1:
            return "X"
        else:
            return "0" if self.freeToPlay() else str(self.costForTurn)

    def freeToPlay(self):
        if self.freeToPlayOnce:
            return True
        else:
            return AbstractDungeon.AbstractDungeon.player is not None and AbstractDungeon.AbstractDungeon.currMapNode is not None and AbstractDungeon.AbstractDungeon.getCurrRoom().phase == AbstractRoom.RoomPhase.COMBAT and AbstractDungeon.AbstractDungeon.player.hasPower(
                "FreeAttackPower") and self.card_type == CardType.ATTACK

    def onMoveToDiscard(self):
        pass

    def triggerWhenDrawn(self):
        pass

    def triggerWhenCopied(self):
        pass

    def triggerOnEndOfPlayerTurn(self):
        if self.isEthereal:
            self.addToTop(ExhaustSpecificCardAction(self, AbstractDungeon.AbstractDungeon.player.hand))

    def triggerOnEndOfTurnForPlayingCard(self):
        pass

    def triggerOnOtherCardPlayed(self, c):
        pass

    def triggerOnGainEnergy(self, e: int, dueToCard: bool):
        pass

    def triggerOnManualDiscard(self):
        pass

    def triggerOnCardPlayed(self, cardPlayed):
        pass

    def triggerOnScry(self):
        pass

    def triggerExhaustedCardsOnStanceChange(self, newStance):
        pass

    def triggerAtStartOfTurn(self):
        pass

    def onPlayCard(self, c, m):
        pass

    def atTurnStart(self):
        pass

    def atTurnStartPreDraw(self):
        pass

    def onChoseThisOption(self):
        pass

    def onRetained(self):
        pass

    def triggerOnExhaust(self):
        pass

    def applyPowers(self):
        self.applyPowersToBlock()
        player = AbstractDungeon.AbstractDungeon.player
        self.isDamageModified = False
        if not self.isMultiDamage:
            tmp = float(self.baseDamage)

            for r in player.relics:
                tmp = r.at_damage_modify(tmp, self)
                if self.baseDamage != int(tmp):
                    self.isDamageModified = True

            for p in player.powers:
                tmp = p.atDamageGive(tmp, self.damageTypeForTurn, self)

            tmp = player.stance.atDamageGive(tmp, self.damageTypeForTurn, self)
            if self.baseDamage != int(tmp):
                self.isDamageModified = True

            for p in player.powers:
                tmp = p.atDamageFinalGive(tmp, self.damageTypeForTurn, self)

            tmp = max(0.0, tmp)

            if self.baseDamage != math.floor(tmp):
                self.isDamageModified = True

            self.damage = math.floor(tmp)

        else:
            m = AbstractDungeon.AbstractDungeon.getCurrRoom().monsters.monsters

            tmp = [float(self.baseDamage) for _ in m]

            for i in range(len(tmp)):
                for r in player.relics:
                    tmp[i] = r.atDamageModify(tmp[i], self)
                    if self.baseDamage != int(tmp[i]):
                        self.isDamageModified = True

                for p in player.powers:
                    tmp[i] = p.atDamageGive(tmp[i], self.damageTypeForTurn, self)

                tmp[i] = player.stance.atDamageGive(tmp[i], self.damageTypeForTurn, self)
                if self.baseDamage != int(tmp[i]):
                    self.isDamageModified = True

            for i in range(len(tmp)):
                for p in player.powers:
                    tmp[i] = p.atDamageFinalGive(tmp[i], self.damageTypeForTurn, self)

                tmp[i] = max(0.0, tmp[i])

            self.multiDamage = [math.floor(dmg) for dmg in tmp]

            for i in range(len(tmp)):
                if self.baseDamage != int(tmp[i]):
                    self.isDamageModified = True

            self.damage = self.multiDamage[0]

    def applyPowersToBlock(self):
        self.isBlockModified = False
        tmp = float(self.baseBlock)

        for p in AbstractDungeon.AbstractDungeon.player.powers:
            tmp = p.modifyBlock(tmp, self)

        for p in AbstractDungeon.AbstractDungeon.player.powers:
            tmp = p.modifyBlockLast(tmp)

        if self.baseBlock != math.floor(tmp):
            self.isBlockModified = True

        tmp = max(0.0, tmp)

        self.block = math.floor(tmp)

    def calculateDamageDisplay(self, mo):
        self.calculateCardDamage(mo)

    def calculateCardDamage(self, mo):
        self.applyPowersToBlock()
        player = AbstractDungeon.AbstractDungeon.player
        self.isDamageModified = False

        if not self.isMultiDamage and mo is not None:
            tmp = float(self.baseDamage)

            for r in player.relics:
                tmp = r.atDamageModify(tmp, self)
                if self.baseDamage != int(tmp):
                    self.isDamageModified = True

            # Applying power modifications
            for p in player.powers:
                tmp = p.atDamageGive(tmp, self.damageTypeForTurn, self)

            tmp = player.stance.at_damage_give(tmp, self.damageTypeForTurn, self)
            if self.baseDamage != int(tmp):
                self.isDamageModified = True

            # Applying monster power modifications for damage received
            for p in mo.powers:
                tmp = p.atDamageReceive(tmp, self.damageTypeForTurn, self)

            # Final damage modifications from player
            for p in player.powers:
                tmp = p.atDamageFinalGive(tmp, self.damageTypeForTurn, self)

            # Final damage modifications from monster
            for p in mo.powers:
                tmp = p.atDamageFinalReceive(tmp, self.damageTypeForTurn, self)

            tmp = max(0.0, tmp)

            if self.baseDamage != math.floor(tmp):
                self.isDamageModified = True

            self.damage = math.floor(tmp)

        else:
            m = AbstractDungeon.AbstractDungeon.getCurrRoom().monsters.monsters
            tmp = [float(self.baseDamage) for _ in m]

            # Calculating damage for each monster
            for i in range(len(tmp)):
                # Relic and power modifications
                for r in player.relics:
                    tmp[i] = r.atDamageModify(tmp[i], self)
                    if self.baseDamage != int(tmp[i]):
                        self.isDamageModified = True

                for p in player.powers:
                    tmp[i] = p.atDamageGive(tmp[i], self.damageTypeForTurn, self)

                tmp[i] = player.stance.at_damage_give(tmp[i], self.damageTypeForTurn, self)
                if self.baseDamage != int(tmp[i]):
                    self.isDamageModified = True

                # Monster-specific power adjustments
                for p in m[i].powers:
                    if not m[i].isDying and not m[i].isEscaping:
                        tmp[i] = p.atDamageReceive(tmp[i], self.damageTypeForTurn, self)

                for p in player.powers:
                    tmp[i] = p.atDamageFinalGive(tmp[i], self.damageTypeForTurn, self)

                for p in m[i].powers:
                    if not m[i].isDying and not m[i].isEscaping:
                        tmp[i] = p.atDamageFinalReceive(tmp[i], self.damageTypeForTurn, self)

                tmp[i] = max(0.0, tmp[i])

            self.multiDamage = [math.floor(dmg) for dmg in tmp]

            for i in range(len(tmp)):
                if self.baseDamage != int(tmp[i]):
                    self.isDamageModified = True

            self.damage = self.multiDamage[0]

    def clearPowers(self):
        self.resetAttributes()
        self.isDamageModified = False

    def addToBot(self, action):
        AbstractDungeon.AbstractDungeon.actionManager.addToBottom(action)

    def addToTop(self, action):
        AbstractDungeon.AbstractDungeon.actionManager.addToTop(action)

    def toString(self):
        return self.name

    def compareTo(self, other):
        return compare_to(self.cardID, other.cardID)

    def getMetricID(self):
        id_in = self.cardID
        if self.upgraded:
            id_in = id_in + "+"
            if self.timesUpgraded > 0:
                id_in = id_in + str(self.timesUpgraded)

        return id_in

    def triggerOnGlowCheck(self):
        pass

    def makeCopy(self):
        raise NotImplementedError
