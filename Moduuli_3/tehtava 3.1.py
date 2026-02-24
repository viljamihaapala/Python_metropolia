pituus = int(input("Anna kuhan pituus(cm): " ))
if pituus <=37:
    puuttuu = 37 - pituus
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu: .2f} cm.")

else:
    print ("Kuha on sallitun mittainen.")

