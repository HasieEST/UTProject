import random, Dealing

print("Kas soovite mängida panustega")
kas_panustada = input("Jah, kui soovite.").lower()
print("")
if kas_panustada == "jah":
    panustamine = True
    player_raha = 100
else:
    panustamine = False

playing = True
while playing is True:
    playing_deck = [("Ärtu äss", 11, "pilt"),("Ärtu kaks", 2, "pilt"), ("Ärtu kolm", 3, "pilt"), ("Ärtu neli", 4, "pilt"), ("Ärtu viis", 5, "pilt"), ("Ärtu kuus", 6, "pilt"), ("Ärtu seitse", 7, "pilt"), ("Ärtu kaheksa", 8, "pilt"), ("Ärtu üheksa", 9, "pilt"), ("Ärtu kümme", 10, "pilt"), ("Ärtu poiss", 10, "pilt"), ("Ärtu emand", 10, "pilt"), ("Ärtu kuningas", 10, "pilt"),("Risti äss", 11, "pilt"),("Risti kaks", 2, "pilt"), ("Risti kolm", 3, "pilt"), ("Risti neli", 4, "pilt"), ("Risti viis", 5, "pilt"), ("Risti kuus", 6, "pilt"), ("Risti seitse", 7, "pilt"), ("Risti kaheksa", 8, "pilt"), ("Risti üheksa", 9, "pilt"), ("Risti kümme", 10, "pilt"), ("Risti poiss", 10, "pilt"), ("Risti emand", 10, "pilt"), ("Risti kuningas", 10, "pilt"),("Potti äss", 11, "pilt"),("Potti kaks", 2, "pilt"), ("Potti kolm", 3, "pilt"), ("Potti neli", 4, "pilt"), ("Potti viis", 5, "pilt"), ("Potti kuus", 6, "pilt"), ("Potti seitse", 7, "pilt"), ("Potti kaheksa", 8, "pilt"), ("Potti üheksa", 9, "pilt"), ("Potti kümme", 10, "pilt"), ("Potti poiss", 10, "pilt"), ("Potti emand", 10, "pilt"), ("Potti kuningas", 10, "pilt"),("Ruutu äss", 11, "pilt"),("Ruutu kaks", 2, "pilt"), ("Ruutu kolm", 3, "pilt"), ("Ruutu neli", 4, "pilt"), ("Ruutu viis", 5, "pilt"), ("Ruutu kuus", 6, "pilt"), ("Ruutu seitse", 7, "pilt"), ("Ruutu kaheksa", 8, "pilt"), ("Ruutu üheksa", 9, "pilt"), ("Ruutu kümme", 10, "pilt"), ("Ruutu poiss", 10, "pilt"), ("Ruutu emand", 10, "pilt"), ("Ruutu kuningas", 10, "pilt")]

#diiler ja mängija andmed
player_hand = []
player_score = 0
player2_hand = []
player2_score = 0
dealer_hand = []
dealer_score = 0

dealer_hand.append(Dealing.draw(playing_deck))
player_hand.append(Dealing.draw(playing_deck))
player_hand.append(Dealing.draw(playing_deck))
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
        player_hand2 = player_hand.pop()
        player_hand.append(Dealing.draw(playing_deck))
        player_hand2.append(Dealing.draw(playing_deck))
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
                dealer_score = Dealing.kokku(dealer_hand)
                while dealer_score < 16:
                    dealer_hand.append(Dealing.draw(playing_deck))
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
            player_score = Dealing.kokku(player_hand2)
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
            dealer_score = Dealing.kokku(dealer_hand)
            while dealer_score < 16:
                dealer_hand.append(Dealing.draw(playing_deck))
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
    mängimas = False
else:
    print("\n<<<<Uus mäng>>>>\n")
