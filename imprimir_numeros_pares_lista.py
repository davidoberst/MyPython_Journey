#imprimir los numeros pares de una lista

list = [1,8,2,5,4,22,66,45,32]
print("numeros pares encontrados:")
for x in list:
    if x % 2 == 0:
     print(x)
     

#imprimir numeros impares de una lista 

list2 = [1,8,2,5,4,22,66,45,32]
print("numeros impares encontrados :")
for x in list:
   if not x %2 == 0:
      print(x)