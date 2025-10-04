#Rotar una lista n posiciones a la dereca
print("*"*50)
print("rotar lista derecha")
ls = [10,20,30,40,50,60]

print(ls)
walk = int(input("veces a recorrer -->"))
del ls[0:walk]
print(ls)
print("*"*50)
