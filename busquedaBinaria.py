#Implementar busqueda Binaria
l = [99,88,1,20,55,2,95,78,55,22]

def search(l,obj):
  l = sorted(l)
  inicio = 0
  fin = len(l)-1
  mitad = inicio + fin // 2
  if obj == l[mitad]:
     print("Found")
  else:
      print("not found")

search(l, 55)



 


