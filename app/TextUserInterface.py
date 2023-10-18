from os import system

class TextUserInterface:
    def __init__(self):
        self.choice = 0
        pass 
    
    def printMenu(self):
        print("################## Talon v2 ##################")
        print("#                                            #")
        print("# 1). Execute a DNS Lookup query             #")
        print("# 0). Exit                                   #")
        print("#                                            #")
        print("##############################################")
        print()
        print()

    def elaborateChoice(self,choice):
        chc = int(choice)
        if(0 <= chc <=1):
            self.choice = chc 
            return self.choice
        else:
            raise ValueError()
        
    def executeCommand(self):
        print(self.choice)
