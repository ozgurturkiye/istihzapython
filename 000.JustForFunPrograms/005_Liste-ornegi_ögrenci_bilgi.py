#3 Öğrencinin bilgilerini tutan ve not hesaplamasını yapan liste örneği

liste = [["", "", "", "", "", "",""],
         ["", "", "", "", "", "",""],
         ["", "", "", "", "", "",""]
        ]

bilgiler = ["No gir...:",
            "Ad gir...:", 
            "SoyAd gir...:", 
            "Not 1 gir...:", 
            "Not 2 gir...:", 
            "Not 3 gir...:"]

for i in range(3):
	for j in range(6):
		liste[i][j] = input(print(bilgiler[j]))
		print(j)
	liste[i][6] = (int(liste[i][3]) + int(liste[i][4]) + int(liste[i][5]))/3
	print(liste[i])

"""
for i in range(3):
	j=0
	##for j in range(6):
	liste[i][j] = input("No gir...:")
	liste[i][j+1] = input("Ad gir...:")	
	liste[i][j+2] = input("SoyAd gir...:")
	liste[i][j+3] = input("Not 1 gir...:")
	liste[i][j+4] = input("Not 2 gir...:")
	liste[i][j+5] = input("Not 3 gir...:")
	liste[i][j+6] = (int(liste[i][j+3]) + int(liste[i][j+4]) + int(liste[i][j+5]))/3 

"""
print(liste)
	
	
