def menu():
    print("What is your name?")
    print("")
    ans1 = input("")
    print("What is your age?")
    print("")
    ans2 = input("")
    print("What is your father's age?")
    ans3 = input("")
    print("")
    print("Your name is")
    print(ans1)
    print("Your age is")
    print(ans2)
    print("Your father's age is")
    print(ans3)
    # This program adds two numbers

    num1 = (ans2)
    num2 = (ans3)

    # Add two numbers
    sum = float(num1) + float(num2)

    # Display the sum
    print('Your ages together are {2}'.format(num1, num2, sum))
    input("")
    if sum == (str):
        print("ERROR: Invalid syntax. Please try again")
        menu()
menu()