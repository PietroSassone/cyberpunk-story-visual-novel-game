define clown = Character("Psycho clown", color = "#ec49e4")
define drank_beer = False
define been_to_toilet = False


label bar:
    hide screen CityMap
    show bg bar
    show screen Bar
    play music "audio/free_Nu_Metal_ArkZion.mp3"
    narrator "At the bar. You could probably use a beer after all this tiring nonsense. Or just leave if you've already done everyithing here."
    jump bar

label order_beer:
    narrator "You drink a nice cold beer. It probably feels good after the recent happenings."
    $drank_beer = True
    jump bar

label talk_to_clown:
    hide screen Bar
    show clown at center:
        zoom 2.0

    narrator "Uh oh. You just bumped into a quite psycho looking clown."
    clown "Howdy my dude! I'm so glad to meet you. Hehehehe..."
    clown "Oh yes, you thought I was this girl? Hehe, that's an illusion. That's how I lure in my unsuspecting victims."

    narrator "Judging by his creepy laugh, this guy clearly has some things misaligned in his head."

    clown "So how about a little fun?"
    clown "I'll ask you three questions!"
    clown "See this beatiful chainsaw I have? If you answer all of the questions right, I'll give it to you as a gift!"
    clown "Of course if you don't, then I'll have to shove it through you. But don't worry, it will be fun!"

    menu clown_intro:
        "Eh, why not?":
            clown "Excellent my dude!"
            jump clown_questions

        "I don't want this, leave me be.":
            clown "Oh, no, you can't back away now, no no."
            jump clown_questions

        "{color=#f00}Listen man! Just give me the chainsaw! Or I'll headbutt you.{/color}" if is_squirrel():
            clown "Whoaaa..."
            narrator "It looks like the clown realized you are a cyber squirrel. He knows your headbutting is so strong, he would be knocked to another dimension."
            narrator "He's scared from that thought."
            jump succeeded_questions

label clown_questions:
    clown "Ready? No? Good! First question!"
    clown "Why don't fish have hair?"

    menu question_one:
        "Because the politicians stole it?":
            clown "So close! But no."
            jump failed_question

        "Because they would never be able to dry their hair as they're living under water.":
            clown "Excellent! Hahaha, next one!"

    clown "So what does have the same weigth as a witch?"
    menu question_two:
        "A duck.":
            clown "I knew you were a man of culture!"

        "A fairy?":
            clown "Come on man! I was expecting better."
            jump failed_question

    clown "Last question! A plane crashes on the border of Molvania and Dundee. Where to bury the survivors?"
    menu question_three:
        "Half of them in each country.":
            jump failed_question

        "Nowhere.":
            clown "You've got them all right!"
            jump succeeded_questions

label failed_question:
    clown "Nooo... I'm a sad panda. I really didn't want to hurt you, but you forced my hand."
    play sound clown_char.get_sound_effect()
    if is_rich():
        narrator "The clown tries to stick the chainsaw in you. But you're rich, so the laws of phisics don't apply to you."
        narrator "You are unscratched."

        $talked_to_clown = True
        hide clown with moveoutright
        jump bar

    else:
        narrator "Game over..."
        hide clown with fade
        pause
        call screen Credits

label succeeded_questions:
    narrator "The clown looks at you with the utmost respect."

    clown "As promised, here you go! Take the chainsaw."
    $player_character.add_inventory_item(CHAINSAW)

    clown "I've also got an extra bonus for you! From now on, we're friends! I'll help you when you need me later!"
    play sound clown_char.get_sound_effect()

    $player_character.add_friend(clown_char)
    
    $talked_to_clown = True
    hide clown with moveoutright
    jump bar

label toilet:
    hide screen Bar
    show bg toilet
    show screen Toilet
    narrator "After that beer, you really need to pee. So you've come to the toilet."
    narrator "But this place looks so dirty..."
    
    menu toilet_choice:
        "Take a regular piss.":
            show bg toilet with fade
            narrator "So much better!"

        "{color=#f00}<Headbutt the toilet into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()
            play sound omg
            narrator "That did it! Whatever dimension it has landed in, it will take twice about keeping it's personal hygiene."
            narrator "That was so satisfying, you don't even need to pee anymore."
            
            $player_character.increase_headbutts()

            if headbutted_too_much():
                hide screen Toilet
                jump other_dimension
            
        "{color=#e717a2}I'm rich and I'm above places like this.{/color}" if is_rich():
            narrator "You're rich and your above the laws of nature. You've decided you don't need to pee anymore."
            narrator "The urge is gone, just like that."

        "{color=#fa510e}<Dark Knight> That toilet is too dirty! I'll water this nice plant instead.{/color}" if is_dark():
            narrator "Being a Dark Knight has freed you from the boundaries of ordinary people. You're braver than the rest."
            narrator "So you've watered the plant."
            show bg toilet with fade
            narrator "It sighs with gratitude."

            $player_character.increase_dark_deeds()

            narrator "But there's a catch! There's always one. You've offended these Japanese exchange students who are also in the toilet."
            play sound scream
            show angry girls at center:
                zoom 2.0
            narrator "They hit you a few times, screaming at you, calling you \"perverted senpai\" before they leave."

            hide angry girls with moveoutleft
        
        "{color=#fcff37}<Holy Knight> This toilet is too dirty. I'll purify it with my holy pee.{/color}" if is_holy():
            narrator "Being a Holy Knight has made you so clean that even your pee is clean and holy."
            show bg toilet with fade
            narrator "You've done it. The toilet is now sanctified. Suddenly the whole room is so much cleaner."
            narrator "The whole place omits a heavenly aura. This place will be a sacred place visited by many pilgrims, for generations."

            $player_character.increase_holy_deeds()

    $bathroom_break = True
    hide screen Toilet
    jump bar
