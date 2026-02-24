pituus = int(input("Anna lohen pituus (cm): "))

if pituus < 60:
     print("Lohi on alamittainen ja se on vapautettava.")

if pituus >= 60:
    print("Lohi on täysimittainen ja voin syödä sen. ")

puuttuu = 60-pituus
print("Lohi on alamittainen, siitä puuttuu", puuttuu, "cm.")







