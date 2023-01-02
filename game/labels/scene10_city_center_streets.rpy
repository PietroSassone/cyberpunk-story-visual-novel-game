define lizzy = Character("Lizzy", color = "#f721af")
define protester = Character("Protester", color = "#d40000")


label city_center_streets:
    hide screen CityMap
    show bg streets
    stop music fadeout 3.0

    narrator "You walk the crowded city center streets, bathing in neon lights."

    narrator "Incoming message from Lizzy the computer:"
    
    show lizzy at left

    lizzy "Hey! I hear some pretty wild s**t is happening around there."
    lizzy "The latest news on the conspiracy theory sites claim something strange."
    lizzy "They say some Antipope guy is in the city to infest everyone with cat AIDS. Get home in one peace, okay?"
    lizzy "Also, that cat you'll buy me better be of good quality! I'm still sulking. I don't want a cheap plastic cat!"

    hide lizzy

    show bg streets other with fade
    narrator "Up ahead, it looks like there's a crowd. Some unrest is going on here."

    show bg crowd with fade

    narrator "You've bumped into a protest. Quite a huge crowd has gathered here. More and more people are arriving each minute."
    narrator "Looks like you've picked the best time to visit the city center..."
    narrator "Judging by the shouts, you quickly gather some information."
    narrator "The people are really frustrated with their lives. They say everything is wrong."
    narrator "They demand that the people at fault for their bad luck should be punished."
    narrator "That means politicians, corporation leaders, loud neighbours, television celebrities, etc."
    narrator "Basically everyone. Except cute pets. Because everybody loves cute pets."

    narrator "The situation is tense. Anything could happen here..."
    narrator "The leader of the crowd tries to pull you in to their protest."

    show protester at right

    protester "Join us! Let's protest together for a better tomorrow!"
    play sound protester_char.get_sound_effect()

    menu protesting_crowd:
        "No offense, but I just really don't care about it all.":
            narrator "So you leave the scene quickly, before it escalates further."
            narrator "The protester is offended. She shouts something about calling her lawyer on you for the insult."
            $player_character.increase_lawsuits()
            if enough_lawsuits_for_jail:
                hide protester
                jump jail
        
        "<Try to calm them down>":
            narrator "You convince them, that the faulty people will never really be punished."
            narrator "It's a dark world and we can't achieve anything, not even with violence."

            protester "I... You may be right. It's very sad."

            narrator "The people around you calm down. Their anger turns into apathy and disappointment."
            protester "Eh... Guess I'll just have to go home and drown my frustration into stress eating."
           
            narrator "You leave the street, as the crowd starts to disband."
         
        "{color=#fa510e}<Dark Knight> Let's start a riot!{/color}" if is_dark():
            play music riot_song
            narrator "Being a Dark Knight has granted you the cunning to fuel their hatred even more."
            narrator "You know exactly what to yell to drive the crowd into a mad frenzy."
            narrator "The situation was already tense. But you've managed to push the people over the edge."

            narrator "They're starting a quite intensive riot. Cars and shops are already burning."

            show bg riot with fade
            protester "Hell yeah! Let's show them! Charge my brothers and sisters!"
            hide protester

            narrator "You nasty little devil."
            narrator "The crowd is wrestling with the cops and looting homes as you walk away, smiling happily."

            show bg riot two with fade
            narrator "Another big win: these people will surely come to your help later if they don't end up in jail."
            narrator "They've even left behind a bag of chips!"

            $player_character.add_friend(protester_char)
            $player_character.increase_dark_deeds()
            $player_character.add_inventory_item(CHIPS)

        "{color=#fcff37}<Holy Knight> <Try to convert the whole crowd to be holy warriors>{/color}" if is_holy():
            play music riot_song
            narrator "Being a Holy Knight has granted you the wisdom to convince even more people to release their inner righteousness."
            narrator "The crowd is already on edge, mouths foaming like rabid dogs."
            narrator "As you start preaching the holy scripts, it hits right through their hearts."
            narrator "They realise this is exactly what they needed! Throwing away all responsibility, and following the orders of some church."
            narrator "They can now be happy, not caring about how tragic life is. They find comfort in not having to think about a solution anymore."
            narrator "You have opened their eyes to the light! Well done!"

            protester "Come on brothers and sisters! Let's devote our lives to bringing the holy light to everyone possible!"
            protester "We'll convert the city, even if they don't want it. They just don't know yet that it is their best interest!"
            protester "Here, I'll give you my pack of potato chips. I won't need it anymore."

            $player_character.add_inventory_item(CHIPS)

            narrator "So they start breaking into buildings, looking for people to convert."
            narrator "You leave the scene satisfied that you've made the world a better place."

            $player_character.add_friend(protester_char)
            $player_character.increase_holy_deeds()

            narrator "Another big win: your holy army will surely come to your help later."

    hide protester
    $dealt_with_protesters = True
    jump city_center
    