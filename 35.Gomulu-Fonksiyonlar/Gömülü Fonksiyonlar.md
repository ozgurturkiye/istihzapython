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
 
 for i in range(256):
	print(i, "-", bytes([i]))   #output:sayıların ascii tablosundaki karşılığını yazdırıyoruz.
 ```
 > Son olarak, bytes() fonksiyonuna parametre olarak 0-256 arası sayılardan oluşan diziler de verebiliriz
 
10. **bytearray()** : Bildiğiniz gibi baytlar değiştirilemeyen bir veri tipidir. Ama eğer hem baytlarla çalışmak, hem de bu baytların üzerinde değişiklik yapabilmek isterseniz baytlar yerine bayt dizileri ile çalışabilirsiniz. İşte bunun için bytearray() adlı bir fonksiyondan yararlanıyoruz.
 - Örnekler
 ```python
 a = bytes("A", "utf-8")
 a[0] #output: 65
 a[0] = 66   #output: TypeError: 'bytes' object does not support item assignment --> Hatası alırız
 
 a = bytearray('adana', 'ascii')
 a    #output: bytearray(b'adana')
 a[0] = 65
 a    #output: bytearray(b'Adana')   -->değiştirebiliyoruz
 ```
11. **chr()** :Bu fonksiyon, kendisine parametre olarak verilen bir tam sayının karakter karşılığını döndürür. Bu fonksiyon sayıları karakterlere dönüştürürken ASCII sistemini değil, UNICODE sistemini temel alır. 
 - `chr(10)   #output:'\n'`
12. **list()** :Bu fonksiyon iki farklı amaç için kullanılabilir:
 1. Liste tipinde bir veri oluşturmak
 2. Farklı veri tiplerini liste adlı veri tipine dönüştürmek
13. **set()** :fonksiyonunun görevi `küme` oluşturmak veya farklı veri tiplerini `kümey`e dönüştürmektir.
14. **tuple()** :fonksiyonunun görevi `demet` oluşturmak veya farklı veri tiplerini `demet`e dönüştürmektir.
15. **frozenset()** :Bu fonksiyonu kullanarak farklı veri tiplerini dondurulmuş kümeye dönüştürebilirsiniz.
16. **complex()** :herhangi bir sayıyı karmaşık sayıya dönüştürür.
17. **float()** :Bu fonksiyonu, sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürmek için kullanıyoruz.
18. **int()** :Bu fonksiyon birkaç farklı amaç için kullanılabilir. 
 - int() fonksiyonunun en temel görevi, bir karakter dizisi veya kayan noktalı sayıyı (eğer mümkünse) tam sayıya dönüştürmektir. Örnek: `int('10') #output:10`
 - herhangi bir sayma sisteminde temsil edilen bir sayıyı onlu sayma sistemine dönüştürmek için de kullanabiliriz. Örneğin:
  - `int('12', 8)     #output:10 --> Sayının karakter dizisi olarak verildiğine dikkat ediniz`
  - `int('4cf', 16)   #output:1231`  
  - `int("111111", 2)  #output:63`
19. **str()** :Bu fonksiyonun, farklı veri tiplerini karakter dizisine dönüştürmek için kullanıldığını biliyorsunuz. 
 ```python
 bayt = b'istihza'
 hatalı_cevrim = str(bayt)   #output: "b'ozgur'"  --> istemzsin büyük ihtimalle bunu :)
 kardiz = str(bayt, encoding='utf-8')
 print(kardiz)   #output: istihza
 
 bayt = bytes('özgür', encoding='utf-8')
 print(bayt)   #output: b'\xc3\xb6zg\xc3\xbcr'
 ```
