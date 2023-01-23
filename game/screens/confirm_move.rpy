screen ConfirmMove():
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        vbox:
            spacing 20
            text "{color=#910505}Warning! Entering the restaurant is a point of no return.{/color}" xalign 0.5
            text "{color=#910505}You will be unable to visit the rest of the locations, if you haven't done so yet.{/color}"
            text "{color=#910505}Continue?{/color}" xalign 0.5
    frame:
        xalign 0.5
        yalign 0.65
        hbox:
            spacing 100
            textbutton "Yes":      
                action Jump('restaurant')

            textbutton "No":      
                action Return()
