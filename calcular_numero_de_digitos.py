#Calcular el numero de digitos de un numero

def num_digitos(n):
    return len(str(abs(n)))  

# abs Sirve para obtener siempre el número positivo equivalente de un valor, sin importar si es negativo o positivo.

#sin abs
def ret(n):
    print(len(str(n)))
ret(-550)