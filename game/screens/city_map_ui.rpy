screen CityMap():
    add "screen_elements/bg city center.jpg"
    
    if not (talked_to_chicken and talked_to_hobo and defeated_zombie):
        frame:
            xalign 0.87
            yalign 0.675
            hbox:
                text "The park" size 40

        imagebutton:
            xalign 0.85
            yalign 0.6
            auto "screen_elements/park_icon_%s.png"
            action Jump("park")
    
    if not purchased_cat:
        frame:
            xalign 0.34
            yalign 0.52
            hbox:
                text "The store" size 40

        imagebutton:
            xalign 0.35
            yalign 0.45
            auto "screen_elements/store_icon_%s.png"
            action Jump('in_the_store')

    if not (talked_to_clown and bathroom_break):
        frame:
            xalign 0.6
            yalign 0.475
            hbox:
                text "The bar" size 40

        imagebutton:
            xalign 0.6
            yalign 0.4
            auto "screen_elements/bar_icon_%s.png"
            action Jump('bar')

    if not dealt_with_protesters:
        frame:
            xalign 0.28
            yalign 0.65
            hbox:
                text "The streets" size 40

        imagebutton:
            xalign 0.3
            yalign 0.58
            auto "screen_elements/street_icon_%s.png"
            action Jump('city_center_streets')

    if purchased_cat:
        frame:
            xalign 0.85
            yalign 0.38
            hbox:
                text "The restaurant" size 40

        imagebutton:
            xalign 0.8
            yalign 0.3
            auto "screen_elements/store_icon_%s.png"
            action Show('ConfirmMove')
