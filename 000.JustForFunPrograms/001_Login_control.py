#This program for user login control and time log
#userName: ozgur
#password: 12345

from datetime import datetime

user_name = input("Please enter your user name: ")
password  = input("Please enter your password")

if user_name == "ozgur" and password == "12345":
    print("Well done!")
else:
    print("Sorry! Wrong user name and password")
    an = datetime.now()
    tarih = datetime.ctime(an)
    print(tarih)   #This will be write in file time_log.txt 
