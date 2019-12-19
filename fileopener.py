import ctypes
import os
ctypes.windll.kernel32.SetConsoleTitleW("Run")
os.system("color f0")
def run():
    if os.name == 'posix':
        exit()
    print("Type the name of a program, folder, document or Internet resource, and Windows will open it for you.")
    answer = input("")
    os.system(answer)
run()