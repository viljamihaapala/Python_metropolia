import random
koodi1 = "". join(str(random.randint(0,9)) for _ in range (3))
koodi2 = "". join(str(random.randint(1,6)) for _ in range (4))

print("Kolminumeroinen koodi: ", koodi1)
print("kolminumeroinen koodi: ", koodi2)
