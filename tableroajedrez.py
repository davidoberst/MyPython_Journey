#Dibujar un tablero de ajedrez en texto


colors = {"white":"⬜",
          "black":"⬛"}
jn = ("".join(colors.values()))
jn2 = ("".join(colors.values())[::-1])
file = jn*4
file2 = jn2*4
for x in range(4):
    print(file)
    print(file2)
    
 


    
   