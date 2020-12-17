import random

def draw(x):
    card_drawn = random.choice(x)
    x.remove(card_drawn)
    return card_drawn

def kokku(x):
    total = 0
    total_set = []
    for el in x:
        total_set.append(el[1])
    total = sum(total_set)
    ace = True
    while ace is True:
        if total > 21 and 11 in total_set:
            total_set.remove(11)
            total_set.append(1)
            total = sum(total_set)
        else:
            ace = False
    return total

def käsi(x):
    kaardid = []
    for el in x:
        kaardid.append(el[0])
    kaardinimed = kaardid[0]
    for i in kaardid[1:]:
        kaardinimed = kaardinimed + ", " + i
    return kaardinimed