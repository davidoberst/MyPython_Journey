#genera la tabla de multiplicar de un numero
def multiplicacion(num):
    nums = [1,2,3,4,5,6,7,8,9,10]
    for x in nums:
      resultado =  num * x
      print(f"{num} x {x} = {resultado} ")

multiplicacion(2)