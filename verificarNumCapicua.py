#verificar si un numero es capicua (palindromo)

def verification(n):
    v = str(n)[::-1]
    n = str(n)
    if n == v:
        print("capicua!")
    else:
     print("no es capicua")

verification(22)
verification(25)

