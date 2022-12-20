screen Credits():
    frame:
        xalign 0.5
        yalign 0.1
        
        vbox:
            yalign 0.0
            xalign 0.5
            spacing 15
            yoffset 50
            text "{color=#910505}Thank you for playing my little nonsense game!{/color}" size 40 xalign 0.5
            text "{color=#910505}I hope you enjoyed it!{/color}" size 35 xalign 0.5
            text "{color=#910505}Created by Peter Szasz.{/color}" xalign 0.5
            text "{color=#910505}Contact: szasz.peter.gi@gmail.com{/color}" xalign 0.5
    
        vbox:
            yalign 0.375
            xalign 0.5
            spacing 25
            xoffset 20
            yoffset 50
            
            text "{u}There are lot of resources used in this game. Icons, images, sounds effects, music.{u}" size 40 xalign 0.5
            text "{u}All of them are license and copyright free.{u}" size 40 xalign 0.5
            text "{u}Please check out the \"About\" menu for links to the resources!{u}" size 40 xalign 0.5

        vbox:
            xalign 0.5
            yalign 0.7
            textbutton _("About Menu") action ShowMenu("about")

    imagebutton:
        xalign 0.5
        yalign 0.9
        auto "screen_elements/button_main-menu_%s.png"
        action MainMenu()
        