import random
hearts_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
pots_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
diamonds_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
spades_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

def deal():
    hand = []
    for i in range(2):
        number = random.randint(1,4)
        if number == 1:
            random.shuffle(hearts_deck)
            card = hearts_deck.pop()
            hand.append(card)
            
        if number == 2:
            random.shuffle(pots_deck)
            card = pots_deck.pop()
            hand.append(card)
            
        if number == 3:
            random.shuffle(diamond_deck)
            card = diamond_deck.pop()
            hand.append(card)
           
        if number == 4:
            random.shuffle(spades_deck)
            card = spades_deck.pop()
            hand.append(card)
          
    return hand
    
print(deal())


def kokku(hand):
    total = 0
    for card in hand:
        if card == "K" or card == "J" or card == "Q":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
    return total

def hit(hand):
    number = random.randint(1,4)
        if number == 1
            random.shuffle(hearts_deck)
            card = hearts_deck.pop()
            hand.append(card)
            
        if number == 2
            random.shuffle(pots_deck)
            card = pots_deck.pop()
            hand.append(card)
            
        if number == 3
            random.shuffle(diamond_deck)
            card = diamond_deck.pop()
            hand.append(card)
           
        if number == 4
            random.shuffle(spades_deck)
            card = spades_deck.pop()
            hand.append(card)         
    return hand

def blackjack(player_hand, dealer_hand):
    if total(dealer_hand) == 21:
    
    elif total(player_hand) == 21:
        



def base_game():
    player_hand = deal()
    dealer_hand = deal()
        