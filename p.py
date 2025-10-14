#Implementar busqueda lineal version

def search(lista,objetivo):
    encontrado = False
    for x in range(len(lista)):
        if lista[x] == objetivo:
            print(f"Objetivo encontrado en la posicion {x}")
            encontrado = True
            break
    if not encontrado:
        print("el objetivo no esta en la lista")

l = [2,99,88,55,87,6,1,7]
search(l,6)
search(l,999)
        
        
    