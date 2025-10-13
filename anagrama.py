#Cpmaprar si dos palabras son anagramas

def comparacion(word1,word2):
 word1 = word1.lower()
 word2 = word2.lower()
 orden1 = sorted(word1)
 orden2 = sorted(word2)
 if len(word1) == len(word2) and orden1 == orden2:
  print("anagrama")
 else:
  print("no anagrama")
comparacion("listen","silent")
comparacion("listen","helloworld")

