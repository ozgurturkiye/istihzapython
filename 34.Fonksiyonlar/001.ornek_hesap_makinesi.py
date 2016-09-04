## Örnek Hesap Makinesi

## 4 İşlemi Yapan Fonksiyonlar

## Toplama
def toplama(sayi_1, sayi_2):
    toplam = sayi_1 + sayi_2
    return toplam
## Çıkarma
def cikarma(sayi_1, sayi_2):
    fark = sayi_1 - sayi_2
    return fark
## Çarpma
def carpma(sayi_1, sayi_2):
    carpim = sayi_1 * sayi_2
    return carpim
## Bölme
def bolme(sayi_1, sayi_2):
    bolum = sayi_1 / sayi_2
    return bolum

sayi_1 = int(input("1. sayı....:"))
islem = input("işlemi seçiniz (+ - * /)")
sayi_2 = int(input("2. sayı....:"))

## Seçilen işleme göre sonucu döndüren secim fonksiyonu
def secim(islem):
    if islem == "+":
        sonuc = (toplama(sayi_1, sayi_2))
        return sonuc
    elif islem == "-":
        sonuc = (cikarma(sayi_1, sayi_2))
        return sonuc
    elif islem == "*":
        sonuc = (carpma(sayi_1, sayi_2))
        return sonuc
    elif islem == "/":
        sonuc = (bolme(sayi_1, sayi_2))
        return sonuc

print(secim(islem))
