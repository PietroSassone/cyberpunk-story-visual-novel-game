label ending_home:
    scene bg apartment with fade
    play music ending_song
    hide screen MenuUI
    narrator "You've finally made it home."

    if player_character.has_item(CAT):
        narrator "Lizzy is really happy with the cat."
        narrator "Unfortunately there's no time for her to play around with it. You've got to leave the city before getting a rest."
    narrator "The whole population is in danger. Better board a train and get far away."

    show bg train with fade

    narrator "You grab Lizzy and the cat and take an afternoon train towards another city. Your new home."
    narrator "You can finally sit back and relax, as you watch the setting sun from the train's windows."

    narrator "The next day:"
    show bg burning city with hpunch

    narrator "The news from your city show that the most terrible things are happening there."
    narrator "The Antipope has blown up halw of the city. A lot of people died. The rest are either infected, or being abducted by an army of zombies."
    narrator "There's pure chaos everywhere. The stock market has crashed. Civil war broke out between the retired people and the youngsters."
    narrator "A second chicken revolution is happening. People are blaming the church. A fanatic movement has started to demand voting rights for mushrooms."
    narrator "A new scientific theory suggests none of this would have happened if we were governed by more capable beings. Like the mushrooms, for example."
    narrator "But anyway, it's all somebody else's problem. You're luckily quite far away from there by now."
    
    call screen Credits
