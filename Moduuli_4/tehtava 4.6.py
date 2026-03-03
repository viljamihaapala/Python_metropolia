import random

N = int(input("Kuinka monta pistettä arvotaan? "))

n = 0

for _ in range(N):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        n += 1

pi_likiarvo = 4 * n / N

print(f"Piin likiarvo: {pi_likiarvo}")
