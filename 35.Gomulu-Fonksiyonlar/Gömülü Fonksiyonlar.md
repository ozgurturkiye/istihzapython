# Gömülü Fonksiyonlar
> Gömülü fonksiyonlar İngilizcede builtin functions olarak adlandırılır. Bu fonksiyonlar gerçekten de dile gömülü vaziyettedirler. Bildiğiniz gibi, bir fonksiyonu kullanabilmemiz için o fonksiyonu tanımlamamız gerekir. İşte gömülü fonksiyonlar, bizim tanımlamamıza gerek kalmadan, Python geliştiricileri tarafından önceden tanımlanıp dile gömülmüş ve hizmetimize sunulmuş faydalı birtakım araçlardır.

1. **abs()** :fonksiyonunu bir sayının mutlak değerini elde etmek için kullanıyoruz.
2. **round()** :fonksiyonu bir sayıyı belli ölçütlere göre yukarı veya aşağı doğru yuvarlamamızı sağlar.
3. **all()** :fonksiyonunun görevi, bir dizi içinde bulunan bütün değerler True ise True değeri, eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.
 - all() fonksiyonu ancak dizi içindeki bütün değerlerin `bool` değeri True ise True çıktısı verecektir.
4. **any()** :fonksiyonunun görevi de, bir dizi içindeki bütün değerlerden en az biri True ise True çıktısı vermektir.
5. **ascii()** :Bu fonksiyon, bir nesnenin ekrana basılabilir halini verir bize. 
 - ascii() fonksiyonu bize **karakter dizisi** döndürür.
 ```python
 a = 'istihza'
print(ascii(a))  #output: 'istihza' --> çıktıya tırnak işaretlerini de eklediğine dikkat edin.
print(ascii('\n!'))   #output: '\n'

a = 'ışık'
print(ascii(a))   #output: '\u0131\u015f\u0131k'

 ```
6. **repr()** : fonksiyonu ise ASCII olmayan karakterlerle karşılaşsa bile, bize çıktı olarak bunların da karakter karşılıklarını gösterir
 - Örnek
 ```python
 ascii('şeker')   #output: "'\\u015feker'"
 repr('şeker')    #output: "'şeker'"
 ```
7. **bool()** :Bu fonksiyon bir nesnenin bool değerini verir
8. **bin()**  :Bu fonksiyon, bir sayının ikili düzendeki karşılığını verir
 - 
 ```python
 bin(12)   #output: '0b1100' Bu fonksiyonun verdiği çıktının bir sayı değil, karakter dizisi olduğuna dikkat etmelisiniz.
 ```
9. **bytes()** : Bu fonksiyon bytes türünde nesneler oluşturmak için kullanılır. 
 - Örnekler etkileşimli kabuk üzerinde çıktıları
 ```python
 bytes()     #output: b''
 bytes(10)   #output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'   --> her bir öğesinin değeri 0 olan 10 baytlık bir veri döndürdü
 bytes("ş", "utf-8")   #output: b'\xc5\x9f'
 "ş".encode("utf-8")   #output: b'\xc5\x9f'   --> Aynı işi yapıyorlar
 bytes([65])           #output: b'A'
 ```
10. **bytearray()** : 
