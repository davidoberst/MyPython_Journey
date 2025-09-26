#cuantas vocales tiene una palabra

def contador(palabra):
 vocales = ["a","e","i","o","u"]
 count = 0
 for x in palabra:
  if x in vocales:
   count = count + 1
 print(count)

contador("cabeza")
   
   

  
  
  