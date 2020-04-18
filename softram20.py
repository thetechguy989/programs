# Module Importing
from time import sleep
import os
# OS Check
if os.name == 'posix':
    exit()
#
def product():
    file_builder = open('softramprog.py', 'w+')
    file_builder.write('''import psutil
import platform
from datetime import datetime
from time import sleep
def get_size(bytes, suffix=""):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "", "", "", "", ""]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
# Memory Information
print("Welcome to SoftRAM20!")
# get the memory details
svmem = psutil.virtual_memory()
print(f"You have {get_size(svmem.total)} GB of memory.")
ram = get_size(svmem.total)
print(f"You have {get_size(svmem.total)} GB of SoftRAM.")
totalram = (float(ram) + float(ram))
print("The total amount of memory that you have is", totalram, "GB")
input("Press ENTER to exit program.")''')
    file_builder.close()
#
def launch():
    choice = input("Do you want to launch SoftRAM20? *y/n* ")
    if choice == 'y':
        os.system("start softramprog.py")
        exit()
    if choice == 'n':
        input("Press ENTER to exit program...")
        exit()
    print("Invalid entry. Please try again.")
    launch()
def installation():
    input("Insert the SoftRAM20 Disk in your computer. Then, press ENTER.")
    time()
    time()
    product()
    print("Thank you for installing SoftRAM20.")
    launch()
##
def time():
    print("Installing.")
    sleep(1)
    os.system("cls")
    print("Installing..")
    sleep(1)
    os.system("cls")
    print("Installing...")
    sleep(1)
    os.system("cls")
    print("Installing..")
    sleep(1)
    os.system("cls")
    print("Installing.")
    os.system("cls")
#
def auth():
    print("To install SoftRAM20, please enter your product key")
    pkey = input("with the format of 'XXXX-OEM-XXXXX'. (All uppercase / case-sensitive) ")
    if pkey == 'SOFT-OEM-RAM20':
        installation()
        exit()
    print("Invalid product key. Please try again.")
    auth()
auth()
#
