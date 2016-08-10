## capitalize()


## capitalize() - ornek_1
kardiz = "istanbul büyükşehir belediyesi"
if kardiz.startswith("i"):
    kardiz = "İ" + kardiz[1:]
kardiz = kardiz.capitalize()
print(kardiz)
