screen CityPark():

    frame:
        xalign 0.4
        yalign 0.4
        
        textbutton "Go further in the park":
            action Jump('inner_park')

    if not talked_to_chicken:
        imagebutton:
            xalign 0.8
            yalign 0.5
            auto "screen_elements/chicken_%s.png"
            action Jump("talk_to_chicken")

    if not talked_to_hobo:
        imagebutton:
            xalign 0
            yalign 0.8
            auto "screen_elements/hobo_%s.png"
            action Jump("talk_to_hobo")

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 10
        auto "screen_elements/button_back-to-map_%s.png"
        action Jump("city_center")