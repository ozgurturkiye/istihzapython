#This part for a litte string example

kardiz      = "This is my favorite string sentences"
kardiz_long = """
This string
is Really 
reallY
long sentences!

""" 

print(kardiz)
print(kardiz_long)

print(kardiz.split())            #split by space
print(kardiz_long.splitlines())  #split by \n newline

#This is important python programmers keep user entered data lower() for standart ***
print(kardiz_long.lower()) 

#join() splitted strings
separeted_kardiz = kardiz.split()          #sapared string as a list
hobaa = " ".join(separeted_kardiz)         #join the list as a string
print(hobaa)
