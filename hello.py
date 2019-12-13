def start():
    print("Hi")
    print("")
    ans1 = input("")
    if ans1 == ("Hi"):
        print("How are you")
        print("")
        input("")
        exit()
    if ans1 == ("exit"):
        exit()
    else:
        print("Please type in (Hi) without brackets to continue the program. Else, type (exit) without brackets to exit the program.")
        start()
start()
