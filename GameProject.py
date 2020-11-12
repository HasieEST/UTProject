import random
hearts_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
pots_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
diamonds_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
spades_deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']

#WIP
#while playing:
    #playing_deck = [("Ace of Hearts", 11, "pilt"),("Two of Hearts", 2, "pilt"), ("Three of Hearts", 3, "pilt"), ("Four of Hearts", 4, "pilt"), ("Five of Hearts", 5, "pilt"), ("Six of Hearts", 6, "pilt"), ("Seven of Hearts", 7, "pilt"), ("Eight of Hearts", 8, "pilt"), ("Nine of Hearts", 9, "pilt"), ("Ten of Hearts", 10, "pilt"), ("Jack of Hearts", 10, "pilt"), ("Queen of Hearts", 10, "pilt"), ("King of Hearts", 10, "pilt"),("Ace of Spades", 11, "pilt"),("Two of Spades", 2, "pilt"), ("Three of Spades", 3, "pilt"), ("Four of Spades", 4, "pilt"), ("Five of Spades", 5, "pilt"), ("Six of Spades", 6, "pilt"), ("Seven of Spades", 7, "pilt"), ("Eight of Spades", 8, "pilt"), ("Nine of Spades", 9, "pilt"), ("Ten of Spades", 10, "pilt"), ("Jack of Spades", 10, "pilt"), ("Queen of Spades", 10, "pilt"), ("King of Spades", 10, "pilt"),("Ace of Clubs", 11, "pilt"),("Two of Clubs", 2, "pilt"), ("Three of Clubs", 3, "pilt"), ("Four of Clubs", 4, "pilt"), ("Five of Clubs", 5, "pilt"), ("Six of Clubs", 6, "pilt"), ("Seven of Clubs", 7, "pilt"), ("Eight of Clubs", 8, "pilt"), ("Nine of Clubs", 9, "pilt"), ("Ten of Clubs", 10, "pilt"), ("Jack of Clubs", 10, "pilt"), ("Queen of Clubs", 10, "pilt"), ("King of Clubs", 10, "pilt"),("Ace of Diamonds", 11, "pilt"),("Two of Diamonds", 2, "pilt"), ("Three of Diamonds", 3, "pilt"), ("Four of Diamonds", 4, "pilt"), ("Five of Diamonds", 5, "pilt"), ("Six of Diamonds", 6, "pilt"), ("Seven of Diamonds", 7, "pilt"), ("Eight of Diamonds", 8, "pilt"), ("Nine of Diamonds", 9, "pilt"), ("Ten of Diamonds", 10, "pilt"), ("Jack of Diamonds", 10, "pilt"), ("Queen of Diamonds", 10, "pilt"), ("King of Diamonds", 10, "pilt")]
    #player_cards = []




def deal():
    hand = []
    for e in range(2): #tuleb ülevaatada.
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
            random.shuffle(diamonds_deck)
            card = diamonds_deck.pop()
            random.shuffle(diamonds_deck)
            card = diamonds_deck.pop()

          
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
    if number == 1:
        random.shuffle(hearts_deck)
        card = hearts_deck.pop()
        hand.append(card)
            
    elif number == 2:
         random.shuffle(pots_deck)
         card = pots_deck.pop()
         hand.append(card)
            
    elif number == 3:
        random.shuffle(diamonds_deck)
        card = diamonds_deck.pop()
        hand.append(card)
           
    elif number == 4:
        random.shuffle(spades_deck)
        card = spades_deck.pop()
        hand.append(card)         
    return hand

def blackjack(player_hand, dealer_hand):
    if kokku(dealer_hand) > kokku(player_hand) and dealer_hand <= 21:
        return "DEALERWINS"
    elif kokku(player_hand) > kokku(dealer_hand) and  player_hand <= 21:
        return "PLAYERWINS"
    elif kokku(player_hand) < kokku(dealer_hand) and dealer_hand > 21:
        return "PLAYERWINS"         

#def split(hand):
    #if player_input_split == True:
        #first_hand = hand.pop()
        #second_hand = hand
    #return first_hand, second_hand


#def base_game():
    #player_hand = deal()
    #dealer_hand = deal()
        
#def start_game():
    #base_game()