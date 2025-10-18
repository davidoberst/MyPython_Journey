import time

# Creación de tickets
tickets = []
ticketsAtended = []
ticket_id = 0

def createTicket():
    global ticket_id, t
    ticket = {}
    print("Create a Ticket:")
    time.sleep(1)
    ticket["name"] = input("Name: ")
    time.sleep(1)
    ticket["description"] = input("Description: ")
    time.sleep(1)
    while True:
     priority  = ticket["priority"] = input("Priority (high, medium, low): ")
     time.sleep(1)
     ticket_id += 1
     ticket["ID"] = ticket_id
     ticket["Status"] = "Pending"
     if priority.lower() not in ["high","medium","low"]:
        time.sleep(1)
        print("Please, select a valid option...")
        time.sleep(1)
     else:
         break
    tickets.append(ticket)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("\n Ticket successfully created!!")
    op = input("Do you want to create a new ticket? : y/n : ")
    if op.lower() == "y":
        createTicket()
    else:
        pass


def System():
    if not tickets:
        print("No tickets yet.")    
    else:
        print("-----------Available Tickets------------ :")
        for x in tickets:
            for clave, valor in x.items():
                print(f"{clave} : {valor}")
            print("")
    input("Press enter to go back : ")

def SystemLogic():
 pass
 

# Bucle principal
while True:
    print("\n-------- Welcome to Tickets -----------")
    print("Options:")
    print("1. Create a Ticket")
    print("2. See Tickets")
    option = input("\n Escribe 'exit' para salir o elige una opción (1 o 2): ").strip().lower()
    if option == "exit":
        break
    elif option == "1":
        createTicket()
    elif option == "2":
        System()
    else:
        print("Invalid option. Try again.")