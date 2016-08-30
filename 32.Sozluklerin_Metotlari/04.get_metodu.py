## Sözlüklerin Metotları

## get() metodu

## ornek_1

sozluk = {"dil": "language",
          "bilgisayar": "computer",
          "masa": "table",
          "kitap": "book"}


sorgu = input("Anlamını öğrenmek istediğiniz kelimeyi yazınız.")

print(sozluk.get(sorgu, "Bu kelimenin anlamını bilmiyorum"))


## ornek_2
## Diyelim ki bir havadurumu programı yazmak istiyoruz. Bu programda kullanıcı bir sehir adı
## girecek. Program da girilen sehre ait havadurumu bilgilerini ekrana yazdıracak.

##hava_durumu = {"istanbul": "30",
##               "izmir": "35",
##               "ankara": "22",
##               "kastamonu": "18",}
##
##hava_sorgu = input("Hava durumunu öğrenmek istediğiniz şehir...:")
##
##print(hava_durumu.get(hava_sorgu, "veri yok"))
