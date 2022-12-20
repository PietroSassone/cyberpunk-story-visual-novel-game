define talked_to_chicken = False
define talked_to_hobo = False
define defeated_zombie = False
define talked_to_clown = False
define bathroom_break = False
define dealt_with_protesters = False
define purchased_cat = False


label city_center:
    show screen CityMap
    hide screen Bar
    hide screen CityPark
    hide screen CityParkInner
    hide screen ConfirmMove

    play music "audio/Y&V_Lune_NCS_Release.mp3"

    narrator "You're in the city center. Choose where you want to go next."
    jump city_center
    