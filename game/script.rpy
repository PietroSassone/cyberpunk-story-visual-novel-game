define narrator = Character("Narrator", color = "#8b7808")

define audio.omg = "audio/omg.mp3"
define audio.scream = "audio/scream.mp3"
define audio.weird_scream = "audio/weird_scream.mp3"
define audio.evil_shriek = "audio/evil_shriek.mp3"
define audio.zombie_voice = "audio/zombie_voice.mp3"
define audio.nuclear_alarm = "audio/nuclear_alarm.mp3"
define audio.riot_song = "audio/free_ncs_Crime.mp3"
define audio.ending_song = "audio/Independence_No_Copyright_Music_Take_My_Heart_and_Burn_It_Down.mp3"
define audio.bad_ending_song = "audio/Suspense_by_Infraction_No_Copyright_Music_Psycho.mp3"

define CYBER_SQUIRREL = 'Cyber Squirrel'
define RICH_PERSON = 'Rich Person'
define TECHNO_SHAMAN = 'Techno Shaman'

define DARK = 'DARK'
define HOLY = 'HOLY'

define LEFT_SHOE = 'Left shoe'
define RIGHT_SHOE = 'Right shoe'
define MUG = 'Mug'
define CHICKEN_FEATHER = 'Chicken feather'
define CHIPS = 'Chips'
define ZOMBIE_ARM = 'Zombie arm'
define CHAINSAW = 'Chainsaw'
define CAT = 'Cat'
define GRENADE = 'Grenade'

define GIRL = 'Girl'
define PSYCHO_CLOWN = 'Psycho Clown'
define TECHNO_CHICKEN = 'Techno chicken'
define OLD_LADY = 'Cherie the old lady'
define POLITICIAN = 'Politician'
define STREET_PROTESTER = 'Street protester'
define HOBO = 'Hobo'


# The game starts here.
label start:
    play music "audio/Hyperloop_license_free.mp3"
    call screen CharacterSelector

    init python:
        from model.player import Player
        from model.friend import Friend

        CORRECT_HINT_COMMON_PART = 'The first magic word decreases the power by five. The second increases it by five. The third increases it by 10.'

        player_character = None
        show_hints = False
        show_magic_level = False
        show_friend_hints = False

        clown_char = Friend(PSYCHO_CLOWN, '{color=#ec49e4}Clown ally attack: tell terrible jokes.{/color}', 25, 35, '#ec49e4')
        old_char = Friend(OLD_LADY, '{color=#ff0296}Old lady ally attack: beat the enemy with some canned catfood.{/color}', 50, 70, '#ff0296')
        girl_char = Friend(GIRL, '{color=#f010b8}Girl ally attack: rocket launcher.{/color}', 35, 45, '#f010b8')
        chicken_char = Friend(TECHNO_CHICKEN, '{color=#1b138a}Chicken ally attack: peck peck.{/color}', 100, 150, '#1b138a')
        politician_char = Friend(POLITICIAN, '{color=#756763}Politician ally attack: long boring speech.{/color}', 10, 50, '#756763')
        protester_char = Friend(STREET_PROTESTER, '{color=#d40000}Protester ally attack: throw molotov cocktails.{/color}', 0, 80, '#d40000')
        hobo_char = Friend(HOBO, '{color=#79ac81}Hobo ally attack: throw dirty napkins.{/color}', 10, 40, '#79ac81')

        def is_squirrel():
            return player_character.get_class_name() == CYBER_SQUIRREL

        def is_shaman():
            return player_character.get_class_name() == TECHNO_SHAMAN

        def is_rich():
            return player_character.get_class_name() == RICH_PERSON

        def is_dark():
            return player_character.get_knight_status() == DARK

        def is_holy():
            return player_character.get_knight_status() == HOLY

        def unlock_antipope_ending():
            return player_character.get_dark_deeds() >= 3 or player_character.get_holy_deeds() >= 3

        def enough_lawsuits_for_jail():
            return player_character.get_lawsuits() >= 3

        def headbutted_too_much():
            return player_character.get_headbutts() >= 5


label start_squirrel:
    $player_character = Player(CYBER_SQUIRREL)
    jump apartment

label start_shaman:
    $player_character = Player(TECHNO_SHAMAN)
    jump apartment

label start_rich:
    $player_character = Player(RICH_PERSON)
    jump apartment
