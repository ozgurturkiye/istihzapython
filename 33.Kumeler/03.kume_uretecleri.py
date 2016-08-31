## Küme Üreteçleri

## içinde 1000 adet 1ile 10000 sayıları arasında random üretilmiş bir liste üret

import random

liste = [random.randint(0, 10000) for i in range(1000)]


## bu 1000 sayının içinde değeri 100'den küçük olanları bul

for i in set(liste):
    if i<100:
        print(i)
## yada

kume = {i for i in liste if i<100}
print(kume)

## yada

kucuk_sayilar = [i for i in liste if i < 100]
print(kucuk_sayilar)
