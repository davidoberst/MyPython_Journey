# Convertidor de números enteros a romanos

n = 4
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
result = ""
rslt = n
while rslt > 0:
    for simbol, value in values.items():
        if value <= rslt:
            result += simbol
            rslt -= value
            break  
print(result)  