#Pyhton kielen muuttujan perustyypit
# merkkinojo (string)
# luku (number), joka voi olla kokonaisluku 4, pitkä kokonaisluku 12345.., liukuluku 4.0 tai 4.5 tai kompleksiluku 3-2i
# totuusarvo (boolean), joka voi olla True tai False
# lista (list)
# monikko (tuple)
# sanakirja (dictionary)



# Luku esim.
# kokonaisluvun arvoalue on < pitkän kokonaisluvun arvoalue (todella suuret/pienet arvot)
eka = -9          # arvoalue -2147483648 >= 2147483647
toka = 12_456_898 # ( 12_456  alaviiva symboli ei pakollinen)
kolmas = 4.5
neljäs = -4+2j    # j-kirjain imag.osa

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)

viides = 10
kuudes = 123456789
seitsämäs = 6,50
kahdeksas = 5+10j

print(viides)
print(kuudes)
print(seitsämäs)
print(kahdeksas)
print(kahdeksas.real)
print(kahdeksas.imag)