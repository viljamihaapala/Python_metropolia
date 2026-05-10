#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
# Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

import math

Numero_1 = int(input("anna numero 1: "))
Numero_2 = int(input("anna numero 2: "))
Numero_3 = int(input("anna numero 3:"))

summa = Numero_1 + Numero_2 + Numero_3
tulo = Numero_1 * Numero_2 * Numero_3
Keskiarvo = summa/3

print("Keskiarvo on, " + str(Keskiarvo))
print("Tulo on, " + str(tulo))
print("Summa on, " + str(summa))

