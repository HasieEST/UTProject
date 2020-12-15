import random

playing = True
while playing is True:
    playing_deck = [("Ärtu äss", 11, "pilt"),("Ärtu kaks", 2, "pilt"), ("Ärtu kolm", 3, "pilt"), ("Ärtu neli", 4, "pilt"), ("Ärtu viis", 5, "pilt"), ("Ärtu kuus", 6, "pilt"), ("Ärtu seitse", 7, "pilt"), ("Ärtu kaheksa", 8, "pilt"), ("Ärtu üheksa", 9, "pilt"), ("Ärtu kümme", 10, "pilt"), ("Ärtu poiss", 10, "pilt"), ("Ärtu emand", 10, "pilt"), ("Ärtu kuningas", 10, "pilt"),("Risti äss", 11, "pilt"),("Risti kaks", 2, "pilt"), ("Risti kolm", 3, "pilt"), ("Risti neli", 4, "pilt"), ("Risti viis", 5, "pilt"), ("Risti kuus", 6, "pilt"), ("Risti seitse", 7, "pilt"), ("Risti kaheksa", 8, "pilt"), ("Risti üheksa", 9, "pilt"), ("Risti kümme", 10, "pilt"), ("Risti poiss", 10, "pilt"), ("Risti emand", 10, "pilt"), ("Risti kuningas", 10, "pilt"),("Potti äss", 11, "pilt"),("Potti kaks", 2, "pilt"), ("Potti kolm", 3, "pilt"), ("Potti neli", 4, "pilt"), ("Potti viis", 5, "pilt"), ("Potti kuus", 6, "pilt"), ("Potti seitse", 7, "pilt"), ("Potti kaheksa", 8, "pilt"), ("Potti üheksa", 9, "pilt"), ("Potti kümme", 10, "pilt"), ("Potti poiss", 10, "pilt"), ("Potti emand", 10, "pilt"), ("Potti kuningas", 10, "pilt"),("Ruutu äss", 11, "pilt"),("Ruutu kaks", 2, "pilt"), ("Ruutu kolm", 3, "pilt"), ("Ruutu neli", 4, "pilt"), ("Ruutu viis", 5, "pilt"), ("Ruutu kuus", 6, "pilt"), ("Ruutu seitse", 7, "pilt"), ("Ruutu kaheksa", 8, "pilt"), ("Ruutu üheksa", 9, "pilt"), ("Ruutu kümme", 10, "pilt"), ("Ruutu poiss", 10, "pilt"), ("Ruutu emand", 10, "pilt"), ("Ruutu kuningas", 10, "pilt")]

#diiler ja mängija andmed
player_hand = []
player_score = 0
dealer_hand = []
dealer_score = 0

def blackjack(player_score, dealer_score):
    if player_score > 21:
        return 0
    elif dealer_score > player_score and dealer_score > 21:
        return 2
    elif dealer_score == player_score:
        return 1
    elif dealer_score < player_score and player_score <= 21:
        return 2    