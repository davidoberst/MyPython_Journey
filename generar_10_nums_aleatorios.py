#generar 10 numeros aleatorios

import random as rd
nums = range(1,11)
for x in nums:
 print(rd.choice(nums))
