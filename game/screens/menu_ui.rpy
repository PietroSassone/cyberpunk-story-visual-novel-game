screen MenuUI():
    imagebutton:
        xalign 1.0
        yalign 0.1
        xoffset -20
        yoffset 10
        auto "screen_elements/button_inventory_%s.png"
        action ShowMenu("Inventory")

    imagebutton:
        xalign 1.0
        yalign 0.2
        xoffset -20
        yoffset 10
        auto "screen_elements/button_status_%s.png"
        action ShowMenu("Status")

    if show_hints:
        imagebutton:
            xalign 1.0
            yalign 0.3
            xoffset -20
            yoffset 10
            auto "screen_elements/button_hints_%s.png"
            action ShowMenu("Hints")
    
    if show_friend_hints:
        imagebutton:
            xalign 1.0
            yalign 0.4
            xoffset -20
            yoffset 10
            auto "screen_elements/button_friend-hints_%s.png"
            action ShowMenu("FriendHints")
            