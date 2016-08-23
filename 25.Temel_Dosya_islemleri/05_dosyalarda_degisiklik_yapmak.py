#Dosyalarda Değişiklik Yapmak
#Bildiğiniz gibi “w” kipi dosya içeriğini tamamen siliyor.

#Dosyaların Sonunda Değişiklik Yapmak (“a” adlı bir kipten yararlanacağız)
#f = open(dosya_adı, "a")

with open("fihrist.txt", "a") as f:
    f.write("Selin Özden\t: 0212 222 22 22\n")
    
#Dosyaların Başında Değişiklik Yapmak (“a+” adlı bir kipten yararlanacağız)
with open("fihrist.txt", "r+") as f:
    veri = f.read()
    f.seek(0) #Dosyayı başa sarıyoruz
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
    
#Dosyaların Ortasında Değişiklik Yapmak
"""
write() metodu bir dosyaya yalnızca karakter dizilerini yazabilir. 
Bu metot yardımıyla dosyaya liste tipinde herhangi bir veri yazamazsınız. 
Eğer mutlaka write() metodunu kullanmak isterseniz, liste üzerinde bir for döngüsü kurmanız gerekir.
"""
with open("fihrist.txt", "r+") as f:
    veri = f.readlines()
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    f.seek(0)
    f.writelines(veri)

#Veya şu şekilde yazılabilir
with open("fihrist.txt", "r") as f:
    veri = f.readlines()

with open("fihrist.txt", "w") as f:
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    f.writelines(veri)
