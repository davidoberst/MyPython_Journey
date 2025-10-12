subArray = [4, 12, 44, -55, 22, 10, -1, 8]

print(f"Numero de elementos en el Arreglo : {len(subArray)}")
print("")

inicio = 0
count = 0
arr = []

# Recorremos de 2 en 2
for i in range(inicio, len(subArray), 2):
    if i + 1 < len(subArray):  # Verificamos que haya un siguiente elemento
        a = subArray[i] + subArray[i+1]
        arr.append(a)
        print(a)

print("")
print("Suma de cada par:", arr)


