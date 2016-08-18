#liste = [i for i in range(100) if i % 3 == 0]
#print(liste)

#Liste üreteçlerinin kullanarak yapılan karmaşık örnekler.

liste = [["Ali","Ayşe", "veli"],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]

print(liste)

tumu = []

for i in liste:
	for z in i:
		if type(z) == type(""):
			for t in z:
				print(t)
		else:
			print(z)
		tumu += [z]
		
print(tumu)
print("--------------------------------")
liste2 = [["Ali","Ayşe", "veli"],
         ["4", "5", "6df"],
         ["7", "8", "9"],
         ["10", "11", "12"]]


#other diye tanımladığımız liste liste2 üzerinden 3 lü döngü kuruyor.
other = [t for z in liste2 for i in z for t in i]
print(other)
