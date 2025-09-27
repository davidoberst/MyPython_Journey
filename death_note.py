
#Death Note en Python

tv = [
    "Haruto",
    "Ren",
    "Yuto",
    "Takumi",
    "Souta",
    "Kaito",
    "Daiki",
    "Ryusei",
    "Itsuki",
    "Sho"
]

print("--------LISTA DE CRIMINALES-----------")
for x in tv:
     print(x)
print("")

while True:

 deathNote = input("---->  ")

 if deathNote in tv:
        print(f"Criminal {deathNote} ELIMINADO")
        tv.remove(deathNote)
        print("lista actualizada")
        for y in tv:
            print(y)
 elif not deathNote:
     print("Todos los criminales fueron eliminados")
     break;
 else:
        print(f"El criminal {deathNote} NO ESTA EN LA LISTA")
        
        