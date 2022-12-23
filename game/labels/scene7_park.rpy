define chicken = Character("Techno Chicken", color = "#1b138a")
define hobo = Character("Old hobo", color = "#79ac81")


label park:
    show bg park
    play music "audio/Arc_North_Symphony_feat_Donna_Tella_no_copyright.mp3"
    hide screen CityMap
    hide screen CityParkInner
    show screen CityPark
    show screen MenuUI

    narrator "Arrived at the park."
    jump park

label talk_to_chicken:
    hide screen CityPark
    show chicken at center:
        zoom 2.0
    
    narrator "You see a technologically enhanced cyberpunk chicken just casually picnicking in the park."
    narrator "Don't be surprised! In case you may have forgotten, this is the future. It's a civilized age."
    narrator "Chickens have evolved to be more intelligent than humans by this time."
    narrator "They've got full citizenship and every right that humans have."
    narrator "A chicken is even the current most popular candidate running for president at the moment."
    narrator "One more fun fact in case you are curious."
    narrator "After the chicken revolution 2 years ago, chickens are legally allowed to keep humans as livestock and eat them."
    narrator "You know, just to give them equality in this PC age. When all that matters is equality. It's the age of chickencipation."

    chicken "Greetings my dude! It's always great to see a friendly face. I'm bored. Care to join me for some intellectual discussion?"

    menu chicken:
        "Join the chicken for a casual tea party.":
            chicken "Cool!"
            narrator "So you spend a chill afternoon having picnic with the chicken."
            narrator "You share the finest English black tea."

            show bg park with fade

            chicken "It was real nice talking to you my dude!"
            chicken "I'll have to leave now. But I'll give you gift. Here, take one of my super advanced cyber chicken feathers!"
            chicken "It may come in handy through your journeys."

            $player_character.add_inventory_item(CHICKEN_FEATHER)
            if is_squirrel():
                chicken "I also realized that you're not entirely human, but half squirrel!"
                chicken "This impresses me very much! So I decided that I'll be your friend!"
                $player_character.add_friend(chicken_char)

            chicken "Adios my dude!"

        "{color=#34b2e47f}Sounds great. Let's talk about the meaning of life!{/color}" if is_shaman():
            play sound chicken_char.get_sound_effect()
            chicken "Fantastic, I bumped into a man of culture!"
            narrator "So you spend the afternoon having a picknick with the chicken. Discussing the life, the universe and everything."

            show bg park with fade
            narrator "The chicken really enjoyed your discussion."

            chicken "It was so good talking to someone so intellectual! You restored my faith in humanity!"

            $player_character.add_inventory_item(CHICKEN_FEATHER)

            chicken "You know what? I was going to simply give one of my super advanced cyber chicken feathers."
            chicken "It may come in handy through your journeys. But I'm so impressed that I will even add you to my friends list!"
            chicken "So you can call on me later."
            chicken "Buon pomeriggio my friend!"
            play sound player_character.get_sound_effect()

            $player_character.add_friend(chicken_char)

        "<Attack the chicken. What could go wrong?>":
            play sound chicken_char.get_sound_effect()
            narrator "The chicken activates his built in lethal war machine mode."
            show chicken angry at center:
                zoom 2.0
            
            play sound "audio/why.mp3"
            pause 4.0
            
            chicken "Why on earth would you do that?"

            chicken "Here I was looking for a peaceful chat. Here I am, trying to convince my peers that not all humans are brabarians..."

            narrator "You're lucky this chicken is a peaceful character and he doesn't attack you."
            narrator "You wouldn't stand a chance against his built in military cyberware."

            $player_character.increase_lawsuits()
            chicken "I'll let you live. But you'll be hearing from my lawyer!"

            
            if enough_lawsuits_for_jail():
                hide chicken
                jump jail

    hide chicken
    $talked_to_chicken = True

    jump park

label talk_to_hobo:
    hide screen CityPark

    show hobo at left:
        zoom 2.0
    narrator "You bump into a poor old hobo."

    hobo "Whoa my dude! You stink of soap. Don't come any closer please!"
    hobo "I've got a one time offer for you by the way."
    hobo "You seem a litlle lost. Like someone who's unsure what to do in this game of life. I can help you with that."
    hobo "I see that you've got a nice mug. If you give it to me, I can give you some hints!"
    hobo "Of course you won't be able to use it anymore. But you don't need it anyway, right?"
    hobo "Choose now. I won't be here later!"

    menu hobo_choice:
        "Sure, why not. Here's the mug.":
            $player_character.get_inventory().pop(MUG)
            narrator "The hobo grabs the mug, hugs it happily while drooling and laughing creepily."

            play sound hobo_char.get_sound_effect()
            pause 6.0

            hobo "So precious... Hehe... Hehehe... Nyhehehe..."
            narrator "After a few seconds, he gets himself in order."
            $show_hints = True

            hobo "Hm right, the hints. So at this moment, a little menu option has been added to your retina computer."
            hobo "In the top right corner."
            hobo "So you can check my hints there."
            hobo "So long!"

        "No, sorry. I'll keep my mug and figure life out on my own.":
            hobo "Your loss my child."

        "{color=#f00}<Headbutt the man into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            hide hobo with fade
            play sound omg
            narrator "Well... Okay."
            $player_character.increase_headbutts()

            if headbutted_too_much():
                jump other_dimension

        "{color=#fa510e}<Dark Knight><Instead of handing over anything, threaten him to get the hints>.{/color}" if is_dark():
            narrator "Being a Dark Knight has granted you bravery to threaten the man."
            narrator "You threaten to break all mugs in the city if he won't give you the hints."
            narrator "The poor man looks genuinely scared."

            hobo "All right all right man! No need to be so rude. You can check the hints in the top right corner."
            hobo "Keep your mug, just leave the rest of them alone you wicked person!"
            $player_character.increase_dark_deeds()
            $show_hints = True

        "{color=#fcff37}<Holy Knight> I'll do better than that. I'll convert you to the holy religion!{/color}" if is_holy():
            narrator "You shine your inner holy light on the man, who shrinks to the ground."
            narrator "He looks up to you with a mix of wonder and terror as you preach the holy scripts."

            narrator "His face holds a newfound reverence as he bursts to tears."
            hobo "O my savior! Now I see the light! I shall serve nothing but the holyness in my remaining days!"
            hobo "I don't need mugs anymore. All I need is the holy light, and you've opened my eyes."
            hobo "I'll go on and convert more people in the park, hallelujah!"

            $show_hints = True
            hobo "You can check the hints from now on in the top right corner of your retinal computer!"
            hobo "Also, consider me your friend. I'll come to your side when you need help converting more infidel dogs!"

            $player_character.add_friend(hobo_char)
            $player_character.increase_holy_deeds()

    hide hobo
    $talked_to_hobo = True

    jump park
