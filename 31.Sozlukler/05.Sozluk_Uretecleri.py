## Sözlük Üreteçleri

## 1 - ## Amaç alfabedeki harfleri numaralandırarak sözlük oluşturmak

harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
harf_no = {}

#### Ornek_1
##
##for i in harfler:
##    harf_no[i] = harfler.index(i)
##
##print(harf_no)

#### Ornek_2
##
##for i in range(len(harfler)):
##    harf_no[harfler[i]] = i
##
##print(harf_no)

## Ornek_3 - Üstteki 2 yöntem yerine sözlük üreteçleri ile

harf_no = {i: harfler.index(i) for i in harfler}

print(harf_no)

## 2 - ## Amaç verilmiş listedeki elemenların kaç harften oluştuklarını
       ## yanlarına yazan sözlük oluşturmak

isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
harf_sayisi = {}

## Ornek_1

for i in range(len(isimler)):
    harf_sayisi[isimler[i]] = len(isimler[i]) 

print(harf_sayisi)

## Ornek_2 - Üstteki yöntem yerine sözlük üreteçleri ile

harf_sayisi_2 = {}
harf_sayisi_2 = {i: len(i) for i in isimler}

print(harf_sayisi_2)
