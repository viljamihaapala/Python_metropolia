#  Kirjoita ohjelma, joka pyytää käyttäjältä sanoja. Jos käyttäjä kirjoittaa sanan "loppu",
# ohjelma tulostaa muodostuneen tarinan ja lopettaa.

tarina = ""
while True:
    sana = input("Anna sana: ")

    if sana == "loppu":
        break

    tarina = tarina + sana + " "

print("Tarinasi:")
print(tarina)