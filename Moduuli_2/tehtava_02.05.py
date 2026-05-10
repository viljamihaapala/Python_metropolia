# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

leiviska_1 = float(input("Anna massa leiviskänä: "))
naula_2 = float(input("Anna massa nauloina: "))
luoti_3 = float(input("Anna massa luoti: "))

leiviska_1_grammmoina = 20*naula_2
naula_2_grammoina = 32*luoti_3
luoti_3_grammoina = 13.3

# koko massa grammoina
massa_grammoina = (13.3*32*20*leiviska_1) +  (32*13.3*naula_2) + (13.3*luoti_3)

kilot = int(massa_grammoina//1000)
grammat = (massa_grammoina %1000)

print(f"kilogrammat {kilot} ja {grammat:.2f} grammaa. ")




