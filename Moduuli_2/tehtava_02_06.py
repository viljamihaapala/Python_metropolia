# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon
# koodia:
# kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
# Vihje: tutustu random.randint()-funktion käyttöön.

# avataan työkalupaketti "Moduuli" = satunnaisluku kirjasto



# Kolminumeroinen koodi (0-9)
import random
numero_1 = random.randint(0,9)
numero_2 =random.randint(0,0)
numero_3 =random.randint(0,9)

print("Koodi on:", numero_1, numero_2, numero_3)



# Nelinumeroinen koodi (1-6)
print("Koodi on: ", random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6))



