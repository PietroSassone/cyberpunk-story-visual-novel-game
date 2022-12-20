screen CityParkInner():

    if not defeated_zombie:
        imagebutton:
            xalign 0.3
            yalign 0.8
            auto "screen_elements/zombie_%s.png"
            action Jump("defeat_zombie")

    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 10
        auto "screen_elements/button_back-to-map_%s.png"
        action Jump("city_center")