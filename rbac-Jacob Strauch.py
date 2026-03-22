#short script to demonstrate access controls

#define roles
admin = True
user = False

#hard coded username and role
username = {"bigBoss":admin}


for name, isAdmin in username.items():
    print(f"Welcome back {name}")

    #check user role if it is admin
    if isAdmin:
        #get input to run simple admin only function
        getSecretary = input("Would you like to schedule interviews for a new secretary? (Y/n)").upper()
        if getSecretary == "Y":
            print("Call 867-5309 for first candidate")
        else:
            print("Time to check on the work floor")
    else:
        #get input and run simple logic for user role only
        leave = input("Do you need to schedule any leave? (Y/n)").upper()
        if leave == "Y":
            print("Leave schedule is full sorry :(")
        else:
            print("Great lets get to work")


#This script demonstrates the confidentiality aspect of the CIA triad. 
#This script uses a role-based access control to only allow users with a specific role classification to access certain aspects of the program. 
#In this way data access is restricted to only the intended users.
