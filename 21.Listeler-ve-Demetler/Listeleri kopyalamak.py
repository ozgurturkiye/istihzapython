liste = ["elma", "armut", "erik"]
#YAPMAMALISIN, bu şekilde yaparsan id'leri aynı iki liste oluşur
liste_kopya = liste
id(liste) == id(liste_kopya) # output: True

#1.Yöntem
liste1 = liste[:]

#2.Yöntem
liste2 = list(liste)

#id'leri kontrol edelim
print("liste id      :{}".format(id(liste)))
print("liste_kopya id:{}".format(id(liste_kopya)))
print("liste1 id     :{}".format(id(liste1)))
print("liste2 id     :{}".format(id(liste2)))
