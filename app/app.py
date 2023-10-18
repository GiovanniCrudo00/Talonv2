from TextUserInterface import TextUserInterface as TUI 

if __name__ == "__main__":
    while True:
        tui = TUI()
        tui.printMenu()
        
        try:
            chc = input("-->")
            choice = tui.elaborateChoice(chc)
            if(choice == 0):
                print("Exiting ...")
                break
            else:
                tui.executeCommand()
        except:
            pass

