# Kirjoita ohjelma keittokauppaa varten: Ohjelma kysyy käyttäjän nimen.
# Jos nimi on
# jokin muu kuin "Matti", ohjelma kysyy keittoannosten määrän ja tulostaa
# kokonaishinnan. Yhden annoksen hinta on 5,90.

nimi = input("Anna nimi: ")
if nimi != "Matti":
    määrä = int(input("Anna määrä: "))
    hinta = määrä*5.90
    print("Kokonaishinta on ", hinta)



