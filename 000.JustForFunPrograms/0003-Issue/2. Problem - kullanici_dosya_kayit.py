#2. Program: Kullanıcı ad, soyad, doğum tarihi, cinsiyet bilgilerini alıp dosyaya kaydeden program

ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
dogum_tarih = input("Doğum tarihinizi giriniz: ")
cinsiyet = input("cinsiyet giriniz E - K : ")
#print("{} {} {} {}".format(ad, soyad, dogum_tarih, cinsiyet))

liste = []
liste = ad, soyad, dogum_tarih, cinsiyet

#1. yol uzun olan
with open("bilgiler.txt", "a") as f:
    for i in liste:
        f.write(i)
        f.write(" ")
    f.write("\n")

#2. yol karakter dizilerinle oynayarak
veri = " ".join(liste)  #join metodu kullanılarak karakter dizisine dönüştürdük

with open("bilgiler.txt", "a") as f:
    f.write(veri) 
    f.write("\n")

