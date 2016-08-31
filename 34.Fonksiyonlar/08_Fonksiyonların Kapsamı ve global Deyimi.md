# Fonksiyonların Kapsamı ve global Deyimi
```python
x = 0

def fonk():
    x = 1
    return x

print('fonksiyon içindeki x: ', fonk())
print('fonksiyon dışındaki x: ', x)
```
Bu kodları çalıştırdığımızda şu çıktıyı alacağız:
```python
fonksiyon içindeki x:  1
fonksiyon dışındaki x:  0
```
Gördüğünüz gibi fonksiyon içindeki ve fonksiyon dışındaki aynı adlı değişkenler birbirine karışmıyor. Bunun sebebi, Python’daki ‘isim alanı’ (namespace) adlı bir kavramdır.

> - Örneğin yukarıdaki kodlarda fonksiyon dışındaki x değişkeni ana isim alanında yer alan ‘global’ bir değişkendir. Fonksiyon içindeki x değişkeni ise fonk() değişkeninin isim alanı içinde yer alan ‘lokal’ bir değişkendir. Bu iki değişken, adları aynı da olsa, birbirlerinden farklı iki nesnedir.

> - Python herhangi bir nesneye göndermede bulunduğumuzda, yani o nesnenin değerini talep ettiğimizde aradığımız nesneyi ilk önce mevcut isim alanı içinde arar. Eğer aranan nesneyi mevcut isim alanı içinde bulamazsa yukarıya doğru bütün isim alanlarını tek tek kontrol eder.

```python
x = 0

def fonk():
    x = 10
    print(x)   #output: 10

fonk()
print(x)       #output: 0 
```
**Python’da bir nesnenin değerini değiştirmekle, o nesneyi yeniden tanımlamak farklı kavramlardır.**

Eğer bir nesne değiştirilebilir bir nesne ise, o nesnenin değerini, lokal isim alanlarından değiştirebilirsiniz:

```python
x = set()

def fonk():
    x.add(10)
    return x

print(fonk())
```
Ama eğer bir nesne değiştirilemez bir nesne ise, o nesnenin değerini zaten normalde de değiştiremezsiniz. Değiştirmiş gibi yapmak için ise o nesneyi yeniden tanımlamanız gerektiğini biliyorsunuz:
```python
>>> isim = 'Fırat'
>>> isim += ' Özgül'
>>> print(isim)

#output: Fırat Özgül
```
> Burada yaptığımız şey, karakter dizisinin değerini değiştirmekten ziyade bu karakter dizisini yeniden tanımlamaktır. Çünkü bildiğiniz gibi karakter dizileri değiştirilemeyen veri tipleridir.

İşte karakter dizileri gibi değiştirilemeyen nesneleri, lokal isim alanlarında değiştiremeyeceğiniz gibi, yeniden tanımlayamazsınız da...
```python
isim = 'Fırat'

def fonk():
    isim += ' Özgül'
    return isim

print(fonk())
```
Bu kodları çalıştırdığınızda Python size bir hata mesajı gösterecektir.

Aynı durum değiştirilebilir nesneler için de geçerlidir:
```python
isim_listesi = []

def fonk():
    isim_listesi += ['Fırat Özgül', 'Orçun Kunek']
    return isim_listesi

print(fonk())   #Bu kod hata verecektir
```
Değiştirilebilen bir veri tipi olan listeleri, fonksiyon içinde yeniden tanımlayamazsınız. Ancak tabii isterseniz listeleri değişikliğe uğratabilirsiniz:
```python
isim_listesi = []

def fonk():
    isim_listesi.extend(['Fırat Özgül', 'Orçun Kunek'])
    return isim_listesi

print(fonk())         #output: ['Fırat Özgül', 'Orçun Kunek']
print(isim_listesi)   #output: ['Fırat Özgül', 'Orçun Kunek']
```
> Gördüğümüz gibi yukarıdaki isim_listesi listesini extend() metodu ile istediğimiz gibi düzenledik.

İşte Python programlama dili bu tür durumlar için çözüm olacak bir araç sunar bize. Bu aracın adı **global**.

> global deyimi her ne kadar ilk bakışta çok faydalı bir araçmış gibi görünse de aslında programlarımızda genellikle bu deyimi kullanmaktan kaçınmamız iyi bir fikir olacaktır. Çünkü bu deyim aslında global alanı kirletmemize neden oluyor. Global değişkenlerin lokal isim alanlarında değişikliğe uğratılması, eğer dikkatsiz davranırsanız programlarınızın hatalı çalışmasına yol açabilir.
