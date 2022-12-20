define dark_man = Character("Dark Man", color = "#fa510e")


label subway_station:
    scene bg subway with fade
    narrator "Anyway. You enter the subway station."
    narrator "The air is filled with the smell left by the thousands of humans crowded here everyday, rotting piles of trash, and some rats."

    narrator "You make your way towards the subway that will take you to the city center."

    narrator "Suddenly a man steps in front of you."
    narrator "What is with people, right? They just can't seem to let you be. You're here minding your simple business.
                \nYet someone always finds you with something. *Sigh*"

    show dark knight at right
    dark_man "I greet you. I am a Dark Knight"
    dark_man "We've been watching you. Don't act surprised. Deep down you know it."
    dark_man "We've been considering your actions. There's potential in you."
    dark_man "You're granted a one in a lifetime opportunity. You can be one of us."
    dark_man "You'll have a chance to unlock you're potential dark side. You'll have power.
                \nYou will realise that you can get away with letting out your anger."
    dark_man "Make the people fear you. Deep down you know you want this. \nSo will you join the Brotherhood?"
    dark_man "Beware: there's no going back. Your choice will have consequences."

    menu dark_knight_before_subway:

        "No thanks man, I'm not buying anything from you. This sounds fishy.":
            dark_man "Your loss."

        "Why not? What could go wrong?":
            $player_character.set_knight_status(DARK)
            play music "audio/Just_Evil_license_free.mp3"

            dark_man "We'll be watching you."

        "{color=#f00}<Headbutt the man into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            pause 3.0
            play sound omg
            hide dark knight with fade
            $player_character.increase_headbutts()

            narrator "The guy is sucked into the vortex! Maybe you should get your anger issues checked."

    hide dark knight with dissolve
    narrator "In the blink of an eye, the man disappers. What a strange day this is starting to get!"

    narrator "So you get on the crowded subway."

    jump on_subway