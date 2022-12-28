screen Status():
    add "screen_elements/bg status.png"
    frame:
        xalign 0.1
        yalign 0.1
        xpadding 15
        ypadding 60
      
        hbox:
            spacing 20

            vbox:
                xoffset 15
                yoffset 15
                spacing 30
                text "Character:" size 50
                text player_character.get_class_name() size 50
                text "Extra association:" size 50
                text player_character.get_knight_status() size 50

            vbox:    
                yalign 0.1
                xalign 0.5
                image player_character._image zoom 0.5

    frame:
        xalign 0.1
        yalign 0.7
        ypadding 60
      
        hbox:
            spacing 20

            vbox:
                spacing 10
                xoffset 15
                yoffset 15
                text "Evil choices you've made:" size 40
                text "Holy choices you've made:" size 40
                text "Number of lawsuits against you:" size 40
                text "Beware!\nYou'll end up in court after 3 lawsuits." size 40

            vbox:    
                spacing 25
                xoffset -20
                text "[player_character._dark_deeds]"
                text "[player_character._holy_deeds]"
                text "[player_character._lawsuits]"
    
    frame:
        xalign 0.6
        yalign 0.5
        xpadding 15

        text "Friends" size 50 xalign 0.5

    frame:
        xalign 0.8
        yalign 0.0
        xpadding 15
        ypadding 30
        yoffset -10

        hbox: 
            yoffset 5
            vbox:
                spacing 10
                for friend in player_character.get_friends():
                    image friend.get_image():
                        zoom 0.175 
                        xalign 0.5

                    text friend.get_name() size 30 xalign 0.5          

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "screen_elements/button_back_%s.png"
        action Return()
