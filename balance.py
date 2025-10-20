#Verificar balance de parentesis en una expresion
def balance(expresion):
 count = 0
 for x in expresion:
   if "(" in x :
    count += 1
   if ")" in x :
    count -= 1
 if count == 0:
  print("Yes")
 else:
  print("No")

print("\n Balanceados :")
balance("(2+2)")
balance("(a+(b-c))")
balance("((3+5)*(2-1))")
balance("(x+y)-(a+b)")
balance("((a+b)+((c+d)))")


print("\n No Balanceados :")
balance("(2+2")
balance("((a+b)")
balance("(a+(b-c)")
balance("((3+5)*(2-1)")


print("\n No Balanceados (Negativos) :")
balance("(2+2))")
balance("a+b)")
balance("((a+b)))))")
balance(")a+(b-c)")





 
