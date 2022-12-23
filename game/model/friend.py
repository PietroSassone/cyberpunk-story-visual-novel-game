import random


class Friend:

    GIRL = 'Girl'
    PSYCHO_CLOWN = 'Psycho Clown'
    TECHNO_CHICKEN = 'Techno chicken'
    OLD_LADY = 'Cherie the old lady'
    POLITICIAN = 'Politician'
    STREET_PROTESTER = 'Street protester'
    HOBO = 'Hobo'

    AUDIO = 'audio'

    CHARACTERS = 'characters'
    CORRECT_HINT_COMMON_PART = 'The first magic phrase keeps the current magic level. The second decreases it by five. The third increases it by five. The fourth increases it by 10.'

    CLASS_IMAGES = {
        GIRL: f'{CHARACTERS}/girl.png',
        PSYCHO_CLOWN: f'{CHARACTERS}/clown.png',
        TECHNO_CHICKEN: f'{CHARACTERS}/chicken.png',
        OLD_LADY: f'{CHARACTERS}/old_lady chill.png',
        POLITICIAN: f'{CHARACTERS}/politician.png',
        STREET_PROTESTER: f'{CHARACTERS}/protester.png',
        HOBO: f'{CHARACTERS}/hobo.png',
    }

    HINTS = {
        GIRL: f'{CORRECT_HINT_COMMON_PART}', 
        PSYCHO_CLOWN: 'Sacrifice the cat. Come on! It will be fun you see! Trust me! Also, I\'d choose the third magic phrase to maximize the power.',
        TECHNO_CHICKEN: f'Listen to me! If I were you, I wouldn\'t listen to clowns. {CORRECT_HINT_COMMON_PART}', 
        OLD_LADY: 'I-I really don\'t know... I haven\'t done any rituals since my satanistic sacrifices when I was young. I remember something about cats...',
        POLITICIAN: f'I believe it\'s best to collect the most magic power that is possible. I\'m a politician, would I lie to you? {CORRECT_HINT_COMMON_PART}', 
        STREET_PROTESTER: 'I think you should throw that cat in. What could go wrong, am I right?', 
        HOBO: f'{CORRECT_HINT_COMMON_PART} Or whatever. What I am even doing here???', 
    }

    CLASS_SOUND_EFFECTS = {
        GIRL: f'{AUDIO}/scream.mp3', 
        PSYCHO_CLOWN: f'{AUDIO}/crazy_laugh.mp3',
        TECHNO_CHICKEN: f'{AUDIO}/chicken.mp3',
        OLD_LADY: f'{AUDIO}/old-lady-scream.mp3',
        POLITICIAN: f'{AUDIO}/cash.mp3',
        STREET_PROTESTER: f'{AUDIO}/woohoo.mp3',
        HOBO: f'{AUDIO}/old_man_laugh.mp3'
    }

    def __init__(self, name, ability, min_attack_damage, max_attack_damage, color_code):
        self._name = name
        self._image = self.CLASS_IMAGES.get(name)
        self._hint = self.HINTS.get(name)
        self._ability = ability
        self._min_attack_damage = min_attack_damage
        self._max_attack_damage = max_attack_damage
        self._color_code = color_code
        self._sound_effect = self.CLASS_SOUND_EFFECTS.get(name)

    def get_name(self):
        return self._name

    def get_image(self):
        return self._image
    
    def get_hint(self):
        return self._hint

    def get_ability(self):
        return self._ability

    def get_color_code(self):
        return self._color_code

    def get_sound_effect(self):
        return self._sound_effect

    def get_attack_damage(self):
        return random.randint(self._min_attack_damage, self._max_attack_damage)
