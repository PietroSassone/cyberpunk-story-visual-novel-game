screen FriendHints():
    frame:
        xalign 0.1
        yalign 0.0
        ypadding 10
      
        hbox:
            spacing 20

            vbox:
                spacing 50
                for friend in player_character.get_friends():
                    image friend.get_image():
                        zoom 0.3

            vbox:    
                yoffset 15
                spacing 120
                for friend in player_character.get_friends():
                    text friend.get_hint() size 30 color friend.get_color_code()

    imagebutton:
        xalign 1.0
        yalign 0.9
        xoffset -30
        yoffset 30
        auto "screen_elements/button_back_%s.png"
        action Return()
        