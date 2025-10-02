#contar cuantas palabras hay en una oracion

def wordCounter(word):
 count = 1
 for x in word:
  if " " in x:
   count += 1
 print(f"la oracion {word} tiene {count} palabras")  
  
wordCounter("hola mundo como estan")