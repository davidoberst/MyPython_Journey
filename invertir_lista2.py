#inverir lista sin usar ::-1


#forma con ::-1
ls = [1,2,3,4,5,6,7,8,9,10]
revert = ls[::-1]
print(f"lista invertida con ::-1 : {revert}")

#forma sin ::-1

invertida = list(reversed(ls))
print(invertida)  # [5, 4, 3, 2, 1]