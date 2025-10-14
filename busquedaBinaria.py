#Implementar busqueda Binaria
# = [1, 2, 20, 22, 55, 55, 78, 88, 95, 99]


l = [99,88,1,20,55,2,95,78,55,22]
def search(l,obj):
  l = sorted(l)
  inicio = 0
  fin = len(l)-1
  mitad = inicio + fin // 2
  if obj == l[mitad]:
     print("Found")
  while obj > l[mitad]:
     mitad += 1
     if obj == l[mitad]:
        print(f"Object {l[mitad]} founded in position ")
        break
     
  while obj < l[mitad]:
     mitad -= 1
     if obj == l[mitad]:
        print(f"Object {l[mitad]} founded in position ")
        break
    

 
     
     
  
     

search(l,99)



 


