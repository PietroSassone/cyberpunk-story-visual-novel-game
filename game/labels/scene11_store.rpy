define cultist = Character("Cultist", color = "#555421")
define cashier = Character("Cashier", color = "#dad9b7")


label in_the_store:
    hide screen CityMap
    show bg store
    
    narrator "You're here at the store."
    play music "audio/free_Hardware_No_Copyright.mp3"

    narrator "You've luckily managed to buy the cat for your computer. Finally something that was easy!"

    $purchased_cat = True
    $player_character.add_inventory_item(CAT)

    narrator "Once more, a strange man grabs your attention."

    show cultist at right:
        zoom 2.0

    cultist "My dude, you've got a minute to talk about our Lord?"
    cultist "I'm talking about tha Antipope of course. Yes. He is here."
    cultist "The head of the Anti-church. If you were not afraid yet, you'd better start being afraid now!"

    show cashier man at left:
        zoom 2.5
    cashier "Don't listen to this lunatic! He's been talking nonesense around this part of the town all day."
    cashier "Antipope, of course... Bs. These sects have really gotten out of hand."
    hide cashier man

    cultist "It is true!"
    cultist "He's waiting for you in the small abandoned techno-communist nihilistic church by the docks."

    menu cultist_choice:
        "Fine, I'll listen to what you want to say.":
            jump cultist_info

        "<Run away. I've had enough of this craze for today.>":
            narrator "So you sprint out of the store."
            cultist "Hey! I haven't finished talking to you man!"
            cultist "Fine. Run away! You'll be haring from my lawyer!"
            $player_character.increase_lawsuits()
            
            if enough_lawsuits_for_jail():
                hide cultist
                jump jail

        "{color=#fa510e}<Dark Knight> <Scare this lunatic>{/color}" if is_dark():
            narrator "Being a Dark Knight has granted you the aura to scare this \"Dark\" cultist."
            narrator "You look at him very threateningly and intensely. Let's show him who's really dark!"
            narrator "After a minute of this, the cultist shrinks to the ground from the weight of your gaze."

            cultist "Ah, no more! Don't look at me with those angry eyes!"
            cultist "I'm out of here, this isn't worth it. Forget that you've ever seen me!"

            $player_character.increase_dark_deeds()

            narrator "As a bonus, the man has left some grenades behind in his hurry. Looks like these are some cat AIDS grenades from the black market."
            $player_character.add_inventory_item(GRENADE)

        "{color=#fcff37}<Holy Knight> You have no power over me, evil spawn! I cast you out!{/color}" if is_holy():
            narrator "Being a Holy Knight has granted you the clarity to rise above the evil man's bad energies."
            narrator "You grab a torchlight and shine all your Holyness on the cultist."
            narrator "As a Holy man, you must cleanse the world of wickedness. You tell him, evil has no power to scare you."

            narrator "He wimpers and falls to the ground under the weight of your glorious gaze."
            cultist "Okay, okay!"
            cultist "Please, no more! I'll be good, I swear! I won't serve the Antipope anymore! Just don't look at me so angrily!"
            narrator "You have cast out the wickedness from his heart. Another victory."

            $player_character.increase_holy_deeds()
    
    hide cultist
    jump ambush

label cultist_info:
    cultist "Fire and blood will rain soon. The city will tremble before his might."
    cultist "Why I'm telling you this, you might ask?"

    cultist "The Lord has sent me here. He's been watching the Dark Knights and the Holy Knights, who've been watching you."
    cultist "He's offering you one chance to be his slave willfully. I suggest you take this chance. He'll enslave everyone eventually anyway."
    cultist "As a token of my goodwill, here, take these special grenades. Instead of spreading death, it spreads cat AIDS."
   
    $player_character.add_inventory_item(GRENADE)
    hide cultist

label ambush:
    show bg outside store
    narrator "You step outside the store."
    if not girl_disarmed:
        show girl at right:
            zoom 2.0

        girl "Surprise! Didn't expect to see me again, right?"
        girl "You seem too well off. This is just not okay."

        narrator "Looks like the girl is not so innocent after all. Also, she has a rocket launcher."

        if player_character.get_inventory().get(RIGHT_SHOE) == None:
            girl "You thought you've made my life better with that one shoe? I wan't the other one as well. Give it to me!!!"
        else:
            girl "Selfish bastard! You haven't spared a shoe for me earlier. Well, you'll have to give both of your shoes now!"

        if is_rich():
            girl "I prey on rich folk like you! You're being robbed!"

        menu girl_ambush:
            "Oh my! Take the shoe, just don't kill me!":
                girl "Haha! Thanks4 So long, you fool!"
                $player_character.get_inventory().pop(LEFT_SHOE)
                $player_character.get_inventory().pop(RIGHT_SHOE)
                narrator "She takes off, leaving you barefooted."
              
            "{color=#fa510e}<Dark Knight> I don't hive time for this. <Knock her out>{/color}" if is_dark():
                narrator "Being a Dark Knight has granted you the recklessness to knock out this evil girl."
                play sound girl_char.get_sound_effect()

                narrator "Just like that."
                narrator "She runs away, shouting very vulgaaric insults at you. Also something about a lawsuit."

                $player_character.increase_dark_deeds()
                
            "{color=#f00}Please. I'm a cyber squirrel. That toy rocket launcher won't hurt me.{/color}" if is_squirrel():
                narrator "She realises her mistake. She doesn't want to be headbutted to an other dimension."
                girl "Alright... Different offer. I'll be your friend! I'll help you spread chaos!"
                
                $player_character.add_friend(girl_char)

            "{color=#fcff37}<Holy Knight> <Excorcise the girl>{/color}" if is_holy():
                narrator "Being a Holy Knight has granted you the ability to excorcise the girl."
                narrator "The girl has seriously swayed from the right path. But it is not her fault."
                narrator "It's the fault of the demons posessibng her. Most likely."
                narrator "I cast you out, evil spirit! Leve this innocent girl!"

                narrator "Nothing seems to be happening."
                narrator "Exorcizamus te, omnis immundus spiritus!"
                narrator "Then you spray some holy water in her eyes."

                girl "Oaaaoooaah! Make it stop! Aaah!"
                play sound girl_char.get_sound_effect()
                girl "I'm calling my lawyer!!!"

                narrator "She runs away, rubbing her eyes. You've successfully cleansed her soul!"
                narrator "Or maybe it was just the water you prayed in her eyes. It's a victory either way."

                $player_character.increase_lawsuits()
                $player_character.increase_holy_deeds()
                
                if enough_lawsuits_for_jail():
                    hide girl
                    jump jail

        narrator "You're done here."
        hide girl

    else:
        "Nothing else is interesting here. Time to move on."
    
jump city_center
