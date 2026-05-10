# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math

r = float(input("Anna ympyrän säde: "))
a= math.pi*r**2
print(f" ympyrän, jonka säde on {r} pinta-ala on {a} ")


# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden ja tulostaa sen pinta‑alan.

kanta = float(input("Anna kannan pituus: "))
korkeus = float(input("Anna kannan korkeus: "))
a = kanta*korkeus
print(f" Suorakulmion pinta-ala on: {a:6.5f} ")
