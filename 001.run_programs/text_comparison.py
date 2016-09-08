# Kümeleri kullanarak iki metin dosyasındaki isimleri karşılaştırıp aynı olanları bulan program...

#metin_1 dosyasını açıyoruz
kardiz_1 = open("metin_1.txt")
#birinci metin dosyasını karakter dizisi olarak okuyoruz
kardiz_1 = kardiz_1.read()
#Karakter dizisi içerisindeki ("I", "ı") değişimi ve boşluk(" ") ve tab("\t") karakterlerini düzenliyoruz
kardiz_1 = kardiz_1.replace("I", "ı").replace("i", "i").replace("\t", "").replace(" ", "").lower()
print(kardiz_1)

#Karakter dizisini split() metodu ile "\n" karakterinden bölerek listeye dönüştürüyoruz
liste_1 = kardiz_1.split("\n")
print(liste_1)
print("----------------------------------------")

kardiz_2 = open("gorevlendirme_liste.txt")
kardiz_2 = kardiz_2.read()
kardiz_2 = kardiz_2.replace("I", "ı").replace("i", "i").replace("\t", "").replace(" ", "").lower()

liste_2 = kardiz_2.split("\n")
print(liste_2)

#liste_1 ve liste_2 listesini, set metodu ile kümeye dönüştürüp kesişim( & - intersection() ) lerini alıyoruz.
print("Küme kesişim")
print(set(liste_1) & set(liste_2))
