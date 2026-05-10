#  Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. Jos luku on pienempi
#  kuin nolla,
# ohjelma tulostaa viestin "Virheellinen numero". Jos luku on suurempi kuin nolla,
# ohjelma tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. Molemmissa tapauksissa
# ohjelma kysyy sen jälkeen uutta lukua.
# Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja poistuu silmukasta.


from math import sqrt
while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        break

    if luku < 0:
        print("Virheellinen numero")

    else:
        print("Neliöjuuri on", sqrt(luku))
        