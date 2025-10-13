ls = [1,2,3,4,5,6,7,9,10]

for i in range(1, 11):  # del 1 al 10
    if i not in ls:
        print(f"El número que falta es: {i}")
