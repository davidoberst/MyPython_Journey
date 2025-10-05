#crear un sistema de login con usuarios y contraseñas
#validar una contraseña (minimo 8 caracteres, 1 numero y una mayuscula)

import pyfiglet
import time

accs = {"user":"password"} 

def login():
  print(pyfiglet.figlet_format("Login", font="small"))
  usr_log = input("Username ---> " )
  passw_log= input("Password ---> ")
  if accs.get(usr_log) == (passw_log):
    print("found")
  else:
    print("not found")

def createAccount():
  print(pyfiglet.figlet_format("Create an account", font="small"))
  while True:
   usr = input("Username ---> ")
   passw = input("Password ---> ")
   if len(passw) >= 8 and any(c.isupper() for c in passw) and any(c.isdigit() for c in passw):
     accs[usr] = passw
     print("Your Account was succesfully created!!!")
     time.sleep(1)
     print("...")
     login()
     break
   else:
    print("The password must have at least 8 characters, one capital letter and one number.")
    time.sleep(1)
    print("Try Again...")
    time.sleep(2)

def access(): 
 print(pyfiglet.figlet_format("Welocome!", font="small"))
 print("Welcome, choose an option...")
 print("1.Login")
 print("2.Create Account")
 option = input("---> ")
 if option == "2":
   createAccount()
 elif option == "1":
   login()
 else:
   print("Invalid Option...")
   time.sleep(2)
   access()

access()
 