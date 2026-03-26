def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko + 1):
          print(" " * (koko - i) + "*" * (2 * i - 1))

kuusi(5)
