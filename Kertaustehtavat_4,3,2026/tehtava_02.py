# Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän.
# Ohjelma tulostaa
# päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina,
# jolloin tuntipalkka on kaksinkertainen.

tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tunnit: "))
viikonpäivä = int(input("Anna viikonpäivä: "))

if viikonpäivä.lower()== "sunnuntai":
    päiväpalkka = tuntipalkka*tunnit*2

else:
    tuntipalkka = tunnit*tuntipalkka

print("Päiväpalkka on", päiväpalkka, "€")