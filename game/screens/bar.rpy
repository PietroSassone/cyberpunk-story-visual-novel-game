screen Bar():
    if not talked_to_clown:
        imagebutton:
            xalign 0.2
            yalign 0.8
            auto "screen_elements/fake_clown_%s.png"
            action Jump("talk_to_clown")

    if drank_beer and not bathroom_break:
        imagebutton:
            xalign 0.975
            yalign 0.5
            auto "screen_elements/toilet_icon_%s.png"
            action Jump("toilet")

        frame:
            xalign 0.99
            yalign 0.4
            hbox:
                text "The toilet" size 40
    
    if not drank_beer:
        frame:
            xalign 0.7
            yalign 0.65
            textbutton "Order a beer.":      
                action Jump('order_beer')

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 10
        auto "screen_elements/button_back-to-map_%s.png"
        action Jump("city_center")