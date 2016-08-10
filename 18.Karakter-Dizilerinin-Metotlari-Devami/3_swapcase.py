## swapcase()


#### swapcase() - ornek_1
##kardiz = "python"
##print(kardiz,"\n")
##kardiz = kardiz.swapcase()
##print(kardiz,"\n")
##kardiz = kardiz.swapcase()
##print(kardiz,"\n")


## swapcase() - ornek_2 (ı,İ sorunu)
kardiz = "istanbul"
for i in kardiz:
    if i == 'İ':
        kardiz = kardiz.replace('İ', 'i')
    elif i == 'i':
        kardiz = kardiz.replace('i', 'İ')
    else:
        kardiz = kardiz.replace(i, i.swapcase())
print(kardiz)
## replace() hatırlatma
## kardiz = "elma"
## print(kardiz.replace("el","EL"))
## ELma
