import pyfiglet

print(pyfiglet.figlet_format("Calculator", font="small"))

pos = 0
temp = ""
digit1 = []
digit2 = []

userInput = input("----->  ")
op = ""
for i, x in enumerate(userInput):
    if x.isdigit():
        temp += x
    elif x in "+-*/":
        if temp:
            digit1.append(int(temp))
            temp = ""
        op = x
        pos = i
        break

temp2 = ""
for y in userInput[pos+1:]:
    if y.isdigit():
        temp2 += y
if temp2:
    digit2.append(int(temp2))

if op == "+":
    r = digit1[0] + digit2[0]
elif op == "-":
    r= digit1[0] - digit2[0]
elif op == "*":
    r = digit1[0] * digit2[0]
elif op == "/":
    r = digit1[0] / digit2[0]

print("Resultado:", r)


  
 
 
 
  
