define bishop = Character("Techno Bishop of the Order of the Holiest of Holy People", color = "#ffffff")
define politician = Character("Politician", color = "#756763")


label central_station:
    show bg central_station with fade
    play music "audio/Thriller_by_Infraction_No_Copyright_Music_Utopia.mp3"

    narrator "You've arrived at the city center station finally."
    narrator "You notice a majestic robed man standing in the middle of the station yelling loudly and looking at the people with contempt."
    narrator "A priest. Here, in the middle of the crowded station, preaching to the people.\nShaming them for their shamelessnes and lack of mindlessly following religion."

    show bishop at center
    bishop "Repent! The end is nigh!"
    narrator "Yes, the good old line."

    bishop "You should all feel ashamed for not living a holy life! Look at yourselves! What has the world come to!"
    bishop "Destruction awaits you all if you don't repent your sins!\nEvil has infested this city."
    bishop "Something terrible is working in the shadows. Beware!"

    narrator " He looks at you."

    if is_dark():
        narrator "He smells you. Then screams in disgust."
        bishop "You! Filth! I smell that you're a Dark Knight! I cast you out, unholy creature! Begone!"
        narrator "You just leave him. Ignore this lunatic."

    else:
        bishop "My man! I looked into your soul and I see decency. It is a rare thing nowadays."
        bishop "This world is rotten! I'm here to distribute the light of Holyness."
        bishop "I see potential only you. Join the church! Become a Holy Knight! Help us spread righteousness!"
        bishop "Should you choose to join us, you could unleash your inner holyness.\nIt would unlock potential
                new opportunities in your life."
        bishop "It's a great ooprtunity! Don't let the celibacy scare you!"
        bishop "What say you, noble man?"

        menu holyness:
            "Hm. Why not? Let us show those infidel dogs together.":
                $player_character.set_knight_status(HOLY)
                bishop "Most excellent! Let the Holy light in your heart guide you on your journey!"
                play music "audio/patriotic_license_free.mp3"

            "No thanks. I'm not really up for it.":
                bishop "Eh. It was worth a try. I guess I'll just go home."
                narrator "So he leaves."
    hide bishop with moveoutright

    jump vote_for_me

label vote_for_me:
    narrator "Then again. It looks like people just won't let you be."
    narrator "Right now, another person approaches you."

    show politician at right:
        zoom 2.0

    politician "Greetings law abiding citizen! I'm your district representative, running for president!"
    narrator "Even worse than the previous faces. A politician."

    if is_holy():
        show bishop at left:
            zoom 2.0

        bishop "This person is a heretic dog! She's withdrawn money from the church!"
        bishop "Here's our first chance to cleanse the world from evil! Punish the heretic!"
        hide bishop with moveoutright

    politician "Vote for me fellow random person! I'm counting on you!"

    menu talk_to_politician:
        "No way in hell.":
            politician "But my dear voter, you'll see reason!"
            narrator "She won't leave you alone."
            jump politician_speech

        "Fine just leave me alone!":
            politician "Great! Thank you fellow whatsyourname-idontcare! See you on election day!"
            narrator "She moves on to convince some other people."

        "{color=#34b2e47f}No. You vote for me!{/color}" if is_shaman():
            politician "..."
            politician "I... Uh... Hmm..."
            narrator "She's totally baffled by your superior intelligence. She's lost for words. She's defeted."
            politician "Well, oh, okay."
            narrator "Realising she's got a lot to learn, she bows her head then leaves."
            narrator "She's now your friend that you can call on."
            play sound player_character.get_sound_effect()
            $player_character.add_friend(politician_char)

        "{color=#e717a2}I'm rich and I can support you. Let's talk business. I want my share of the money you steal from the people.{/color}" if player_character.get_class_name() == 'Rich Person':
            narrator "Her eyes flash with enthusiasm."
            narrator "You discuss the details of how you'll support her campaign and how she'll give you some companies that she'll steal from their owners."
            narrator "You both shake hands and part happily. She's now your friend. You can call on her."
            $player_character.add_friend(politician_char)

        "{color=#f00}<Headbutt the man into another dimension>{/color}" if is_squirrel():
            play sound player_character.get_sound_effect()

            narrator "The politician has a very thick skin on her face. This didn't even scratch her."
            narrator "She continues talking about her campaign."
            $player_character.increase_headbutts()
            
            jump politician_speech

        "{color=#fcff37}<Holy Knight> Burn the heretic!{/color}" if is_holy():
            narrator "Being a Holy Knight has granted you the strenght to unleash your inner righteousness."
            narrator "Punishing her for preying on the poor, you chase her out from the station with a Holy flamethrower. Lent to you by the bishop."

            play sound scream
            show politician escaping at right:
                zoom 2.0

            narrator "Of course it's a civilized age so you're not actually hurting her. It's just some pyrotechnic effect."
            narrator "No politicians were harmed during making this content."
            narrator "Only her ego. But you've done a Holy deed, spreading justice for the poor."

            $player_character.increase_lawsuits()
            $player_character.increase_holy_deeds()
            narrator"As she runs out the station, she shouts at you one more time:"
            politician "You'll be hearing from my lawyer!!!"

    hide politician with dissolve
    jump leave_station
      
label politician_speech:
    narrator "She just keeps on talking..."
    politician "So here's my 500 step agenda:"

    show bg central_station with fade
    narrator "10 minutes later:"

    politician "And then there will be some celebrations and everybody will be happy..."

    show bg central_station with fade
    politician "And then I'll pet some cute little animals and kids..."

    show bg central_station with fade
    narrator "20 minutes later:"

    politician "And of course this is all very good for you!"
    politician "So see you on election day!"

    narrator "She finally leaves. Hallelujah!"

    hide politician
    jump leave_station

label leave_station:
    narrator "Finally you make your way to the surface. You've arrived at the city center. Time to get things done."
    jump city_center
