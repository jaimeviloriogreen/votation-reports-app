from ast import For
from os import system
from colorama import Fore

def showMessages(message, color):
    system("clear")
    
    print("")
    print( color + message + Fore.RESET)
    print("")