#ordenar una lista sin usar .sort()

lista = [21,22,11,0,1,5,9,44,80]
for x in range(len(lista)):
 for y in range(len(lista)):
    if lista[x] < lista[y]:
     lista[x],lista[y] = lista[y],lista[x]
     print(lista)

     
