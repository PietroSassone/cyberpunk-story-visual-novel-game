screen CharacterSelector():
    add "screen_elements/bg charselector.png"

    frame:
        xalign 0.5
        text "{b}Choose your character!{b}" size 100 xalign 0.5
    hbox:
        xalign 0.5
        yalign 0.3
        spacing 20
        yoffset 20

        imagebutton:
            auto "screen_elements/squirrel_%s.png"
            action Jump('start_squirrel')

        imagebutton:
            auto "screen_elements/shaman_%s.png"
            action Jump('start_shaman')

        imagebutton:
            auto "screen_elements/rich_%s.png"
            action Jump('start_rich')
    frame:
        xpadding 10
        ypadding 25
        xalign 0.15
        yalign 0.8

        hbox:
            text "Cyber Squirrel:\nStrong." size 50

    frame:
        xpadding 10
        ypadding 25
        xalign 0.5
        yalign 0.8

        hbox:
            text "Techno Shaman:\nIntelligent." size 50
    
    frame:
        xpadding 10
        ypadding 25
        xalign 0.85
        yalign 0.8

        hbox:
            text "Rich Person:\nMake a guess." size 50
            