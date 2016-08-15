#This program for user login control
#userName: ozgur
#password: 12345

user_name = input("Please enter your user name: ")
password  = input("Please enter your password")

if user_name == "ozgur" and password == "12345":
    print("Well done!")
else:
    print("Sorry! Wrong user name and password")
    #You can log time in here for failed input
