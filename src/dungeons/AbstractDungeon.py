from ..core import GlobalVar
from sts_random import stsRandom as Random
class AbstractDungeon:
    # monsterRng = None
    # mapRng = None
    # eventRng = None
    # merchantRng = None
    # cardRng = None
    # treasureRng = None
    # relicRng = None
    # potionRng = None
    # monsterHpRng = None
    # aiRng = None
    # shuffleRng = None
    # cardRandomRng = None
    miscRng = None
    srcColorlessCardPool = None
    srcCurseCardPool = None
    srcCommonCardPool = None
    srcUncommonCardPool = None
    srcRareCardPool = None
    colorlessCardPool = None
    curseCardPool = None
    commonCardPool = None
    uncommonCardPool = None
    rareCardPool = None
    commonRelicPool = None
    uncommonRelicPool = None
    rareRelicPool = None
    shopRelicPool = None
    bossRelicPool = None
    def __init__(self):
        self.Settings = GlobalVar.get_value('settings')
        self.monsterRng = Random(self.Settings.seed)
        self.eventRng = Random(self.Settings.seed)
        self.merchantRng = Random(self.Settings.seed)
        self.cardRng = Random(self.Settings.seed)
        self.treasureRng = Random(self.Settings.seed)
        self.relicRng = Random(self.Settings.seed)
        self.monsterHpRng = Random(self.Settings.seed)
        self.potionRng = Random(self.Settings.seed)
        self.aiRng = Random(self.Settings.seed)
        self.shuffleRng = Random(self.Settings.seed)
        self.cardRandomRng = Random(self.Settings.seed)
        self.miscRng = Random(self.Settings.seed)
        pass
    
    def generateSeeds(self):
        self.Settings = GlobalVar.get_value('settings')
        self.monsterRng = Random(self.Settings.seed)
        self.eventRng = Random(self.Settings.seed)
        self.merchantRng = Random(self.Settings.seed)
        self.cardRng = Random(self.Settings.seed)
        self.treasureRng = Random(self.Settings.seed)
        self.relicRng = Random(self.Settings.seed)
        self.monsterHpRng = Random(self.Settings.seed)
        self.potionRng = Random(self.Settings.seed)
        self.aiRng = Random(self.Settings.seed)
        self.shuffleRng = Random(self.Settings.seed)
        self.cardRandomRng = Random(self.Settings.seed)
        self.miscRng = Random(self.Settings.seed)
       
