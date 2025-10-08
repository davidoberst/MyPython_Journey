#Convertidor de Numeros Enteros a Romanos

n = 7   #numero a convertir

values = {          #valores de numeros romanos a entero
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

usingNumber = {}

for simbol, value in values.items():
    if value <= n:
     usingNumber[simbol] = value
     break
rslt = n - value
print(rslt)
    
