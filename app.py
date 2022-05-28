from os import system
from prettytable import PrettyTable
from colorama import Fore

from settings.set import dataConnection
from helpers.messages import showMessages
from helpers.inquirer import questionMenu
from helpers.data import Data

ptable = PrettyTable()

showMessages("Wellcome to votation report @app", Fore.GREEN)

while True:
    
    opt = questionMenu()
    
    if opt == "1":
        system("clear")
        data = Data(dataConnection)
        
        showMessages("List of candidates:",  Fore.GREEN)
        
        ptable.field_names = [ 
            Fore.CYAN + "#" + Fore.RESET, 
            Fore.CYAN + "Fisrt Name" + Fore.RESET, 
            Fore.CYAN + "Last Name" + Fore.RESET, 
            Fore.CYAN + "Aspirations" + Fore.RESET, 
        ]   
         
        candidates = data.getCandidates()
        candidates = [list(candidate) for candidate in candidates]
    
        ptable.add_rows(candidates)
        print(ptable)
        print("")
        
        ptable.clear()
        
    elif opt == "2":
        data = Data(dataConnection)
        showMessages("Votes cast:",  Fore.GREEN)
        
        ptable.field_names = [
            Fore.CYAN + "Number of votes cast" + Fore.RESET
        ]
         
        votes = data.numberOfVoteCast()
        votes = [list(votes) for vote in votes]
        
        ptable.add_rows(votes)
        print(ptable)
        print("")
        
        ptable.clear()
    elif opt == "3":
        data = Data(dataConnection)
        showMessages("Vote by gender:",  Fore.GREEN)
        
        genders = data.votesByGender()
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
        data = Data(dataConnection)
        showMessages("Vote by candidates:", Fore.GREEN)
        
        voteByCandidates = data.votesByCandidates()
        voteByCandidates = [list(candidate) for candidate in voteByCandidates]
        
        ptable.field_names = [
            Fore.CYAN + "Candidates" + Fore.RESET, 
            Fore.CYAN + "Number of votes cast" + Fore.RESET
        ]
        
        ptable.add_rows(voteByCandidates)
        print(ptable)
        print("")
        
        ptable.clear()
            
    elif opt == "5":
        showMessages("Percent of votes by candidates:",  Fore.GREEN)
        
        data = Data(dataConnection)
        totalVotes = data.numberOfVoteCast()[0]
        
        data = Data(dataConnection)
        percentVotes = data.votesByCandidates()
        
        ptable.field_names = [
            Fore.CYAN + "Candidates" + Fore.RESET, 
            Fore.CYAN + "Percent of votes" + Fore.RESET
        ]
            
        percentVotes = [(x, f"{(( y / totalVotes ) * 100):.2f} %") for x,y in percentVotes]
    
        ptable.add_rows(percentVotes)
        print(ptable)
        print("")
        
        ptable.clear()
    elif opt == "6":
        showMessages("Session closed!", Fore.CYAN)
        break
    




