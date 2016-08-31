
# Fonksiyonlar
> Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu işlemleri tek adımda yapmamızı sağlamaktır. 

```python
print("Fırat", "Özgül", "1980", "Adana")`: Benim gördüğüm
```

```python
print("Fırat", "Özgül", "1980", "Adana", sep=" ", end="\n", file=sys.stdout, flush=False)`: Gerçekte olan
```

# Fonksiyon Tanımlamak ve Çağırmak
```python
def kayıt_oluştur(parametre1, parametre2, parametre3, parametre4):
   (...)
```

```python
kayıt_oluştur(parametre1, parametre2, parametre3, parametre4)
```

Teknik olarak söylemek gerekirse, ilk parçaya `‘fonksiyon tanımı’ (function definition)`, ikinci parçaya ise `‘fonksiyon çağrısı’ (function call)` adı verilir. Dolayısıyla bir fonksiyonun yaşam döngüsü iki aşamadan oluşur. Buna göre bir fonksiyon önce tanımlanır; ...sonra da çağrılır;

Bu derse gelinceye kadar öğrendiğimiz print(), type() ve open() gibi fonksiyonlara teknik olarak `‘gömülü fonksiyonlar’ (builtin functions)` adı verilir.

# Fonksiyonların Yapısı
```python
def bir_fonksiyon():
    (...)
```

Tahmin edebileceğiniz gibi, sonraki satıra yazacağımız kodlar girintili olacak. Yani mesela:

Fonksiyon gövdesine, def ifadesinden itibaren 4 (dört) boşlukluk bir girinti veriyoruz.

```python
def selamla():
    print("Elveda Zalim Dünya!")
```
Örneğin:
```python
def selamla():
    print("Elveda Zalim Dünya!")

selamla()
```
> - Python’da bir fonksiyonun yaşam döngüsü iki aşamadan oluşur: Tanımlanma ve çağrılma.
> - Fonksiyonun adını belirleyip iki nokta üst üste koyduktan sonra, alt satırda girintili olarak yazdığımız bütün kodlar fonksiyonun gövdesini oluşturur. Doğal olarak, bir fonksiyonun gövdesindeki bütün kodlar o fonksiyona aittir. Girintinin dışına çıkıldığı anda fonksiyon tanımı da sona erer.



Kaynakça: http://belgeler.istihza.com/py3/fonksiyonlar.html
