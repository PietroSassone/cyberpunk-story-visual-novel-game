define old_lady = Character("Old lady", color = "#ff0296")
define audio.explosion = "audio/explosion.mp3"


label on_subway:
    scene bg subway_int with fade
    
    if not banker_disarmed:
        jump subway_surprise
    else:
        jump subway_lady

label subway_surprise:
    show banker angry at right

    narrator "Suddenly you're faced with the angry banker from before."

    banker "Surprise b***h! You didn't give me smokes, prepare for the consequences!"

    narrator "He's got a pocket nuke..."
    play sound nuclear_alarm

    menu subway_threat:
        "Calm down man... I'll give you those nonexistent smokes. Here!":
            banker "Too late, now I'm angry!"
            narrator "Game over..."
            
            scene bg explosion with hpunch
            hide banker with fade
            
            play sound explosion
            play sound scream
            
            pause
            call screen Credits

        "{color=#e717a2}I'm rich. I don't have to die with the plebs here.{/color}" if is_rich():
            play sound player_character.get_sound_effect()
            narrator "The bomb blows up. The whole subway is destroyed, with everyone on board."
            
            scene bg explosion with hpunch
            play sound explosion
            play sound scream

            narrator "The explossion will be seen from quite far..."
            
            hide banker with fade
            
            narrator "But you go on without a scratch.\nYou're rich. The laws of physics don't apply to you."
            
            narrator "Unforunately the subway is completely ruined. You'll just have to go on by foot, before the cops arrive."
            narrator "Which won't happen for a while. Nowadays scenes like this are common. Everybody's used to them."

            jump central_station

        "{color=#34b2e47f}<With your impressive hacking skills, disarm the bomb>{/color}" if is_shaman():
            narrator "Hacking..."
            narrator "Breaching firewall..."
            narrator "The guy takes a smoke break..."
            narrator "The ICE is thicker than expected..."
            narrator "Finally you manage to DDOS the bomb's computer system with 3 zetabytes of cute cat videos.\nCrisis averted."
            narrator "The man looks surprised. He wasn't expecting this."
            play sound player_character.get_sound_effect()

            banker "Ah, screw it. Maybe next time."
            narrator "He steps aside, peacefully continuing the journey."
            hide banker

            jump subway_lady
        
        "{color=#34b2e47f}<Talk to the bomb about some psychology>{/color}" if is_shaman():
            play sound player_character.get_sound_effect()
            narrator "So you ask the bomb about it's personal opinion about all of this."
            narrator "It's happy that someone finally listens to his problems."
            narrator "It starts to talk about how it's life is messed up after it got into a serious fight with it's wife."
            narrator "It's marriage is in ruins. The wife took the kids."
            narrator "So the bomb is happy that you talked to it, but it doesn't see a way out of this. So it still blows up."

            scene bg explosion with hpunch
            play sound explosion
            hide banker with fade
            play sound weird_scream
            narrator "Game over..."
            call screen Credits

        "{color=#f00}<Headbutt the nuclear device.>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            pause 3.0
            scene bg explosion with hpunch

            play sound explosion
            hide banker with fade
            play sound weird_scream

            narrator "My dude, this wasn't the brightest idea... This was a weapon of mass destruction after all."
            narrator "Game over..."
            call screen Credits

        "{color=#f00}<Headbutt the man to another dimension.>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            pause 3.0

            $player_character.increase_headbutts()

            hide banker with fade
            play sound omg

            narrator "Well... Crisis averted!"

label subway_lady:
    narrator "On the subway, there's only one free seat left.\nYou're on your way towards it..."
    narrator "But you're not the only one with eyes for it."
    
    show old_lady chill at right:
        zoom 2.0

    narrator "A sour, evil looking old lady looks at you with signature look of superiority."

    old_lady "Don't even think about it my dude! You youngsters are so disrespectful!"
    old_lady "Back in my day you wouldn't even have been worthy to get on the subway..."
    old_lady "This seat is made for my royal butt only."

    menu subway_seat:
        "I've got no choice but to accept the wisdom in her words.":
            old_lady "Told ya. Ha!"
            narrator "She smiles smugly, looking at you with contempt and with even bigger signature superiority."

        "Try to negotiate for the seat.":
            old_lady "No way you little devilspawn!"
            narrator "She growls at you victoriously, looking at you with contempt and with even bigger signature superiority."
            narrator "She takes the seat."

        "{color=#e717a2}I'm rich. I'll pay for the seat.{/color}" if is_rich():
            play sound player_character.get_sound_effect()
            narrator "She looks at you with newfound respect and gives you the seat.\nWith agility that would make young people jealous."
            old_lady "Why didn't you start with that, dearie? Call me Cherie. Let's be friends!"
            narrator "You become instant friends."
            $player_character.add_friend(old_char)

        "{color=#34b2e47f}<Talk to her about some philosophy. Is the seat even real?>{/color}" if is_shaman():
            play sound player_character.get_sound_effect()
            old_lady "Oh my! You're so intellectual. I had no idea!"
            narrator "Says the old lady with happy tears in her eyes."
            narrator "She shows you photographs of her grandchildren and you become instant friends."
            $player_character.add_friend(old_char)
        
        "{color=#fa510e}<Dark Knight> Nah, I'll shove her aside and take the place all for myself.{/color}" if is_dark():
            narrator "Being a Dark Knight has granted you the strenght to unleash your inner...\nWell, darkness."
            narrator "You finally broke free from the constraints of society and ethics. So illuminating!"

            play sound old_char.get_sound_effect()

            show old_lady shocked at right:
                zoom 2.0

            narrator "The old lady is shocked by your lack of respect."
            old_lady "You'll be hearing from my lawyer!!!"
            narrator "Then she passes out from the outrage."

            $player_character.increase_lawsuits()
            $player_character.increase_dark_deeds()
        
    hide old_lady with dissolve

jump central_station    
