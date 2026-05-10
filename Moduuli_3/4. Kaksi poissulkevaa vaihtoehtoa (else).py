# Esim 1.
# Tarkastellaan esimerkkiohjelmaa, joka ilmoittaa, jos lääkettä saa antaa potilaalle.
# Lääkkeen käyttö on sallittua, kun potilas on aikuinen. Käyttö on sallittua myös, jos potilas on vähintään 15-vuotias
# ja hänen painonsa on vähintään 55 kiloa. Seuraava ohjelma kysyy aluksi potilaan iän.
# Jos ikä on vähintään 15 mutta alle 18 vuotta, ohjelma kysyy myös painon. Lopuksi ohjelma ilmoittaa käyttäjälle,
# jos lääkkeen käyttö on sallittua.

# if lisätään else, jolloin saadaan aina vastaus!

ikä = int(input("Anna potilaan ikä: "))
if 15 >=ikä<=18:
    paino = float(input("Anna potilaan paino kg: "))
if (ikä>=18 or ikä>15 and paino>=55):
    print("Lääkkeen saa antaa potilaalle")
else:                                              # else viittaa viimeiseen "if lauseeseen"
    print("Lääkettä ei saa antaa!")



# Esim 2.
# Ohjelma kysyy ensin lapsen iän. Jos ikä on vähintään 12 mutta alle 16 vuotta, ohjelma kysyy lisäksi, kuinka paljon rahaa lapsella on.
# Lopuksi ohjelma ilmoittaa, voiko lapsi ostaa energiajuoman. Energiajuoman ostaminen on sallittua, jos lapsi on vähintään 16‑vuotias.
# Ostaminen on sallittua myös, jos lapsi on vähintään 12‑vuotias ja hänellä on vähintään 3 euroa rahaa.

ikä = int(input("Anna lapsen ikä: "))
if 12>=ikä<16:
    raha = float(input("Anna lapsen omistama rahamäärä: "))
if 16>=ikä or ikä>=12 and raha>=3:
    print("Lapsi saa ostaa energiajuoman! ")
else:
    print("Lapsi ei saa ostaa energiajuomaa! ")