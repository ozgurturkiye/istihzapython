## rjust(), ljust()


#### ornek_1
##for i in dir(""):
##    print(i.ljust(20))
##    
##for i in dir(""):
##    print(i.rjust(20))


## ornek_2
for i in "elma", "armut", "patlıcan":
    print(i.ljust(10, "."))

for i in "elma", "armut", "patlıcan":
    print(i.rjust(10, "."))
