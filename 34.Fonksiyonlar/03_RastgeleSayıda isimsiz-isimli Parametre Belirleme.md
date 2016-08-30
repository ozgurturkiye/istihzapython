# Rastgele Sayıda İsimsiz Parametre Belirleme

> Peki acaba biz kendimiz, sınırsız parametre alabilen fonksiyonlar üretebilir miyiz?
> Bu sorunun cevabı ‘evet’ olacaktır.

```python
def fonksiyon(*parametreler):
    print(parametreler)

fonksiyon(1, 2, 3, 4, 5)
```


`output:` (1, 2, 3, 4, 5)

> - Bu arada, bu tür fonksiyonların alabileceği parametre sayısı, dediğimiz gibi, pratikte sınırsızdır, ama teknik olarak bu sayı 256 adedi geçemez.
> - Yukarıdaki kodların verdiği çıktının bir demet olduğuna dikkatinizi çekmek isterim.
> - Bu bilgiye sahip olduktan sonra, bu tür fonksiyonları demet işleme kurallarına göre istediğiniz şekilde manipüle edebilirsiniz.

Örnek
```python
def çarp(*sayılar):
    sonuç = 1
    for i in sayılar:
        sonuç *= i
    print(sonuç)
```
çarp(1, 2, 3, 4)

> - Elbette * işaretiyle birlikte kullanacağınız parametrenin adı olarak, Python’ın değişken adlandırma kurallarına uygun bütün kelimeleri belirleyebilirsiniz.
> - Yazdığımız kodlarda Python programlama dilinin geleneklerine bağlı kalmak çoğunlukla iyi bir alışkanlıktır.
> - Ama Python dünyasında * işaretiyle birlikte kullanılacak parametrenin adı geleneksel olarak, ‘argümanlar’ anlamında ‘args’tır. Yani Python programcıları genellikle yukarıdaki gibi bir fonksiyonu şöyle tanımlar:

`def fonksiyon(*args):`

# Rastgele Sayıda İsimli Parametre Belirleme
```python
def fonksiyon(**parametreler):
    print(parametreler)

fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")
```
`output:` {'şehir': 'Ankara', 'isim': 'Ahmet', 'soyisim': 'Öz', 'meslek': 'Mühendis'}

> - Gördüğünüz gibi, fonksiyonu tanımlarken parametremizin sol tarafına yerleştirdiğimiz ** işareti, bu fonksiyonu çağırırken yazdığımız isimli parametrelerin bize bir sözlük olarak verilmesini sağlıyor.
> - Bu yapının bize bir sözlük verdiğini bildikten sonra, bunu sözlük veri tipinin kuralları çerçevesinde istediğimiz şekilde evirip çevirebiliriz.

Örnek
```python
def kayıt_oluştur(**bilgiler):
    print("-"*30)

    for anahtar, değer in bilgiler.items():
        print("{:<10}: {}".format(anahtar, değer))

    print("-"*30)

kayıt_oluştur(ad="Fırat", soyad="Özgül", şehir="İstanbul", tel="05333213232")
```
> - Tıpkı * işaretlerinin betimlediği parametrenin geleneksel olarak ‘args’ şeklinde adlandırılması gibi, ** işaretlerinin betimlediği parametre de geleneksel olarak ‘kwargs’ şeklinde adlandırılır.

`def kayıt_oluştur(**kwargs):`

Örnek:
```python
def karşılık_bul(*args, **kwargs):
    for sözcük in args:
        if sözcük in kwargs:
            print("{} = {}".format(sözcük, kwargs[sözcük]))
        else:
            print("{} kelimesi sözlükte yok!".format(sözcük))


sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

karşılık_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)
```
