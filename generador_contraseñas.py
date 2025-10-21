#Generador de Contraseñas Seguras
import random as rd
caracteres = 12
letras_mayus = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letras_minus = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                "n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = ["1","2","3","4","5","6","7","8","9"]
simb = ["!","@","#","$","%","^","&","*","(",")",
            "-","_","=","+","[","]","{","}",";",":",
            "'",",",".","<",">","/","?","|","~"]

def choices():
 passw = ""
 for x in range(12):
   x = rd.choice(letras_mayus + letras_minus + nums + simb)
   passw += x
 print(passw)


choices()