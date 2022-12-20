import random


class InventoryItem:

    def __init__(self, name, image_path, min_damage, max_damage, magic_level):
        self._name = name
        self._image_path = image_path
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._magic_level = magic_level

    def get_name(self):
        return self._name

    def get_image_path(self):
        return self._image_path

    def get_magic_level(self):
        return self._magic_level

    def get_attack_damage(self):
        return random.randint(self._min_damage, self._max_damage)
        