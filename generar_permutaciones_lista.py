#generar todas las permutaciones de una lista

from itertools import permutations

lista = [1, 2, 3]

for p in permutations(lista):
    print(p)
