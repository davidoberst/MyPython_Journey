#Implementar busqueda Binaria
l = [99,88,1,20,55,2,95,78,55,22]

def search(l, obj):
    l = sorted(l)
    inicio = 0
    fin = len(l) - 1

    while inicio <= fin:
        mitad = (inicio + fin) // 2

        if l[mitad] == obj:
            print(f"Object {l[mitad]} found at position {l.index(l[mitad])}")
            return
        elif l[mitad] < obj:
            inicio = mitad + 1
        else:
            fin = mitad - 1

    print("Object not found")

search(l, 55)
search(l, 2)
search(l, 95)


 


