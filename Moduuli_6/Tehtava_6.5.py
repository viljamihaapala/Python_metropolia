
def karsi_parittomat(numerot):
    parilliset = []
    for n in numerot:
        if n % 2 == 0:
            parilliset.append(n)
    return parilliset

def main():

    luvut = [3, 8, 11, 4, 7, 10, 2]

    karsittu = karsi_parittomat(luvut)

    print("Alkuperäinen lista:", luvut)
    print("Karsittu lista (vain parilliset):", karsittu)


main()
