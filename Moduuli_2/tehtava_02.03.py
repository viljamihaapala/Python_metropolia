# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

import math
kanta = float(input("Anna suorakulmion kannan pituus: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

a = kanta*korkeus
p = 2*kanta + 2*korkeus

print(f"Suorakulmion pinta-ala on + {a} ")
print(f"Suorakulmion piiri on + {p} ")


# TAI

kanta = float(input("Anna suorakulmion kannan pituus: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

a = kanta*korkeus
p = 2*kanta + 2*korkeus

print("Suorakulmion pinta-ala on " + str(a))
print("Suorakulmion piiri on " + str(p))