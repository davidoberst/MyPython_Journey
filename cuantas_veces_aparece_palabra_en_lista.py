#contar cuantas veces aparece cada letra en una plabra

def contador(palabra):
    count = {}
    for x in palabra:
        if x in count:   # si ya existe la letra en el diccionario
            count[x] += 1
        else:            # si no existe, la inicializa en 1
            count[x] = 1
    return count

print(contador("palabra"))

#alternativa

from collections import Counter
print(Counter("alamo"))

