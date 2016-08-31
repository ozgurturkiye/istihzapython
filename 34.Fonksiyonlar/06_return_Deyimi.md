# return Deyimi
> - return kelimesi İngilizcede ‘iade etmek, geri vermek, döndürmek’ gibi anlamlar taşır. İşte yukarıdaki örnekte de return deyiminin yaptığı iş budur. Yani bu deyim bize fonksiyondan bir değer ‘döndürür’.
> - Python fonksiyondan hususi bir değerin döndürülmediğini göstermek için ‘None’ adlı bir değer döndürür...

Örnek:
```python
def ismin_ne():
    isim = input("ismin ne? ")
    return isim

print("Merhaba {}. Nasılsın?".format(ismin_ne()))
```
# Örnek bir Uygulama
> Amacımız belli miktarda ve belli aralıkta rastgele sayılar üreten bir program yazmak. Örneğin programımız şu şekilde altı adet rastgele sayı üretebilecek:

```python
import random

def sayı_üret(başlangıç=0, bitiş=500, adet=6):
    sayılar = set()

    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))

    return sayılar

print(sayı_üret())                         #output: {384, 230, 104, 17, 148, 282}
print(sayı_üret(0, 100, 10))               #output: {1, 6, 14, 47, 16, 85, 88, 57, 58, 63}
print(*sayı_üret(100, 1500, 3), sep='-')   #output: 1066-678-447

```

Kaynakça: http://belgeler.istihza.com/py3/fonksiyonlar.html#ornek-bir-uygulama
