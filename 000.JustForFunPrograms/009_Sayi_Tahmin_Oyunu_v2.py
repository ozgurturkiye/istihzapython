## ---Sayı Tahmin Oyunu---

## Kullanıcının 0-100 arasında rastgele bir sayı tutup;
## yaptığı yönlendirmelerle bilgisayarın sayıyı bulduğu program

import random
tahmin = int(random.randint(0,100))

girisMesaji = """Şimdi sizinle bir oyun oynayalım
0-100 arasında bir sayı tutun lütfen
Benim tahminim sizin tuttuğunuz sayıdan küçükse k, büyükse b tuşuna basarak;
bulmamda bana yardım ediniz
Eğer bildiysem e tuşuna basınız"""

print(girisMesaji)
print()
print("Tuttuğunuz her sayıyı en fazla 8 denemede bulurum, var mısınız iddiaya?")
print()

deneme = 1
ipucu = ""
altSinir = 0
ustSinir = 100 

while ipucu != "e":
    ipucu = input("""Deneme-{}- Tuttuğunuz sayı {} mı/mi?
                Büyük mü (b), Küçük mü (k)""".format(deneme, int(tahmin)))
    deneme += 1

    if (ipucu == "e"):
        deneme -= 1
        print("Tebrikler bana, {}. denememde buldum işte".format(deneme))

    else:
        if (ipucu == "b"):
            altSinir = tahmin

        elif (ipucu == "k"):
            ustSinir = tahmin

    tahmin = (altSinir + ustSinir) / 2
