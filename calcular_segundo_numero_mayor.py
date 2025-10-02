#Calcular el seugndo numero mayor de una lista

list = [2,4,55,88,77,95,10,90,2999,2998]
print(f"el numero mayor de la lista es {max(list)}")
list.remove(max(list))
print(f"ahora el numero mayor de la lista es {max(list)}")
 