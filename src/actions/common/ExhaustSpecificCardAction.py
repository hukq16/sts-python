# finished
from ..AbstractGameAction import AbstractGameAction

from ...core.Settings import Settings


class ExhaustSpecificCardAction(AbstractGameAction):
    targetCard = None
    group = None
    startingDuration = 0

    def __init__(self, targetCard, group, isFast=False):
        super().__init__()
        from ...dungeons.AbstractDungeon import AbstractDungeon
        self.targetCard = targetCard
        self.setValues(AbstractDungeon.player, AbstractDungeon.player, self.amount)
        self.actionType = AbstractGameAction.ActionType.EXHAUST
        self.group = group
        self.startingDuration = Settings.ACTION_DUR_FAST
        self.duration = self.startingDuration

    def update(self):
        if self.duration == self.startingDuration and self.group.contains(self.targetCard):
            self.group.moveToExhaustPile(self.targetCard)
            self.targetCard.exhaustOnUseOnce = False
            self.targetCard.freeToPlayOnce = False

        self.tickDuration()
