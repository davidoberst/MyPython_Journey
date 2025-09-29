#calcular la potencia de un numero sin usar **
print(f"potencia a conseguir = {2**5}")
def c(n, p):
    result = 1
    for i in range(p):
        result = result * n   
    return result
print(c(2, 5))

