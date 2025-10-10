# Convertidor de números enteros a romanos
import time

# ASCII art de un gato
gato = r"""
 /\_/\  
( o.o ) hola neuronita artificial!
 > ^ <
"""

print(gato)
time.sleep(1)

print("-----------------------------------\n")
time.sleep(1)

values = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}

while True:
    entrada = input("Eli, digita el número a convertir o escribe 'exit' para salir ----->  ")
    time.sleep(2)
    
    if entrada.lower() == "exit":
        print("\n¡chao neuronita!")
        time.sleep(2)
        break
    
    if not entrada.isdigit():
        print("\nPor favor, ingresa un número válido.\n")
        time.sleep(2)
        continue
    
    n = int(entrada)
    result = ""
    rslt = n
    
    while rslt > 0:
        for simbol, value in values.items():
            if value <= rslt:
                result += simbol
                rslt -= value
                break  
    
    print(f"\nEl número {n} en romano es: {result}\n")
    time.sleep(2)
