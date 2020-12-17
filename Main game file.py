import random, Dealing, turtle, graafika

pliiats = turtle.Turtle()
pliiats.hideturtle()
pliiats.speed(0)
pliiats.penup()
pliiats.pensize(5)

graafika.mänguala(pliiats)



print("Kas soovite mängida panustega")
kas_panustada = input("Jah, kui soovite.\n>>>>").lower()
print("")
if kas_panustada == "jah":
    panustamine = True
    player_raha = 100
elif kas_panustada == "":
    panustamine = False

mängib = True
while mängib is True:
    playing_deck = [("Ärtu äss", 11, "hA.gif"),("Ärtu kaks", 2, "h2.gif"), ("Ärtu kolm", 3, "h3.gif"), ("Ärtu neli", 4, "h4.gif"), ("Ärtu viis", 5, "h5.gif"), ("Ärtu kuus", 6, "h6.gif"), ("Ärtu seitse", 7, "h7.gif"), ("Ärtu kaheksa", 8, "h8.gif"), ("Ärtu üheksa", 9, "h9.gif"), ("Ärtu kümme", 10, "h10.gif"), ("Ärtu poiss", 10, "hJ.gif"), ("Ärtu emand", 10, "hQ.gif"), ("Ärtu kuningas", 10, "hK.gif"),("Risti äss", 11, "clubsA.gif"),("Risti kaks", 2, "clubs2.gif"), ("Risti kolm", 3, "clubs3.gif"), ("Risti neli", 4, "clubs4.gif"), ("Risti viis", 5, "clubs5.gif"), ("Risti kuus", 6, "clubs6.gif"), ("Risti seitse", 7, "clubs7.gif"), ("Risti kaheksa", 8, "clubs8.gif"), ("Risti üheksa", 9, "clubs9.gif"), ("Risti kümme", 10, "clubs10.gif"), ("Risti poiss", 10, "clubsJ.gif"), ("Risti emand", 10, "clubsQ.gif"), ("Risti kuningas", 10, "clubsK.gif"),("Potti äss", 11, "spadesA.gif"),("Potti kaks", 2, "spades2.gif"), ("Potti kolm", 3, "spades3.gif"), ("Potti neli", 4, "spades4.gif"), ("Potti viis", 5, "spades5.gif"), ("Potti kuus", 6, "spades6.gif"), ("Potti seitse", 7, "spades7.gif"), ("Potti kaheksa", 8, "spades8.gif"), ("Potti üheksa", 9, "spades9.gif"), ("Potti kümme", 10, "spades10.gif"), ("Potti poiss", 10, "spadesJ.gif"), ("Potti emand", 10, "spadesQ.gif"), ("Potti kuningas", 10, "spadesK.gif"),("Ruutu äss", 11, "diaA.gif"),("Ruutu kaks", 2, "dia2.gif"), ("Ruutu kolm", 3, "dia3.gif"), ("Ruutu neli", 4, "dia4.gif"), ("Ruutu viis", 5, "dia5.gif"), ("Ruutu kuus", 6, "dia6.gif"), ("Ruutu seitse", 7, "dia7.gif"), ("Ruutu kaheksa", 8, "dia8.gif"), ("Ruutu üheksa", 9, "dia9.gif"), ("Ruutu kümme", 10, "dia10.gif"), ("Ruutu poiss", 10, "diaJ.gif"), ("Ruutu emand", 10, "diaQ.gif"), ("Ruutu kuningas", 10, "diaK.gif")]

    #diiler ja mängija andmed
    player_hand = []
    player_score = 0
    player2_hand = []
    player2_score = 0
    dealer_hand = []
    dealer_score = 0

    dealer_hand.append(Dealing.draw(playing_deck))
    graafika.create_card_image(dealer_hand, "dealer")
    player_hand.append(Dealing.draw(playing_deck))
    graafika.create_card_image(player_hand, "player")
    player_hand.append(Dealing.draw(playing_deck))
    graafika.create_card_image(player_hand, "player")
    player_score = Dealing.kokku(player_hand)
    print("Mängu alustav käsi: " + Dealing.käsi(player_hand))
    print("Mängu alustav skoor: " + str(player_score))
    print("Mängu alustav diileri kaart: " + Dealing.käsi(dealer_hand))

    if panustamine == True:
        print("Teil on hetkel krediiti: " + str(player_raha)+"\n")


    player_panus = 0
    player_panus2 = 0
    if panustamine == True:
        while player_panus == 0:
            try:
                player_panus = int(input("Kui palju panustate?\n>>>> "))
                if player_panus > player_raha:
                    print("Teil puudub piisavalt vahendeid, et panustada nii palju.")
                    player_panus = 0
            except:
                print("Sisestatud väärtus ei ole täisarv, proovige uuesti!")
                player_panus = 0
    print("")

    if player_hand[0][1] == player_hand[1][1]:
        print("Kas soovite poolitada?")
        spliting = input("Jah, kui soovite").lower()
        if spliting == "jah":
            player_hand2 = player_hand[1]
            graafika.create_card_image(player_hand2, "player2")
            player_hand.remove(player2_hand)
            player_hand.append(Dealing.draw(playing_deck))
            graafika.create_card_image(player_hand, "player")
            player_hand2.append(Dealing.draw(playing_deck))
            graafika.create_card_image(player_hand2, "player2")
            player_panus2 = player_panus
            player_score = Dealing.kokku(player_hand)
            player_score2 = Dealing.kokku(player_hand2)
            print("Esimene käsi: " + Dealing.käsi(player_hand))
            print("Esimese käe skoor: " + str(player_score))
            print("Teine käsi: " + Dealing.käsi(player2_hand))
            print("Teise käe skoor: " + str(player_score2))

    mängimas = True
    player_võit = None
    player_võit2 = None
    while mängimas:
        if len(player2_hand)>1:
            print("Kas soovite esimesele käele tõmmata kaarti juurde?")
            tõmbamas = input("Kirjutage 'jah' kaardi tõmbamiseks, kirjutage 'hoia' tõmbamise lõpetamiseks.").lower()
            print("")
            if tõmbamas == "jah":
                player_hand.append(Dealing.draw(playing_deck))
                graafika.create_card_image(player_hand, "player")
                player_score = Dealing.kokku(player_hand)
                if player_score > 21:
                    print("Esimene käsi hetkel: " + Dealing.käsi(player_hand))
                    print("Esimese käe skoor: " + str(player_score)+"\n Olete lõhki läinud. Kaotasite selle käega!")
                    player_võit = False
                elif len(player_hand)>4:
                    print("Oi sa ei läinud viie kaardiga lõhki. Võitsite!")
                    player_võit = True
                else:
                    print("Esimene käsi hetkel: " + Dealing.käsi(player_hand))
                    print("Esimese käe skoor: " + str(player_score)+"\n")
            elif tõmbamas == "hoia":
                tõmbamas2 = input("Kirjutage 'jah' kaardi tõmbamiseks, kirjutage 'hoia' tõmbamise lõpetamiseks.").lower()
                print("")
                if tõmbamas2 == "jah":
                    player_hand2.append(Dealing.draw(playing_deck))
                    graafika.create_card_image(player_hand2, "player2")
                    player_score2 = Dealing.kokku(player_hand2)
                    if player_score2 > 21:
                        print("Teine käsi hetkel: " + Dealing.käsi(player_hand2))
                        print("Teise käe skoor: " + str(player_score2)+"\n Olete lõhki läinud. Kaotasite selle käega!")
                        player_võit = False
                    elif len(player_hand2)>4:
                        print("Oi sa ei läinud viie kaardiga lõhki. Võitsite!")
                        player_võit = True
                    else:
                        print("Teine käsi hetkel: " + Dealing.käsi(player_hand2))
                        print("Teise käe skoor: " + str(player_score2)+"\n")
                elif tõmbamas2 == "hoia":
                    print("Nüüd võtab diiler kaardi.")
                    dealer_hand.append(Dealing.draw(playing_deck))
                    graafika.create_card_image(dealer_hand, "dealer")
                    dealer_score = Dealing.kokku(dealer_hand)
                    while dealer_score < 16:
                        dealer_hand.append(Dealing.draw(playing_deck))
                        graafika.create_card_image(dealer_hand, "dealer")
                        dealer_score = Dealing.kokku(dealer_hand)
                    print("Diileri käsi on hetkel:" + Dealing.käsi(dealer_hand))
                    print("Diileri käe skoor: "+ str(dealer_score)+"\n")
                    if len(dealer_hand) > 4:
                        player_võit2 = False
                    elif dealer_score > 21:
                        player_võit2 = True
                    elif dealer_score >  player_score2:
                        print("Diileril suurem käsi, kui teie teine käsi. Kaotasite sellega!")
                        player_võit2 = False
                    else:
                        print("Teie teine käsi on suurem, kui diileri. Võitsite sellega!")
                        player_võit2 = True
                if len(dealer_hand) > 4:
                    print("Diiler ei läinud viie kaardiga lõhki. Kaotasite!")
                    player_võit = False
                    mängimas = False
                elif dealer_score > 21:
                    print("Diiler läks lõhki. Te võitsite!")
                    player_võit = True
                    mängimas = False
                elif dealer_score >  player_score:
                    print("Diileril suurem käsi, kui teie esimene käsi. Kaotasite sellega!")
                    player_võit = False
                    mängimas = False
                else:
                    print("Teil on suurem käsi, kui diileri. Võitsite sellega!")
                    player_võit = True
                    mängimas = False
        else:
            tõmbamas = input("Kirjutage 'jah' kaardi tõmbamiseks, kirjutage 'hoia' tõmbamise lõpetamiseks.").lower()
            print("")
            if tõmbamas == "jah":
                player_hand.append(Dealing.draw(playing_deck))
                graafika.create_card_image(player_hand, "player")
                player_score = Dealing.kokku(player_hand)
                if player_score > 21:
                    print("Teie käsi hetkel: " + Dealing.käsi(player_hand))
                    print("Teie käe skoor: " + str(player_score)+"\n Olete lõhki läinud. Kaotasite!")
                    player_võit = False
                    mängimas = False
                elif len(player_hand)>4:
                    print("Oi sa ei läinud viie kaardiga lõhki. Võitsite!")
                    player_võit = True
                    mängimas = False
                else:
                    print("Teie käsi hetkel: " + Dealing.käsi(player_hand))
                    print("Teie käe skoor: " + str(player_score)+"\n")
            elif tõmbamas == "hoia":
                print("Nüüd võtab diiler kaardi.")
                dealer_hand.append(Dealing.draw(playing_deck))
                graafika.create_card_image(dealer_hand, "dealer")
                dealer_score = Dealing.kokku(dealer_hand)
                while dealer_score < 16:
                    dealer_hand.append(Dealing.draw(playing_deck))
                    graafika.create_card_image(dealer_hand, "dealer")
                    dealer_score = Dealing.kokku(dealer_hand)
                print("Diileri käsi on hetkel:" + Dealing.käsi(dealer_hand))
                print("Diileri käe skoor: "+ str(dealer_score)+"\n")
                if len(dealer_hand) > 4:
                    ("Diiler ei läinud viie kaardiga lõhki. Kaotasite!")
                    mängimas = False
                    player_võit = False
                elif dealer_score > 21:
                    print("Diiler läks lõhki. Te võitsite!")
                    player_võit = True
                    mängimas = False
                elif dealer_score >  player_score:
                    print("Diileril suurem käsi, kui teie teie käsi. Kaotasite!")
                    player_võit = False
                    mängimas = False
                else:
                    print("Teie teie käsi on suurem, kui diileri. Võitsite!")
                    player_võit = True
                    mängimas = False
        if panustamine == True:
            if player_võit2 is not None:
                if player_võit2 == True:
                    player_raha = player_raha + player_panus2
                elif player_võit2 == False:
                    player_raha = player_raha - player_panus2
                if player_võit == True:
                    player_raha = player_raha + player_panus
                elif player_võit == False:
                    player_raha = player_raha - player_panus
            else:
                if player_võit == True:
                    player_raha = player_raha + player_panus
                elif player_võit == False:
                    player_raha = player_raha - player_panus
            if player_raha < 1:
                print("Teil pole enam krediiti. Mäng läbi!")
                break
    mängib_uuesti = input("\nVajutage enter, kui soovite uuesti mängida, 'ei' kui ei soovi edasi mängida!\n>>>>").lower()
    if mängib_uuesti == "ei":
        print("Tänan mängimast!")
        mängib = False
    else:
        print("\n<<<<Uus mäng>>>>\n")
