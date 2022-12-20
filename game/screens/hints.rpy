screen Hints():
    frame:
        xalign 0.2
        yalign 0.3
        
        vbox:    
            spacing 15
            xoffset 35
            yoffset 20
            
            text "{b}{u}General:{b}{u}"
            text "- As you probably already realized, you can make choices in this game of life." size 25
            text "- You had the chance to choose your class and even join one of 2 distinct groups that hate each other." size 25
 
            text "{b}{u}Friends and items:{b}{u}"
            text "- You can make friends along your way today. Only specific actions lead to a character becoming your friends." size 25
            text "- Some such actions are only available to a given class. Or it may simply depend on your behaviour." size 25
            text "- All of the characters you can befriend are:" size 25
            text "- The girl with the shoe collecting addiction. The old lady. The wise and deadly techno chicken. A politician. A crazy clown. A group of protesters." size 25
            text "- You can also collect these items next to what you started with: a zombie arm, a grenade, a chainsaw, a chicken feather, a bag of chips and a cat." size 25

            text "{b}{u}Locations:{b}{u}"
            text "- There are 4 locations you can visit in the city center to collect everything. Once you've bought the cat, the restaurant scene unlocks." size 25
            text "- It is a point of no return. Only go there if you want to conclude the day." size 25
        
        vbox:
            yalign 0.9
            spacing 15
            xoffset 35
            yoffset -50
            text "{b}{u}Endings{b}{u}"
            text "- There are 9 possible ways to end your story today. 3 are utter catastrophies you trigger instantly if you make bad choices." size 25
            text "- If you've made at least 3 of the total 5 possible evil or holy deed, you'll have the chance to fight a final boss." size 25
            text "- You can trigger the same ending if you fail the fight or surrender. 2 other endings are possible if you win, based on your group association." size 25
            text "- You can instead also try to do a ritual to win the situation instead of fighting." size 25
            text "- If you've made friends, they'll help you in the fight or in the ritual." size 25
            text "- The same goes for the items you collect." size 25
            text "- The ritual has 3 possible endings. One is the same as if you just walk away and go home." size 25

    imagebutton:
        xalign 1.0
        yalign 0.9
        xoffset -30
        yoffset 30
        auto "screen_elements/button_back_%s.png"
        action Return()
        