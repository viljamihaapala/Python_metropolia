def yhteenlasku(a, b):
    return a + b

def vahennyslasku(a, b):
    return a - b

def kertolasku(a, b):
    return a * b

def jakolasku(a, b):
    if b == 0:
        return "Virhe: Nollalla ei voi jakaa!"
    return a / b

def laskin():
    print("--- Tervetuloa käyttämään laskinta ---")

    while True:
        print("\nValitse toiminto:")
        print("1: Yhteenlasku (+)")
        print("2: Vähennyslasku (-)")
        print("3: Kertolasku (*)")
        print("4: Jakolasku (/)")
        print("0: Lopeta ohjelma")

        valinta = input("Syötä valintasi (0-4): ")

        if valinta == "0":
            print("Kiitos laskimen käytöstä. Heippa!")
            break

        if valinta in ("1", "2", "3", "4"):
            try:
                luku1 = float(input("Anna ensimmäinen luku: "))
                luku2 = float(input("Anna toinen luku: "))

                if valinta == "1":
                    print(f"Tulos: {luku1} + {luku2} = {yhteenlasku(luku1, luku2)}")
                elif valinta == "2":
                    print(f"Tulos: {luku1} - {luku2} = {vahennyslasku(luku1, luku2)}")
                elif valinta == "3":
                    print(f"Tulos: {luku1} * {luku2} = {kertolasku(luku1, luku2)}")
                elif valinta == "4":
                    tulos = jakolasku(luku1, luku2)
                    if isinstance(tulos, str):
                        print(tulos)
                    else:
                        print(f"Tulos: {luku1} / {luku2} = {tulos}")
            except ValueError:
                print("Virhe: Syötäthän vain numeroita.")
        else:
            print("Virheellinen valinta, yritä uudelleen.")

laskin()
