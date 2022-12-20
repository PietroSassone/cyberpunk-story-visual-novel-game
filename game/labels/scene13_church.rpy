define antipope = Character("Antipope", color = "#a5a008")


label church_tunnel:
    stop music fadeout 3.0
    
    narrator "So you've decided to go after this mysterious Antipope."
    show bg church with pushright
    narrator "Supposedly he's hiding in the old techno-communist nihilistic church by the docks. That place has been locked down for a while."
    narrator "According to the conspiracy theory websites about the guy, the easiest way in to the church is an unused undergroound tunnel."

    show bg tunnel with fade
    narrator "This one right here. Not a creepy place at all."

    narrator "As you walk down the tunnel, it's like you keep hearing someone breathing down your neck. But nobody's there."
    narrator "Better keep moving quickly."

    show bg tunnel with fade
    narrator "You luckily arrive to the end of the tunnel without any incidents."
    narrator "With a sigh of relief, you see that there's a trapdoor ahead, probably leading to the inside of the church."
    narrator "Just like they said on the conspiracy theorist website. It is even unlocked! How convenient."
    narrator "You can climb up."
    narrator "Go on."
    narrator "What could go wrong, anyway?"

    jump church

label church:
    hide screen MenuUI
    show bg church interior with pushright

    narrator "The interior of the abandoned techno church is very sinister. Only some seriously wacked person would use this place as a base of operations."
    narrator "I bet your mind is already racing. Imagining all kinds of horrors."
    
    show monster one at left:
        zoom 2.0
    narrator "He probably looks like this."
    
    show monster two at right:
        zoom 2.0
    narrator "Or like this."

    show monster three at right:
        zoom 2.0
    narrator "Or even worse, like this."

    hide monster

    pause 3.0
    show antipope at right with vpunch:
        zoom 2.0

    antipope "Greetings fine young person!"
    antipope "I'm the Antipope and I bid you welcome to my humble home. I'm so excited! I hope you'll like it here."
    antipope "What? I'm not what you were expecting?"
    antipope "What were you expecting, some kind of monster? Oh no, see, I'm very cute and lovely!"
    antipope "I bet you'de love to rub my ears!"
    antipope "I'm glad you're here. We don't get so many visitors here."
    antipope "What do I mean by \"We\"?"
    antipope "Well of course me, and my army of soul sucking zombies."
    antipope "So you've come to submit and be my slave wilingly? It'll be so much fun! We'll play fetch all day long!"
    antipope "Yes, that's why I've created my plan to overthrow this city. I'll blow up cat AIDS bombs everywhere."
    antipope "Then people will suffer, and it they will have no choice, but to play with me all day! Yaay!"

    play sound "audio/evil_laugh.mp3"

    menu church_choice:
        "You know what? Being the slave sounds like less responsibility. I'll surrender.":
            narrator "So you have laid down your weapons."
            antipope "Most excellent! You'll be my favorite pet!"
            hide antipope
            jump ending_defeat
            
        "Sorry, but your plan is just evil. I have to stop it.":
            antipope "So you have chosen... Death."
            show antipope fight
            play sound evil_shriek
            play music "audio/free_AURORA_by_DEgITx_(feat_Matty_M).mp3"
            jump boss_fight

label victory:
    stop music fadeout 3.0
    antipope "Oh no! I'm bored of fighting. Let's just stop it."
    hide antipope

    menu end_choice:
        "{color=#fcff37}<Holy Knight> I have purged the city from evil!{/color}" if is_holy():
            jump ending_holy

        "{color=#fa510e}<Dark Knight> I will be the new Antipope{/color}" if is_dark():
            jump ending_dark
            