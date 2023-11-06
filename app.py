from app.TextUserInterface import TextUserInterface as TUI
from os import system
from rich import print
import pyfiglet
import sys

if __name__ == "__main__":
    
    while True:
        tui = TUI()
        system("clear")
        title = pyfiglet.figlet_format('Talon v2.0') # Create title and print it
        print(f'[yellow]{title}[/yellow]')
        tui.printMenu()
        try:
            chc = input("-->")
            choice = tui.elaborateChoice(chc)
            tui.executeCommand()
        except Exception:
            print("Something went wrong...")
        
        
