from Settings import Settings
from ..dungeons.AbstractDungeon import AbstractDungeon
from . import GlobalVar as global_var

global_var._init()
global_var.set_value('settings', Settings())
global_var.set_value('dungeon', AbstractDungeon())