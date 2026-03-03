while True:
    tuumat = float(input("Anna tuumat (negatiivinen lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break

    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa = {sentit} cm")
