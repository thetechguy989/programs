from os import system
from os import name
from time import sleep
def colour():
    if name == 'nt':
        print("Welcome to my colourful/colorful program, WindowsUser.")
    if name == 'posix':
        print("Welcome to my colourful/colorful program, MacOSUser/LinuxUser")
    system('color 40')
    sleep(2)
    system('color 30')
    sleep(2)
    system('color 20')
    sleep(2) 
    colour()
colour()