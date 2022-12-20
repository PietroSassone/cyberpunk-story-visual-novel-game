define zombie = Character("Zombie", color = "#a3a107")


label inner_park:
    show bg park inner
    hide screen CityPark
    show screen CityParkInner
    narrator "Arrived at the heart of the park. Look around, or go back to the map if there's nothing else here."
    jump inner_park

label defeat_zombie:
    hide screen CityParkInner
    show zombie_idle at right:
        zoom 2.0
    narrator "Looks like you bumped into a zombie!"
    narrator "Indeed, right here in the middle of the park! Surrounded by happy families walking their kids, not really being bothered by the zombie."
    narrator "Beware, it wants to eat your brain!"

    play sound zombie_voice

    menu zombie_fight:
        "Holy s**t, I'll just run away.":
            narrator "So you ran away."

        "Knock it out!":
            zombie "Hraaaargh!!!"
            narrator "So you punch it hard. The zombie falls down, unconscius."

        "{color=#f00}<Headbutt the zombie into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            hide zombie_idle
            narrator "You headbutted it so hard, I can't even describe how hard!"

            $player_character.increase_headbutts()

            if headbutted_too_much():
                jump other_dimension

        "{color=#34b2e47f}<Try to talk about some intellectual topic. Maybe the zombie just wants to talk?>{/color}" if is_shaman():
            narrator "So you start to question it about Newton's first law."
            play sound player_character.get_sound_effect()

            narrator "It seems to stop. Looks like it's trying really hard to think."
            zombie "Wuh... Hrrr... Hmmmraaarhg..."
            narrator "Then it passes out from the effort and the strain it put on it's brain."
        
        "{color=#e717a2}I'm rich. I'll pay if you leave me alone.{/color}" if is_rich():
            play sound player_character.get_sound_effect()
            narrator "Well, it looks like the zombie doesn't understand what you're saying. It doesn't care."
            
            zombie "Sheeeesh..."

            narrator "It tries to eat your brain. But you're rich. You're above things like this, so it doesn't succeed."
            narrator "The zombie just sadly crawls away."
        
    play sound zombie_voice

    hide zombie_idle

    narrator "In the meanwhile the zombie dropped it's arm. You pick it up and put it in your inventory."
    narrator "Who knows, it may come in handy later."
    
    $player_character.add_inventory_item(ZOMBIE_ARM)

    narrator "After the initial scare wears down, you realize an even more interesting fact."
    narrator "It wasn't even a zombie, not really."
    narrator "It was just an average teenager who's brain started rotting after spending too much time on his phone."
    narrator "Also, he didn't want to eat your brain. He just desperately needed a phone charger. Well, nevermind."

    $defeated_zombie = True

    jump inner_park
