from ..core.Settings import Settings
from ..dungeons.AbstractDungeon import AbstractDungeon
import GlobalVar as global_var

global_var.init()
global_var.set_value('settings', Settings())
global_var.set_value('dungeon', AbstractDungeon())