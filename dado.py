#Generar el lanzamiento de dos dados

import random as rd
dado1 = rd.randint(1,7)
dado2 = rd.randint(1,7)
print("-"*50)
print("LANZAMIENTO")
print("-"*50)
print(f"El dado uno saco : {dado1}")
print(f"El dado dos saco : {dado2}")
print(f"RESULTADO : {dado1 + dado2}")


