screen Friends():
    frame:
        xalign 0.05
        yalign 0.5
        hbox: 
            for friend in player_character.get_friends():
                image friend.get_image():
                    zoom 0.5           
             