#Crear un cronometro en python 
import time
stop = False
count_sec = 0
count_min = 0
tme = 0
while stop == False:
 count_sec += 1

 if count_sec >= 60:
  count_min += 1
  count_sec = 0

 print(f"\rCount : {count_min}:{count_sec:02}", end='', flush=True)
 time.sleep(1)

  



  
  
 

