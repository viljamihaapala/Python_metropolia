#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon
# koodia:
# 1. Viisinumeroinen koodi, Jokainen numeromerkki on väliltä 0…4.
# 2. Kolminumeroinen koodi, Jokainen numeromerkki on väliltä 5…9.

import random

nro_1 =random.randint(0,4)
nro_2 =random.randint(0,4)
nro_3 =random.randint(0,4)
nro_4 =random.randint(0,4)
nro_5 =random.randint(0,4)
print('Viisinumeroinen koodi on: ', nro_1, nro_2, nro_3, nro_4, nro_5 )

# TAI

print("Kolminumeroinen koodi on: ", random.randint(5,9), random.randint(5,9), random.randint(5,9))


# Arvo luku (1-100)
print("Luku 1-100 välillä: ", random.randint(1,100))


