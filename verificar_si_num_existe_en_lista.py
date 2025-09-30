#Verificar si un numero existe en una lista
lista = [2,5,6,7,8,10]
while True:
 entrada = int(input("Escriba el numero que quiere verificar : "))
 if entrada in lista:
        print("esta")

 else:
        print("no esta")