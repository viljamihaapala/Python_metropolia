import math

def yksikkohinta(halkaisija_cm, hinta_euro):
    sade = halkaisija_cm / 2
    pinta_ala_m2 = math.pi * (sade ** 2) / 10000  # cm² → m²
    return hinta_euro / pinta_ala_m2

def main():
    print("Anna ensimmäisen pizzan tiedot:")
    d1 = float(input("Halkaisija (cm): "))
    h1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    d2 = float(input("Halkaisija (cm): "))
    h2 = float(input("Hinta (€): "))

    y1 = yksikkohinta(d1, h1)
    y2 = yksikkohinta(d2, h2)

    print(f"\nPizzan 1 yksikköhinta: {y1:.2f} €/m²")
    print(f"Pizzan 2 yksikköhinta: {y2:.2f} €/m²")

    if y1 < y2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif y2 < y1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat täsmälleen yhtä edullisia.")

main()
