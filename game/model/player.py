from model.inventory_item import InventoryItem
from model.item_magic_level import MagicLevel
import functools


class Player:
    SQUIRREL = 'Cyber Squirrel'
    SHAMAN = 'Techno Shaman'
    RICH = 'Rich Person'

    LEFT_SHOE = 'Left shoe'
    RIGHT_SHOE = 'Right shoe'
    MUG = 'Mug'
    CHICKEN_FEATHER = 'Chicken feather'
    ZOMBIE_ARM = 'Zombie arm'
    CHAINSAW = 'Chainsaw'
    CAT = 'Cat'
    GRENADE = 'Grenade'
    CHIPS = 'Chips'

    SCREEN_ELEMENTS = 'screen_elements'
    AUDIO = 'audio'

    ZERO = 0

    CLASS_IMAGES = {
        SQUIRREL: f'{SCREEN_ELEMENTS}/squirrel_idle.png', 
        SHAMAN: f'{SCREEN_ELEMENTS}/shaman_idle.png',
        RICH: f'{SCREEN_ELEMENTS}/rich_idle.png'
    }

    CLASS_SOUND_EFFECTS = {
        SQUIRREL: f'{AUDIO}/roar.mp3', 
        SHAMAN: f'{AUDIO}/yipee.mp3',
        RICH: f'{AUDIO}/cash.mp3'
    }

    EXTRA_INVETORY_ITEMS = {
        CHICKEN_FEATHER: InventoryItem(CHICKEN_FEATHER, f'{SCREEN_ELEMENTS}/feather_icon.png', 60, 80, MagicLevel.STRONG), 
        ZOMBIE_ARM: InventoryItem(ZOMBIE_ARM, f'{SCREEN_ELEMENTS}/arm_icon.png', 50, 75, MagicLevel.MEDIUM),
        CHAINSAW: InventoryItem(CHAINSAW, f'{SCREEN_ELEMENTS}/chainsaw_icon.png', 50, 70, MagicLevel.MEDIUM),
        CAT: InventoryItem(CAT, f'{SCREEN_ELEMENTS}/cat_icon.png', ZERO, ZERO, MagicLevel.EXTREME),
        GRENADE: InventoryItem(GRENADE, f'{SCREEN_ELEMENTS}/grenade_icon.png', ZERO, ZERO, MagicLevel.LOW),
        CHIPS: InventoryItem(CHIPS, f'{SCREEN_ELEMENTS}/chips_icon.png', 500, 1000, MagicLevel.MEDIUM)
    }

    def __init__(self, class_name):
        self._class = class_name
        self._image = self.CLASS_IMAGES.get(class_name)
        self._sound_effect = self.CLASS_SOUND_EFFECTS.get(class_name)

        self._inventory = {
            self.LEFT_SHOE: InventoryItem(self.LEFT_SHOE, f'{self.SCREEN_ELEMENTS}/shoes_icon.png', self.ZERO, self.ZERO, MagicLevel.LOW),
            self.RIGHT_SHOE: InventoryItem(self.RIGHT_SHOE, f'{self.SCREEN_ELEMENTS}/shoes_icon.png', self.ZERO, self.ZERO, MagicLevel.LOW),
            self.MUG: InventoryItem(self.MUG, f'{self.SCREEN_ELEMENTS}/mug_icon.png', self.ZERO, self.ZERO, MagicLevel.STRONG)
        }

        self._knight_status = 'No association'
        self._dark_deeds = 0
        self._holy_deeds = 0
        self._lawsuits = 0
        self._headbutts = 0
        self._friends = []

    def get_class_name(self):
        return self._class

    def get_image(self):
        return self._image

    def get_sound_effect(self):
        return self._sound_effect

    def get_inventory(self):
        return self._inventory
    
    def get_knight_status(self):
        return self._knight_status

    def get_dark_deeds(self):
        return self._dark_deeds

    def get_holy_deeds(self):
        return self._holy_deeds

    def get_lawsuits(self):
        return self._lawsuits

    def get_headbutts(self):
        return self._headbutts

    def get_friends(self):
        return self._friends

    def has_friend(self, friend_name):
        return any(friend.get_name() == friend_name for friend in  self._friends)

    def has_item(self, item_name):
        return item_name in self._inventory

    def get_item(self, item_name):
        return self._inventory[item_name]

    def get_magic_power_sum(self):
        return functools.reduce(lambda sum,item: sum + (self._inventory[item].get_magic_level().value if item != self.CAT else 0), self._inventory, 0)

    def add_inventory_item(self, item_name):
        self._inventory[item_name] = self.EXTRA_INVETORY_ITEMS.get(item_name)
    
    def set_knight_status(self, knight_status):
        self._knight_status = knight_status

    def increase_dark_deeds(self):
        self._dark_deeds += 1

    def increase_holy_deeds(self):
        self._holy_deeds += 1

    def increase_headbutts(self):
        self._headbutts += 1

    def increase_lawsuits(self):
        self._lawsuits += 1

    def add_friend(self, friend):
        self._friends.append(friend)
