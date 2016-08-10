## lower() - metodu bir karakter dizisini tamamen küçük harflerden olusacak sekle
##getirir
## upper() - metodu bir karakter dizisini tamamen büyük harflerden olusacak sekle
##getirir


## lower() - ornek_1
kisi = input("Aradığınız kişinin adı ve soyadı: ")
kisi = kisi.lower()
if kisi == "ahmet öz":
    print("email: aoz@hmail.com")
    print("tel : 02121231212")
    print("şehir: istanbul")
elif kisi == "mehmet söz":
    print("email: msoz@zmail.com")
    print("tel : 03121231212")
    print("şehir: ankara")
elif kisi == "mahmut göz":
    print("email: mgoz@jmail.com")
    print("tel : 02161231212")
    print("şehir: istanbul")
else:
    print("Aradığınız kişi veritabanında yok!")


#### lower() - ornek_2 (ı, İ sorunu - upper içinde aynı sorun var)
##iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
##iller = iller.replace("I", "ı").replace("İ", "i").lower()
##print(iller)
##
##
#### upper() - ornek_1 
##sehir = input("Hava durumunu öğrenmek için bir şehir adı girin: ")
##sehir = sehir.upper()
##if sehir == "ADANA":
##    print("parçalı bulutlu")
##elif sehir == "ERZURUM":
##    print("karla karışık yağmurlu")
##elif sehir == "ANTAKYA":
##    print("açık ve güneşli")
##else:
##    print("Girdiğiniz şehir veritabanında yok!")
