#Ejercicios de Logica #6 - Verificar si una palabra es palindromo

while True:
    palabra = input("Escribe tu palabra : ")
    procesamiento = palabra[::-1]
    if palabra == procesamiento:
        print("palindromo")
    else:
        print("no es palindromo")

        