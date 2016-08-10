## title()


## title() - ornek_1
kardiz = "istanbul"
if kardiz.startswith("i"):
    kardiz = "İ" + kardiz[1:]
    kardiz = kardiz.title()
else:
    kardiz = kardiz.title()
print(kardiz)
#### Burada else: bloğu ile birlikte kod tekrarı var, Bundan kurtulmak için
#### aşağıdaki şekilde de yazılabilir.
##kardiz = "istanbul"
##if kardiz.startswith("i"):
##    kardiz = "İ" + kardiz[1:]
##
##kardiz = kardiz.title()
##print(kardiz)


#### title() - ornek_1
##kardiz = "on iki ada"
##
##for kelime in kardiz.split():
##    if kelime.startswith("i"):
##        kelime = "İ" + kelime[1:]
##        
##kelime = kelime.title()
##
##print(kelime, end=" ")
