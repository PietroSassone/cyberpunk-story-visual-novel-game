define enemy_attack_types = {
    1: ['He bites your feet!', 10, 40],
    2: ['He pisses on your feet!', 20, 50],
    3: ['He rubs his used toy ball to your feet!', 30, 65]
}

label boss_fight:
    $self_hp = 500
    $antipope_hp = 500
    show screen BossFight
    jump enemy_attacks

label enemy_attacks:
    if antipope_hp > 0 and self_hp > 0:
        $attack_tpye = renpy.random.randint(1, 3)
        $narrator_message = enemy_attack_types.get(attack_tpye)[0]

        narrator "[narrator_message]"
        $feet_damage = renpy.random.randint(enemy_attack_types.get(attack_tpye)[1], enemy_attack_types.get(attack_tpye)[2])
        
        if RIGHT_SHOE not in player_character.get_inventory():
            narrator "You take increased damage because you've lost your right shoe."
            $feet_damage *= 2

        if LEFT_SHOE not in player_character.get_inventory():
            narrator "You take increased damage because you've also lost your left shoe."
            $feet_damage *= 3
     
        $self_hp -= feet_damage
        narrator "Damage taken from feet attack: [feet_damage]"

        jump fight_choice

    hide screen BossFight

    if antipope_hp <= 0:
        narrator "You did it!"
        jump victory
    else:
        narrator "You failed to defeat him. Your adventures have come to a tragic end."
        hide antipope
        jump ending_defeat
    
label fight_choice:
    $success = renpy.random.randint(1, 3)
    $damage_done = 0
    menu choose_attack_type:
        "Attack on your own.":      
            jump hit_attack

        "Choose inventory item for attack.":      
            jump item_attack

        "Ask friend for help.":      
            jump ally_attack

label player_attack_success_check:
    if success in [1,2]:
        antipope "Hey!"
    elif damage_done > 0:
        antipope "Hehe, too slow!"
        narrator "The cheeky bastard is quick, you missed him."
        $damage_done = 0
    
    $antipope_hp -= damage_done
    narrator "Damage done: [damage_done]"

    if damage_done > 0:
        play sound "audio/cartoon_scream.mp3"

    jump enemy_attacks

label hit_attack:
    menu simple_attack:
        "Hit him.":
            $damage_done = renpy.random.randint(1, 20)

        "{color=#f00}Hit him hard.{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            $damage_done = renpy.random.randint(10, 40)

        "{color=#34b2e47f}Hit him with a high school mathematics excercise book.{/color}" if is_shaman():
            play sound player_character.get_sound_effect()
            $damage_done = renpy.random.randint(20, 40)

        "{color=#e717a2}I'm rich. I'll just heal myself.{/color}" if is_rich():
            play sound player_character.get_sound_effect()
            $damage_done = 0
            $healing = renpy.random.randint(40, 70)
            $self_hp += healing

            narrator "[healing] health regenerated."

        "Back":
            jump fight_choice

    jump player_attack_success_check
        
label item_attack:
    menu inventory_attack:
        "Throw the bag of chips at him." if player_character.has_item(CHIPS):
            antipope "Aaaagh, gluten! Nooo!"
            narrator "He's allergic to gluten it seems. You've knocked him out instantly."
            $success = 1
            $damage_done = player_character.get_item(CHIPS).get_attack_damage()

        "Eat the chips for extra health." if player_character.has_item(CHIPS):
            $damage_done = 0
            $healing = player_character.get_item(CHIPS).get_attack_damage()

            $self_hp += healing
            narrator "[healing] health regenerated."
            $player_character.get_inventory().pop(CHIPS)

        "Throw a cat AIDS grenade at him." if player_character.has_item(GRENADE):
            antipope "Lol. I'm a doggy, that doesn't work against me!"
            $player_character.get_inventory().pop(GRENADE)
            $damage_done = 0

        "Throw the zombie arm at him." if player_character.has_item(ZOMBIE_ARM):
            antipope "Eww, gross!"
            $damage_done = player_character.get_item(ZOMBIE_ARM).get_attack_damage()
            $player_character.get_inventory().pop(ZOMBIE_ARM)

        "Shoot him with the death ray of the thechno chicken feather." if player_character.has_item(CHICKEN_FEATHER):
            antipope "That's not fair!"
            $damage_done = player_character.get_item(CHICKEN_FEATHER).get_attack_damage()

        "Chainsaw go bo brrrr!" if player_character.has_item(CHAINSAW):
            $damage_done = player_character.get_item(CHAINSAW).get_attack_damage()

        "Back":
            jump fight_choice
    
    jump player_attack_success_check

label ally_attack:
    menu friend_attack:
        "[clown_char._ability]" if player_character.has_friend(PSYCHO_CLOWN):
            play sound clown_char.get_sound_effect()
            show clown at left:
                zoom 2.0

            clown "Nyghehehe!"

            $damage_done = clown_char.get_attack_damage()
            hide clown with moveoutleft
        
        "[girl_char._ability]" if player_character.has_friend(GIRL):
            play sound girl_char.get_sound_effect()
            show girl at left:
                zoom 2.0

            girl "How you like that? He?!"

            $damage_done = girl_char.get_attack_damage()
            hide girl with moveoutleft

        "[old_char._ability]" if player_character.has_friend(OLD_LADY):
            play sound old_char.get_sound_effect()
            show old_lady shocked at left:
                zoom 2.0
        
            old_lady "Naughty doggo!"

            $damage_done = old_char.get_attack_damage()
            hide old_lady with moveoutleft

        "[politician_char._ability]" if player_character.has_friend(POLITICIAN):
            play sound politician_char.get_sound_effect()
            show politician at left:
                zoom 2.0
            
            politician "I'm counting on your vote! I won't steal from you, I promise!"

            $damage_done = politician_char.get_attack_damage()
            hide politician with moveoutleft

        "[protester_char._ability]" if player_character.has_friend(STREET_PROTESTER):
            play sound protester_char.get_sound_effect()
            show protester at left

            protester "Down with the system! Down with everybody! Anarchy!!!"

            $damage_done = protester_char.get_attack_damage()
            hide protester with moveoutleft

        "[chicken_char._ability]" if player_character.has_friend(TECHNO_CHICKEN):
            play sound chicken_char.get_sound_effect()
            show chicken at left:
                zoom 2.0

            chicken "Being evil does have it's price. This is that price."

            $damage_done = chicken_char.get_attack_damage()
            hide chicken with moveoutleft

        "[hobo_char._ability]" if player_character.has_friend(HOBO):
            play sound hobo_char.get_sound_effect()
            show hobo at left:
                zoom 2.0

            hobo "What am I actually doing here???"

            $damage_done = hobo_char.get_attack_damage()
            hide hobo with moveoutleft

        "Back":
            jump fight_choice

    jump player_attack_success_check
