#Contar cuantas veces aparece un numero en una lista

lista = [22,55,66,888,776,3,5,6,7,88,3,2,2,1,0,7]
for x in range(len(lista)):
 contador = 0
 for y in range(len(lista)): 
  if lista[x] == lista[y]:
   contador += 1
   print(f"el numero {x} aparece {contador} veces")
   
