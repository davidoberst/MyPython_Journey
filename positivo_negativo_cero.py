#verificar si un numero es positivo, negativo o 0


def verificacion(num):
 if num == 0:
  print("el numero es 0")
 elif num >= 0:
  print("positivo")
 else:
  print("negativo")

verificacion(0)
verificacion(-5)
verificacion(22)