pituus = int(input("Ahvenen pituus:"))

if pituus < 25:
    print("Ahven on alamittainen ja se on vapautettava: ")

if pituus >= 25:
    print("Ahven on täysimittainen ja voin syödä sen: ")

puuttuu = 25-pituus
print("Ahven on alamittainen ja pituudesta puuttuu", puuttuu,"cm.")



