# Monenko desimaalin tarkkuudella liukuluvut esitetään, tai
# Monenko merkin suuruinen tila vaikkapa merkkijonolle varataan.

#Esim.
fahrenheit_str = input("Anna lämpötila fahrenheit-asteina:")
fahrenheit_str = float(fahrenheit_str)
celcius = (fahrenheit_str-32)*(5/9)
print("Lämpötila celcius asteina: " +str(celcius))
# ->Anna lämpötila fahrenheit-asteina:102
# ->Lämpötila celcius asteina: 38.88888888888889

# Nyt celsius-lämpötila näytetään aina kahden desimaalin tarkkuudella:
print(f"Lämpötila celcius asteina: {celcius: 6.2f}")
# f" = tulostettava merkkijono sisältää muotoiltavia lausekkeita.
# 6.2 = tulos esitetään kuusi merkkiä leveässä kentässä, ja liukuluvun esitystarkkuus on kaksi desimaalia.

# esim:
# .5f : liukuluku viiden desimaalin tarkkuudella
# 10.2f : liukuluku kahden desimaalin tarkkuudella kymmenen merkkiä leveään kenttään
# <20s : merkkijono 20 merkkiä leveään kenttään vasemman reunan mukaan tasattuna
# 8d : kokonaisluku kahdeksan merkkiä leveään kenttään