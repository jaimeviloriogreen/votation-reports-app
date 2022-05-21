from ast import For
from os import system
from prettytable import PrettyTable
from colorama import Fore

from helpers.inquirer import questionMenu
from helpers.db import Connection

system("clear")
connected = Connection()
ptable = PrettyTable()

print( Fore.GREEN + "Wellcome to votation report @app")
print("")

while True:
    
    opt = questionMenu()
    
    if opt == "1":
        system("clear")
        
        print("Lista de los candidatos:")
        print("")
        
        ptable.field_names = ["#", "Nombre", "Apellido", "Aspiraciones"]   
         
        candidates = connected.getCandidates()
        candidates = [list(candidate) for candidate in candidates]

        ptable.add_rows(candidates)
        print(ptable)
        print("")
        
        ptable.clear()
        
    elif opt == "2":
        system("clear")
        print("")
        
        ptable.field_names = ["Número de votos emitidos"]
         
        votes = connected.numberOfVoteCast()
        votes = [list(votes) for vote in votes]
        
        ptable.add_rows(votes)
        print(ptable)
        print("")
        
        ptable.clear()
    elif opt == "3":
        system("clear")
        print(opt)
    elif opt == "4":
        system("clear")
        print(opt)
    elif opt == "5":
        system("clear")
        print(opt)
    elif opt == "6":
        system("clear")
        print(Fore.CYAN + "Session closed!")
        connected.closeConnection()
        break
    




