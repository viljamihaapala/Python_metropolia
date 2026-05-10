#  + ,   -,   * (kerto),   /(jako desi),  //(jako koko),   % (jakojäännös) ja  **(potenssi)



# Alla oleva ohjelma kysyy lämpötilan Fahrenheit-asteina ja muuntaa sen Celsius-asteiksi.
# Muunnos tehdään siten, että Fahrenheit-asteista vähennetään 32, ja erotus kerrotaan vakiolla 5/9.

fahrenheit_str = input("Anna lämpötila fahrenheit-asteina: ")    #str, koska muuttuja teksti
fahrenheit_str =float(fahrenheit_str)     #float = muuntaa teksin desimaaliluvuksi
celcius = (fahrenheit_str-32)*(5/9)
print("Lämpötila celcius asteina: " + str(celcius))




#Kirjoita ohjelma, joka: Kysyy käyttäjältä painon kiloina.Muuntaa käyttäjän antaman arvon liukuluvuksi (float).
#Laskee painon paunoina (pounds) kaavalla:paunat =kilot×2.204

kilograms_str = input("Anna paino kiloina: ")    #Muuttuja on teksti string
kilograms_str = int(kilograms_str)             #Muunnetaan muuttuja kokonaisluvuksi
pounds = (kilograms_str*2.204)
print("Paino paunoina: " + str(pounds))



