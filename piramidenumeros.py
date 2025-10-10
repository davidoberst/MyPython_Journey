#imprimir una pirmaide de numeros

def piramide_numeros(n):
    for i in range(1, n + 1):
        espacios = " " * (n - i)       
        numeros = " ".join(str(x) for x in range(1, i + 1))      
        print(espacios + numeros)

piramide_numeros(5)
