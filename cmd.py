from os import system
from os import name
if name == 'posix':
    exit()
system('ver')

def cmd():
    cmdc = input("C:\>")
    system(cmdc)
    if cmdc == 'exit':
        exit()
    cmd()
cmd()