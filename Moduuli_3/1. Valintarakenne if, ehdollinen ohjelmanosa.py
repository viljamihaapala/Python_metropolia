# If eli vaihtoehtoinen suorituspolku
# Python-kielessä ehdollisesti suoritettava ohjelmanosa toteutetaan if-lauseen avulla. L
# Pseudokoodi
# Sisennetään "yhden askeleen" eli 4 x enter


# Ohjelma kysyy käyttäjältä taskussa olevan rahamäärän ja ilmoittaa tälle, jos rahat riittävät viiden euron hintaisen latten ostoon.
# Jos rahat eivät riitä, ohjelma ei ilmoita mitään:

rahat = int(input("Paljonko sinulla on rahaa taskussa:"))
if rahat>=5:
             print("Voit ostaa latten.")

#Ohjelma kysyy käyttäjältä, paljonko hänellä on rahaa mukana venereissulla, ja ilmoittaa hänelle,
# jos rahat riittävät 12 euron hintaiseen jigi‑settiin.Jos rahat eivät riitä, ohjelma ei ilmoita mitään.

rahat = float(input("Paljonko sinulla on rahaa mukana venereissulla: "))
if rahat>=12:
    print("Voit ostaa jigisetin.")


