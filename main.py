#5.4 Review. Authentication Review.
#This is challenge 34 & 35
#Create a Password Authenticator that gives you three tries with an user account
import os
import stdiomask
#stdiomask is a input hider so text isnt shown.
#if not installed use pip install stdiomask or pip3 install stdiomask
cor=0
username = input("Welcome Please Put Your UserName Here\n>>> ").lower()

if os.path.exists(username):
    for i in range(0,3):
        f = open(username, "r")
        print("Enter Password")
        if stdiomask.getpass(">>> ") == f.read():
            cor=1
            break
        else:
            print("incorect")
    if cor == 1:
        print("Welcome")
    elif cor == 0:
        print("Too many incorect tries")
else:
    print("User Does Not Exist")
    print("Would you like to create "+username+"? [y/n] ")
    passing = input(">>> ")
    if passing == "y":
        print("Enter Password")
        password = stdiomask.getpass(">>> ")
        b = open(username, "w")
        b.write(password)
        b.close()
        os.system("clear")
        import main
    elif passing == "Y":
        print("Enter Password")
        password = stdiomask.getpass(">>> ")
        b = open(username, "w")
        b.write(password)
        b.close()
        os.system("clear")
        import main
    else:
        print("Bye!")
