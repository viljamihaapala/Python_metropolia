pituus = float(input("Anna lohen pituus (cm): "))

if pituus > 60:
    print("Lohi on täysimittainen ja voin pitää sen. ")

if pituus <= 60:
    print("Lohi on alamittainen ja se on vapautettava. ")

puuttuu = 60-pituus
print("Lohi on alamittainen, pituudesta puuttuu", puuttuu, "cm.")


