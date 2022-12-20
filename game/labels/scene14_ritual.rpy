label ritual:
    show bg alley
    stop music fadeout 3.0
    
    narrator "You've gathered your stuff and went into the rundown alley between two office buildings."
    narrator "You know, because there's no better place to complete a wild ritual than a rundown alley between two marketing office buildings."
    narrator "That piece of broken furniture will be a perfect altar. Yes, that piece of junk in the middle, on the ground."
    narrator "Oh, about the ritual, yes. You and Lizzy read about it earlier on one of her favourite conspiracy theorist sites."
    narrator "If you do your magic mumbo-jumbo correctly, you can summon the interdimensional goat. He's some benevolent deity, who will surely fix the problems of the world."
    narrator "Totally legit."

    narrator "The only problem is that you don't really remember how to do the ritual properly. Let's try it anyway."
    
    $show_magic_level = True

    play music "audio/Infraction_No_Copyright_Music_It_Follows.mp3"

    narrator "You'll have to achieve a certain magic energy level to make it succeed, that's for sure."
    narrator "Your inventory items luckily all have some magic energy! Convenient, right?"
    narrator "Let's see how well you did today. Check your inventory now!"

    narrator "Yes."

    $total_magic_level = player_character.get_magic_power_sum()

    narrator "Looks like based on your items, you have a total magic power of [total_magic_level]. We don't count the cat. For obvious reasons."

    show screen MagicLevel

    narrator "I don't know whether you trust me at this point as reality starts to fall apart. But I'd advise to gather a magic level that's between 25-30. Boundaries are included."
    narrator "You'll have 3 chances to say magic phrases to modify your magic level."

    narrator "Hopefully you've gathered some friends along the way, otherwise who would give you hints now about the ritual?"
    
    if len(player_character._friends) > 0:
        $show_friend_hints = True
        narrator "You friends can provide you with some suggestions of their own. Check the new menu on the right."
        narrator "It is up to you whether you trust these guys..."

    $iteration = 3

    while iteration > 0:
        narrator "[iteration] more rounds of spellcasting left."
        menu ritual_first_choice:
            "Bella ciao.":
                $total_magic_level += 0

            "Abracapocus.":
                $total_magic_level -= 5

            "String String = \"**********\"":
                $total_magic_level += 5

            "Ihn nikho! Mahna nikho mha nahna e rei!":
                $total_magic_level += 10

            "Sacrifice the cat" if player_character.has_item(CAT):
                $total_magic_level += player_character.get_item(CAT).get_magic_level().value
                $player_character.get_inventory().pop(CAT)
        $ iteration -=1

    hide screen MagicLevel
    if total_magic_level > 30:
        narrator "Something's not right..."
        jump ending_cthulhu
    elif total_magic_level < 25:
        narrator "It seems like you didn't collect enough magical energy. The ritual has failed."
        narrator "<Sigh> Nothing else can be done it seems. You've at least tried. Let's just go home. Then you better flee the city."
        jump ending_home

    jump ending_goat
