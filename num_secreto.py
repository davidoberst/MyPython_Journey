#Crear un programa que adivine un numero secreto

import random as rd
n = rd.randint(1,100)
print("Adivina el numero secreto!")
while True:
 entry = int(input("Cual crees que es? ---> : "))
 if entry < n:
    print("el numero es mayor")
 elif entry > n:
    print("el numero es menor")
 else:
   print("correcto, el numero era ese, ganaste")
   break;

