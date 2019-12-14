import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Process Killer")
import os
import time
def menu():
    print("What do you want to do? \n1. Kill Example1.exe \n2. Kill Example2.exe (2)")
    choice = input()
    
    if choice == "1":
        os.system('taskkill /f /im example1.exe') 
        print("Done!")
        input("Press ENTER to close program.")
        exit()
        
    if choice == "2":
        os.system('taskkill /f /im example2.exe')
        time.sleep(2)
        os.system('C:\Windows\example2.exe')
        print("Done!")
        input("Press ENTER to close program.")
        exit()
        
    else:
        print("Sorry. Invalid command.")
        menu()

menu()
