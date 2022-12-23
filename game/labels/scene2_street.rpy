define banker = Character("Banker", color = "#c5140d")
define girl = Character("Girl", color = "#f010b8")
define audio.sparta = "audio/this-is-sparta.wav"
define audio.omg = "audio/omg.wav"
define audio.shut_up = "audio/shut-up.wav"
define audio.scream = "audio/scream.mp3"
define audio.weird_scream = "audio/weird_scream.mp3"
define girl_disarmed = False


label street:

    play music "audio/chill_bg_music_license_free.mp3"
    
    scene bg elevator with fade

    narrator "So you leave your apartment and descend the elevator. Time to head down the street."

    scene bg street with fade

    narrator "The weather's nice around here. Just another beautiful day in a beautiful city."

    narrator "So you're making your way towards the subway station on the corner."
    narrator "When suddenly a man steps in your way."

    show banker at left
    
    banker "Hey my dude! Don't be alarmed. I'm just an average banker. Totally legit. Really!"
    banker "So you've got some cigarettes for me?"

    $banker_disarmed = False

    menu banker_on_the_street:

        "Nope, I don't.":
            
            show banker angry at left:
                
            banker "F*** you."
            narrator "The man seems angry. He struts off towards the subway station."
            hide banker angry with moveoutright

        "Lol. I don't but I'll give it to you. Here you go!":
            
            narrator "You pretend like you're handing over something to the man.
                        He takes the nothing. He looks pleased."
            narrator "Kids, remember this: smoking is unhealthy."

            banker "Wise man!"
            narrator "He leaves."

            $banker_disarmed = True

            hide banker with moveoutright

        "{color=#f00}<Headbutt the man into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()

            hide banker with fade
            play sound omg

            narrator "Well... That was something!"
            narrator "The guy just disappeared, who knows if he'll ever be found again!"
            $banker_disarmed = True
            $player_character.increase_headbutts()

    jump street_surprise

label street_surprise:
    narrator "So you keep walking.
                When suddenly an innocent looking ragged little girl steps in your way."

    show girl at right:
        zoom 2.0
    girl "O kind sir! I'm a poor little homeless girl. Would you be so kind to give me half of your shoes?"

    menu girl_on_the_street:

            "Wut? No no, sorry I can't give you the half pair of my shoes.":
                
                girl "F*** you. I won't forget this."
                narrator "The girl seems angry. She leaves."
                narrator "You continue your walk with both shoes protecting your little feet."

            "Of course. Here you go, one shoe.":
                
                narrator "You hand over half of your pair of shoes.
                            She takes it. But instead of looking pleased she looks strangely at you."
                narrator "Almost like with a creepy greedy look."

                girl "Thank you O good sir! I won't forget this."
                narrator "She leaves. But for some reason you don't feel relieved."
                narrator "You continue your walk with only one shoe."
                
                $player_character.get_inventory().pop(RIGHT_SHOE)

            "{color=#e717a2}I'm rich. I don't have to talk to you.{/color}" if is_rich():
                play sound player_character.get_sound_effect()
                girl "Oh. Ok."
                narrator "Unable to resist your power, the girl shrinks away."

            "{color=#f00}Don't make me headbutt you to another dimension!{/color}" if is_squirrel():
                narrator "She realises you're a cyber squirrel, who can headbutt people to other dimensions."
                girl "Oh my! That puts things into a different perspective. Keep the shoe. I'll work for you instead!"
                girl "You look like a strong person. I'll be your friend! Hopefully that means the chance to loot more shoes!"
                $girl_disarmed = True
                $player_character.add_friend(girl_char)

            "{color=#f00}<Headbutt the girl into another dimension>{/color}" if is_squirrel():
                play sound player_character.get_sound_effect()
                pause 3.0

                hide girl with fade
                play sound girl_char.get_sound_effect()

                narrator "Holy s**t!"
                narrator "Poor girl!"
                $girl_disarmed = True
                $player_character.increase_headbutts()

    hide girl with moveoutright

    jump subway_station
    