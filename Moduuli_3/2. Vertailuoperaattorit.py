# >	suurempi kuin
# <	pienempi kuin
# >=	suurempi tai yhtäsuuri kuin
# <=	pienempi tai yhtäsuuri kuin
# ==	yhtä suuri kuin
# !=	eri suuri kuin

# Voidaan ketjuttaa 170 <= 180
# Voidaan käyttää merkkijonoille m1<m2

# esim.
pituus = int(input("Anna pituus: "))
if 170 <=pituus<=185:
    print("Olet keskipitkä")



suutari = input("Anna suutarin nimi: ")
raatali = input("Anna raatalin nimi: ")
if suutari == raatali:                                           # Muista (:!)
    print("Ei voi olla totta, suutari ja raatali ovat kaimoja")  # Muista sisennys Tab/ 4xenter


vene = input("Anna veneen merkki: ")
moottori =input("Anna moottorin merkki: ")
if vene==moottori:
    print("Saat kokonaispaketista paremma tarjouksen")


vapa = input("Anna vavan merkki: ")
kela = input("Anna kelan merkki: ")
if vapa != kela:
    print("Kokonaislaatu kärsii")

