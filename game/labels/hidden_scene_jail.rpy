define officer = Character("Police Officer", color = "#119eb1")


label jail:
    play music bad_ending_song
    hide screen MenuUI
    show officer at right:
        zoom 2.0

    officer "Hold it right there! You've been behaving badly. 3 lawsuits have been filed against you. You're coming with me!"

    hide officer
    
    show bg jail with fade
    narrator "It looks like you've collected so many lawsuits, you've been thrown to jail."
    narrator "Of course only until your trial. Which should be in a few years."
    narrator "Lizzy the computer will be pissed, because she won't get that cat soon."
    narrator "Better luck next time!"
    call screen Credits
    