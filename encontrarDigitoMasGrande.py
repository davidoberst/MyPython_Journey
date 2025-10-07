#Encontrar el digito mas grande de un numero

def digito_mas_grande(n):
    n = abs(n) 
    return max(int(d) for d in str(n))

print(digito_mas_grande(5729))   # 9
print(digito_mas_grande(-834))   # 8
print(digito_mas_grande(1002))   # 2
