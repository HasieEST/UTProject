#Version 0.0.1
#Hasie Part
ChangeOmegaa...

def base_game():
    player_hand = 0
    dealer_hand = 0
    if load_game == True:
        player_cash = load_game_cash
    else:
        player_cash = 500

def game_deck():
     hearts_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
     pots_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
     diamonds_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
     spades_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']