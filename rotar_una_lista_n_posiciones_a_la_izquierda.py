

#rotar una lista n posiciones a la izquierda

ls2 = [10,20,30,40,50,60]
ls2 = ls2[::-1]
print("*"*50)
print("rotar lista izquierda")
walk2 = int(input("veces a recorrer -->"))
del ls2[0:walk2]
print(ls2)
 
 