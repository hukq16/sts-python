# nearly finished
from enum import Enum
from .CardSave import CardSave
from .AbstractCard import CardRarity, CardType, CardColor


class CardGroupType(Enum):
    DRAW_PILE = 0
    MASTER_DECK = 1
    HAND = 2
    DISCARD_PILE = 3
    EXHAUST_PILE = 4
    CARD_POOL = 5
    UNSPECIFIED = 6

    def __int__(self):
        return self.value


class CardGroup:

    def __init__(self, type: CardGroupType, g=None):
        # 初始化实例变量
        # Initialize instance variables
        self.handPositioningMap = {}
        self.queued = []
        self.inHand = []
        self.type = type
        self.group = []
        if g:
            # 如果传入了一个 CardGroup 对象，复制其内容
            # If a CardGroup object is passed, copy its content
            for c in g.group:
                self.group.append(c.makeSameInstanceOf())

    def getCardDeck(self):
        """
        获取卡牌套组。
        Retrieve the card deck.
        """
        retVal = []
        for card in self.group:
            retVal.append(CardSave(card.cardID, card.timesUpgraded, card.misc))
        return retVal

    def getCardNames(self):
        """
        获取卡牌名称列表。
        Retrieve list of card names.
        """
        retVal = []
        for card in self.group:
            retVal.append(card.cardID)
        return retVal

    def getCardIdsForMetrics(self):
        """
        获取用于指标的卡牌ID列表。
        Retrieve list of card IDs for metrics.
        """
        retVal = []
        for card in self.group:
            retVal.append(card.getMetricID())
        return retVal

    def clear(self):
        """
        清空卡牌组。
        Clear the card group.
        """
        self.group.clear()

    def contains(self, c):
        """
        检查是否包含指定卡牌。
        Check if a specific card is contained.
        """
        return c in self.group

    def canUseAnyCard(self):
        """
        检查是否有任何卡牌可以使用。
        Check if any card can be used.
        """
        for card in self.group:
            if card.hasEnoughEnergy():
                return True
        return False

    def fullSetCheck(self):
        """
        检查是否有完整的卡牌套组。
        Check for a full set of cards.
        """
        times = 0
        card_ids = [card.cardID for card in self.group if card.rarity != CardRarity.BASIC]
        card_count = {}
        for card_id in card_ids:
            card_count[card_id] = card_count.get(card_id, 0) + 1

        for card, count in card_count.items():
            if count >= 4:
                times += 1

        return times

    def pauperCheck(self):
        """
        检查是否是低级卡牌。
        Check if all cards are of low rarity.
        """
        for card in self.group:
            if card.rarity == CardRarity.RARE:
                return False
        return True

    def cursedCheck(self):
        """
        检查是否是诅咒卡牌。
        Check for cursed cards.
        """
        count = sum(1 for card in self.group if card.type == CardType.CURSE)
        return count >= 5

    def highlanderCheck(self):
        """
        检查是否是高地人套组。
        Check for a Highlander set.
        """
        card_ids = [card.cardID for card in self.group if card.rarity != CardRarity.BASIC]
        return len(set(card_ids)) == len(card_ids)

    def applyPowers(self):
        """
        应用所有卡牌的力量。
        Apply powers to all cards.
        """
        for card in self.group:
            card.applyPowers()

    def removeCard(self, c):
        """
        从卡组中移除一张卡牌。
        Remove a card from the group.
        """

        from ..dungeons.AbstractDungeon import AbstractDungeon
        from .AbstractCard import AbstractCard
        if isinstance(c, AbstractCard):
            self.group.remove(c)
            if self.type == CardGroupType.MASTER_DECK:
                c.onRemoveFromMasterDeck()
                for r in AbstractDungeon.player.relics:
                    r.onMasterDeckChange()
        elif isinstance(c, str):
            for card in self.group:
                if card.cardID == c:
                    self.group.remove(card)
                    return True
            return False

    def addToHand(self, c):
        """
        将一张卡牌添加到手牌中。
        Add a card to the hand.
        """
        self.group.append(c)

    def addToTop(self, card):
        """将一张卡添加到卡组顶部"""
        self.group.append(card)

    def addToBottom(self, card):
        """将一张卡添加到卡组底部"""
        self.group.insert(0, card)

    def addToRandomSpot(self, card):
        """将一张卡添加到卡组随机位置"""
        from ..dungeons.AbstractDungeon import AbstractDungeon
        if not self.group:
            self.group.append(card)
        else:
            self.group.insert(AbstractDungeon.cardRandomRng.random(len(self.group) - 1), card)

    def getTopCard(self):
        """获取卡组顶部的卡"""
        return self.group[-1] if self.group else None

    def getNCardFromTop(self, num: int):
        """从卡组顶部获取第n张卡"""
        if len(self.group) > num:
            return self.group[-1 - num]
        return None

    def getBottomCard(self):
        """获取卡组底部的卡"""
        return self.group[0] if self.group else None

    def getRandomCard(self, rng_or_useRng_or_type, useRng_or_rarity=None):
        """
        根据给定条件获取随机卡牌
        """
        from sts_random import stsRandom as Random
        from ..dungeons.AbstractDungeon import AbstractDungeon
        from ..badlogic.math.MathUtils import MathUtils
        if useRng_or_rarity is None:
            if isinstance(rng_or_useRng_or_type, bool):
                if rng_or_useRng_or_type:
                    return self.group[AbstractDungeon.cardRng.random(len(self.group) - 1)]
                else:
                    return self.group[MathUtils.randomInt(len(self.group) - 1)]
            elif isinstance(rng_or_useRng_or_type, Random):
                return self.group[rng_or_useRng_or_type.random(len(self.group) - 1)]

        if useRng_or_rarity is not None:
            if isinstance(rng_or_useRng_or_type, bool) and isinstance(useRng_or_rarity, CardRarity):
                filtered = [c for c in self.group if c.rarity == useRng_or_rarity]
                if not filtered:
                    return None
                else:
                    filtered.sort()
                    if rng_or_useRng_or_type:
                        return filtered[AbstractDungeon.cardRng.random(len(filtered) - 1)]
                    else:
                        return filtered[MathUtils.randomInt(len(filtered) - 1)]
            elif isinstance(rng_or_useRng_or_type, Random) and isinstance(useRng_or_rarity, CardRarity):
                filtered = [c for c in self.group if c.rarity == useRng_or_rarity]
                if not filtered:
                    return None
                else:
                    filtered.sort()
                    return filtered[rng_or_useRng_or_type.random(len(filtered) - 1)]
            elif isinstance(rng_or_useRng_or_type, CardType) and isinstance(useRng_or_rarity, bool):
                filtered = [c for c in self.group if c.type == rng_or_useRng_or_type]
                if not filtered:
                    return None
                else:
                    filtered.sort()
                    if useRng_or_rarity:
                        return filtered[AbstractDungeon.cardRng.random(len(filtered) - 1)]
                    else:
                        return filtered[MathUtils.randomInt(len(filtered) - 1)]

    def removeTopCard(self):
        """移除卡组顶部的卡牌"""
        if self.group:
            self.group.pop(len(self.group) - 1)

    def shuffle(self, rng=None):
        """洗牌"""
        from ..badlogic.math.MathUtils import MathUtils
        from sts_random import JavaRandom
        from ..dungeons.AbstractDungeon import AbstractDungeon
        if rng is None:
            MathUtils.shuffle(self.group, random=JavaRandom(AbstractDungeon.shuffleRng.randomLong()))
        else:
            MathUtils.shuffle(self.group, random=JavaRandom(rng.randomLong()))

    def __str__(self):
        """以字符串形式返回卡组信息"""
        return "\n".join(card.cardID for card in self.group)

    def update(self):
        """更新卡组中每张卡的状态"""
        for card in self.group:
            card.update()

    def isEmpty(self):
        return not self.group

    def size(self):
        return len(self.group)

    def getUpgradableCards(self):
        retVal = CardGroup(CardGroupType.UNSPECIFIED)
        for card in self.group:
            if card.canUpgrade():
                retVal.group.append(card)
        return retVal

    def hasUpgradableCards(self):
        """检查是否有可升级的卡牌"""
        return any(card.canUpgrade() for card in self.group)

    def getPurgeableCards(self):
        """获取可净化的卡牌"""
        retVal = CardGroup(CardGroupType.UNSPECIFIED)
        for card in self.group:
            if card.cardID not in ["Necronomicurse", "CurseOfTheBell", "AscendersBane"]:
                retVal.group.append(card)
        return retVal

    def getSpecificCard(self, target_card):
        """获取指定的卡牌"""
        return target_card if target_card in self.group else None

    def triggerOnOtherCardPlayed(self, usedCard):
        from ..dungeons.AbstractDungeon import AbstractDungeon
        """当其他卡牌被播放时触发"""
        for card in self.group:
            if card != usedCard:
                card.triggerOnOtherCardPlayed(usedCard)

        # 假设AbstractDungeon.player.powers已经按Python方式实现
        for power in AbstractDungeon.player.powers:
            power.onAfterCardPlayed(usedCard)

    def sortWithComparator(self, comp, ascending=True):
        """使用比较器进行排序"""
        self.group.sort(key=comp, reverse=not ascending)

    def sortByRarity(self, ascending=True):
        """按稀有度排序"""
        self.sortWithComparator(lambda card: card.rarity, ascending)

    def sortByRarityPlusStatusCardType(self, ascending=True):
        from functools import cmp_to_key
        """按稀有度和状态卡牌类型排序"""
        self.sortWithComparator(lambda card: card.rarity, ascending)
        self.sortWithComparator(cmp_to_key(CardGroup.status_cards_last_comparator), ascending)

    def sortByType(self, ascending=True):
        """按卡牌类型排序"""
        self.sortWithComparator(lambda card: card.card_type, ascending)

    def sortByAcquisition(self):
        pass

    # def sortByStatus(self,ascending=True):
    #     """按状态排序"""
    #     from functools import cmp_to_key
    #     self.sortWithComparator(cmp_to_key(CardGroup.status_cards_last_comparator), ascending)
    def sortAlphabetically(self, ascending=True):
        """按字母顺序排序"""
        self.sortWithComparator(lambda card: card.name, ascending)

    def sortByCost(self, ascending=True):
        """按消耗排序"""
        self.sortWithComparator(lambda card: card.cost, ascending)

    @staticmethod
    def status_cards_last_comparator(c1, c2):
        if c1.type == CardType.STATUS and c2.type != CardType.STATUS:
            return 1
        elif c1.type != CardType.STATUS and c2.type == CardType.STATUS:
            return -1
        else:
            return 0

    def getSkills(self):
        return self.getCardsOfType(CardType.SKILL)

    def getAttacks(self):
        return self.getCardsOfType(CardType.ATTACK)

    def getPowers(self):
        return self.getCardsOfType(CardType.POWER)

    def getCardsOfType(self, cardType):
        retVal = CardGroup(CardGroupType.UNSPECIFIED)
        for card in self.group:
            if card.type == cardType:
                retVal.addToBottom(card)
        return retVal

    def getGroupedByColor(self):
        colorGroups = {color: CardGroup(CardGroupType.UNSPECIFIED) for color in CardColor}
        for card in self.group:
            colorGroups[card.color].addToTop(card)

        retVal = CardGroup(CardGroupType.UNSPECIFIED)
        for group in colorGroups.values():
            retVal.group.extend(group.group)
        return retVal

    def findCardById(self, id):
        for card in self.group:
            if card.cardID == id:
                return card
        return None

    @staticmethod
    def getGroupWithoutBottledCards(group):
        retVal = CardGroup(CardGroupType.UNSPECIFIED)
        for card in group.group:
            if not card.inBottleFlame and not card.inBottleLightning and not card.inBottleTornado:
                retVal.addToTop(card)
        return retVal
