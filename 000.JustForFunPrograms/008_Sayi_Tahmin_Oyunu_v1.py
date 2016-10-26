## ---Sayı Tahmin Oyunu---

## 0-100 arasında rastgele bir sayı tutup
## kullanıcıyı yönlendirerek bulduran program

import random
tutSayi = random.randint(0,100)

tahTutkardiz = "Tahmininiz..:{}--Tuttuğum sayı..:{}"
tahminkardiz = "{}. Tahmininizi giriniz...:"

deneme = 1
tahmin = -1

while tahmin != tutSayi:
    tahmin = int(input(tahminkardiz.format(deneme)))
    if tahmin == tutSayi:
        print("Tebrikler " + str(deneme) + ". tahmininizde bildiniz :)")
        print(tahTutkardiz.format(tahmin, tutSayi))
    elif tahmin < tutSayi:
        print("Daha büyük bir sayı giriniz")
        deneme += 1
    elif tahmin > tutSayi:
        print("Daha küçük bir sayı giriniz")
        deneme += 1
