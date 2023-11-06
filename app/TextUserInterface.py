from os import system
import sys
from rich import print
from rich.console import Console
from rich.table import Table
import pyfiglet
from app.Commands import *
from app.Validators import *
import time
from rich.progress import track
from random import randrange


class TextUserInterface:
    def __init__(self):
        self.choice = 0
        pass 
    
    def printMenu(self):
        print("1). DNS Lookup")
        print("2). WHOIS Lookup")
        print("3). IP GeoLocation")
        print("0). Exit")
        print()
        print()

    def elaborateChoice(self,choice):
        # take the choice from input and validate using function validateChoice(int)
        # Then assign the value to the internal variable
        chc = int(choice)
        self.choice=ValidateChoice(chc)
        return choice
        
    def executeCommand(self):
        # Here execute the code
        if(self.choice == 0): # if 0 exit the process
            sys.exit()

        elif(self.choice == 1):
            target = input("Insert target for DNS Lookup --> ")
            try:
                ValidateTargetDomain(target)
                results = DNS_lookup(target)
                system("clear")
                elaps=randrange(1,4)
                for i in track(range(elaps), description="Processing DNS lookup..."):
                    time.sleep(1)
                #Print the results
                table = Table(title="DNS Lookup Results")

                table.add_column("Record", justify="right", style="cyan", no_wrap=True)
                table.add_column("Value", justify="right", style="green")
                for i in results:
                    table.add_row(i, results[i])

                console = Console()
                console.print(table)
            except DomainNotValid:
                print("Invalid Domain given")
            
            input("Press Enter to go back to menu...")
        elif(self.choice == 2):
            target = input("Insert target for WHOIS Lookup --> ")
            try:
                ValidateTargetDomain(target)
                results = whois_lookup(target)
                system("clear")

                elaps=randrange(1,4)
                for i in track(range(elaps), description="Processing WHOIS lookup..."):
                    time.sleep(1)
                #Print the results
                table = Table(title="WHOIS Lookup Results")

                table.add_column("Record", justify="right", style="cyan", no_wrap=True)
                table.add_column("Value", justify="right", style="green")
                for i in results:
                    table.add_row(i, results[i])

                console = Console()
                console.print(table)
            except DomainNotValid:
                print("Invalid Domain given")
            input("Press Enter to go back to menu...")
        elif(self.choice == 3):
            target = input("Insert target for IP GeoLocation --> ")
            try:
                ValidateTargetIP(target)
                results = ip_geolocation(target)
                system("clear")
                elaps=randrange(1,4)
                for i in track(range(elaps), description="Processing IP Geo-Localization..."):
                    time.sleep(1)
                #Print the results
                table = Table(title="IP GeoLocation Results")

                table.add_column("Record", justify="right", style="cyan", no_wrap=True)
                table.add_column("Value", justify="right", style="green")
                
                for i in results:
                    table.add_row(i, results[i])

                console = Console()
                console.print(table)
            except IPNotValid:
                print("Invalid IP given")
            input("Press Enter to go back to menu...")
        else:
            print("Invalid command...")
