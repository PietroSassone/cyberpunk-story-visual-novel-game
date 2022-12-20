define goat = Character("Interdimensional goat", color = "#08a5a5")


label ending_goat:
    show bg utopia_ending with fade
    hide screen MenuUI
    play music ending_song
    narrator "Oh! You did it! You've summoned the interdimensional goat!"
    narrator "Who would've thought that this can be done for real?"
    narrator "The internet was right again."

    show goat at right:
        zoom 2.0

    goat "Sup?"

    narrator "The world is saved!"
    narrator "Indeed it is. Starting tomorrow, all wars end, as humanity realises that a deity has descended among us."
    narrator "Politicians all stop their work. Both capitalist and communist agendas stop immediately."
    narrator "The banks and religions cease to exist. Scientist invent free, green and unlimited energy."
    narrator "Everyone gets enlightened by the goat's aura. People stop being jerks and now everybody is just full of love, all around the world!"
    narrator "Truly, an utopia has come. The golden age for humanity is here!"

    call screen Credits
    