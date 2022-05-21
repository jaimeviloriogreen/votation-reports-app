from ast import For
from os import system
from prettytable import PrettyTable
from colorama import Fore

from settings.set import dataConnection
from helpers.inquirer import questionMenu
from helpers.db import Connection

system("clear")
connected = Connection(dataConnection)
ptable = PrettyTable()

print("")
print( Fore.GREEN + "Wellcome to votation report @app")
print("")

while True:
    
    opt = questionMenu()
    
    if opt == "1":
        system("clear")
        
        print(Fore.RESET + "")
        print(Fore.GREEN + 'List of candidates:')
        print(Fore.RESET + "")
        
        ptable.field_names = [ 
        Fore.CYAN + "#" + Fore.RESET, 
        Fore.CYAN + "Fisrt Name" + Fore.RESET, 
        Fore.CYAN + "Last Name" + Fore.RESET, 
        Fore.CYAN + "Aspirations" + Fore.RESET, 
        ]   
         
        candidates = connected.getCandidates()
        candidates = [list(candidate) for candidate in candidates]

        ptable.add_rows(candidates)
        print(ptable)
        print("")
        
        ptable.clear()
        
    elif opt == "2":
        system("clear")
        print(Fore.RESET + "")
        print(Fore.GREEN + "Votes cast:")
        print(Fore.RESET + "")
        
        ptable.field_names = [
            Fore.CYAN + "Number of votes cast" + Fore.RESET
        ]
         
        votes = connected.numberOfVoteCast()
        votes = [list(votes) for vote in votes]
        
        ptable.add_rows(votes)
        print(ptable)
        print("")
        
        ptable.clear()
    elif opt == "3":
        system("clear")
        print(Fore.RESET + "")
        print(Fore.GREEN + "Vote by gender:")
        print(Fore.RESET + "")
        
        genders = connected.votesByGender()
        genders = [list(gender) for gender in genders]
        
        ptable.field_names = [
            Fore.CYAN + "Gender" + Fore.RESET, 
            Fore.CYAN + "Number" + Fore.RESET
        ]
        
        ptable.add_rows(genders)
        print(ptable)
        print("")
        
        ptable.clear()
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
    




