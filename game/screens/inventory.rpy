screen Inventory():
    add "screen_elements/bg inventory.png"
    frame:
        xalign 0.5
        yalign 0.2
        ypadding 30
        xpadding 40
      
        hbox:
            spacing 20
            xoffset 15

            vbox:
                spacing 50
                for item_name in player_character.get_inventory():
                    text item_name size 50

            vbox:    
                spacing 42
                for item in player_character.get_inventory().values():
                    image item.get_image_path()

            if show_magic_level:
                vbox:    
                    spacing 50
                    xoffset -20
                    for item in player_character.get_inventory().values():
                        $magic_energy = item.get_magic_level().value
                        text "Magic: [magic_energy]" size 50

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "screen_elements/button_back_%s.png"
        action Return()
        