20. **dict()** :Bu fonksiyon, farklı veri tiplerinden sözlükler üretmemizi sağlar. Örneğin bu fonksiyonu kullanarak boş bir sözlük oluşturabiliriz.
21. **callable()** :Bu fonksiyon, bir nesnenin ‘çağrılabilir’ olup olmadığını denetler. Peki hangi nesneler çağrılabilir özelliktedir. Mesela fonksiyonlar çağrılabilir nesnelerdir. Değişkenler ise çağrılabilir nesneler değildir. True - False
22. **ord()** :Bu fonksiyon, bir karakterin karşılık geldiği ondalık sayıyı verir. Örneğin: `ord('a')   #output: 97`
23. **oct()** :Bu fonksiyon, bir sayıyı sekizli düzendeki karşılığına çevirmemizi sağlar.
24. **hex()** :Bu fonksiyon, bir sayıyı onaltılı düzendeki karşılığına çevirmemizi sağlar.
25. **eval(), exec(), globals(), locals(), compile()** : Kaynakça: http://belgeler.istihza.com/py3/gomulu_fonksiyonlar.html#eval-exec-globals-locals-compile
26. **enumerate()** :İngilizcede enumerate kelimesi ‘numaralandırmak’ anlamına gelir. enumerate() fonksiyonunun görevi de kelimenin bu anlamıyla aynıdır. Yani bu fonksiyonu kullanarak nesneleri numaralandırabiliriz. Örnek: `list(enumerate('istihza'))   #output: [(0, 'i'), (1, 's'), (2, 't'), (3, 'i'), (4, 'h'), (5, 'z'), (6, 'a')]`
27. **exit()** :Bu fonksiyon, o anda çalışan programdan çıkmanızı sağlar. Eğer bu komutu etkileşimli kabukta verirseniz o anda açık olan oturum kapanacaktır.
28. **help()** :fonksiyonu gömülü fonksiyonlar içinde en faydalı fonksiyonların başında gelir. Bu fonksiyonu kullanarak Python programlama diline ait öğelere ilişkin yardım belgelerine ulaşabiliriz. Örneğin:`help(dir)`
29. **id()** :Python’da her nesnenin bir kimliğinin olduğunu biliyorsunuz. Python’daki her nesnenin kimliği eşşiz, tek ve benzersizdir.
30. **input()** :bu gömülü fonksiyonu kullanarak kullanıcı ile veri alışverişinde bulunabiliyoruz.
31. **format()** :
 Bu gömülü fonksiyonun görevi, daha önce karakter dizilerini işlerken, karakter dizilerinin bir metodu olarak öğrendiğimiz format() metodununa benzer bir şekilde, karakter dizilerini biçimlendirmektir. Ancak format() fonksiyonu, daha önce öğrendiğimiz format() metoduna göre daha dar kapsamlıdır. format() metodunu kullanarak oldukça karmaşık karakter dizisi biçimlendirme işlemlerini gerçekleştirebiliriz, ama birazdan inceleyeceğimiz format() gömülü fonksiyonu yalnızca tek bir değeri biçimlendirmek için kullanılır.
 `'{:.2f}'.format(12)   #output:12.00`
32. **filter()** :Bu gömülü fonksiyon yardımıyla dizi niteliği taşıyan nesneler içindeki öğeler üzerinde belirli bir ölçüte göre bir süzme işlemi uygulayabiliriz.
33. **len()**: Bu fonksiyon yardımıyla nesnelerin uzunluklarını hesaplayabileceğimizi biliyorsunuz.
34. **map()** : Haritalamaya yarar :) Örnek:
 ```python
 def karesini_bul(n):
	return n ** 2

liste = [1, 4, 5, 4, 2, 9, 10]
map_liste = list(map(karesini_bul, liste))
print(map_liste)   #output: [1, 16, 25, 16, 4, 81, 100]
 ```
35. **max()** :fonksiyonunun görevi, bir dizi içindeki en büyük öğeyi vermektir. 
36. **min()** :min() fonksiyonu max() fonksiyonunun tam tersini yapar.
37. **open()** :Bu fonksiyon herhangi bir dosyayı açmak veya oluşturmak için kullanılır.Bu fonksiyonun formülü şudur:
 ```python
 open(dosya_adi, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
 ```
38. **pow()** : Daha önceki derslerimizde pek çok kez örneklerini verdiğimiz bu fonksiyon İngilizcedeki power (kuvvet) kelimesinin kısaltmasından oluşur. Adının anlamına uygun olarak, bu fonksiyonu bir sayının kuvvetlerini hesaplamak için kullanıyoruz. Örnek: `pow(2, 3)   #output:8`
39. **print()** :Bu fonksiyonu, bildiğiniz gibi, kullanıcılarımıza birtakım mesajlar göstermek için kullanıyoruz.
 ```python
 print(deg1, deg2, deg3, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
 ```
40. **quit()** :Bu fonksiyonu programdan çıkmak için kullanıyoruz. Eğer bu fonksiyonu etkileşimli kabukta verecek olursanız etkileşimli kabuk kapanacaktır.
41. **range()** :Bu fonksiyonu belli bir aralıktaki sayıları listelemek için kullanıyoruz.
42. **reversed()** : Tersyüz etmek için
43. **sorted()** :Bu metot, daha önceki derslerimizden de bildiğiniz gibi, bir dizi içindeki öğeleri belirli bir ölçüte göre sıraya dizmemizi sağlıyor. Bununla ilgili çok basit bir örnek verelim: `sorted('ahmet')   #output:['a', 'e', 'h', 'm', 't']`
44. **slice()** :birtakım öğelerden oluşan bir nesnenin yalnızca belli kısımlarını ayırıp alma işlemi
45. **sum()** :Bu fonksiyonun temel görevi, bir dizi içindeki değerlerin toplamını bulmaktır.
46. **type()**: type() fonksiyonunun görevi bir nesnenin hangi veri tipine ait olduğunu söylemektir.
47. **zip()** : Kaynakçadan örnekleri inceleyiniz.
48. **vars()** :u fonksiyon, mevcut isim alanı içindeki metot, fonksiyon ve nitelikleri listeler. Eğer bu fonksiyonu parametresiz olarak kullanırsak, daha önce gördüğümüz locals() fonksiyonuyla aynı çıktıyı elde ederiz. Örnek:

 ```python
 
 vars()
 vars(str)
 vars(list)
 vars(dict)
 ```


