label restaurant:
    hide screen CityMap
    hide screen ConfirmMove
    show bg restaurant
    play music "audio/Jim_Yosef_Samurai_license_free.mp3"

    narrator "Well, it's almost about time to conclude your business in this city for today."
    narrator "First of all, you better grab some food before going further."
    narrator "Then you should think things over. Decide what to do next."

    if len(player_character._friends) > 0:
        narrator "You have collected some friends along the way. Let's call them for a strategic planning!"

        show screen Friends
        narrator "Your new friends have come to your help! They will provide valuable input in your final actions for today."
        narrator "These are same hardcore veterans. With them by your side, nothing can go wrong."
        narrator "You also have to buy them dinner now that you've called them to the restaurant."
        hide screen Friends

    narrator "Let's assess the situation. You've got the cat."
    narrator "Then you realized that something terrible is about to happen."
    narrator "Some possibly evil guy called the Antipope is about to do something bad."
    narrator "He also threatened you personally. This may be bad for your health on the long run."
    narrator "You know that he's plotting his... Plots in the old abandoned techno-communist nihilistic church by the docks."
    narrator "What do you wan't to do with the situation?"

    menu final_choice:
        "This is too crazy for me. I'll just go home to Lizzy with the cat, then we'll leave this city.":
            narrator "So you've decided to leave all this crazyness behind. Let it be somebody else's problem."
            jump ending_home

        "Enough of this stress. I'll summon the interdimensional goat and ask it for guidance.":
            jump ritual
            
        "{color=#7a3d00}I'll end the threat of this Antipope myself.{/color}" if unlock_antipope_ending():
            jump church_tunnel
jump city_center
            