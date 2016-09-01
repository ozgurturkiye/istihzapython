# Modüller
## Modül Nedir?
> Bu soruyu, şimdiye kadar gördüğümüz modüllere bakarak cevaplayacak olursak, modüllerin, bazı işlevleri kolaylıkla yerine getirmemizi sağlayan birtakım fonksiyonları ve nitelikleri içinde barındıran araçlar olduğunu söyleyebiliriz.

> Python’ın fonksiyon sistemi nasıl bize bir işlevselliği aynı dosya içinde tekrar tekrar kullanma imkanı veriyorsa, modül sistemi de bir fonksiyonu farklı dosyalar ve programlar içinde tekrar tekrar kullanma imkanı verir.

> Dolayısıyla modüller sayesinde, bir kez yazdığımız kodları pek çok farklı program içinde kullanma imkanı elde ediyoruz. Bu da bizim;

 - Daha az kod yazmamızı,
 - Bir kez yazdığımız kodları tekrar tekrar kullanabilmemizi,
 - Daha düzenli, daha derli toplu bir şekilde çalışabilmemizi

> sağlıyor.

# Hazır Modüller
Hatırlarsanız, Python’da iki farklı fonksiyon türü olduğundan söz etmiştik:

1. Kendi tanımladığımız fonksiyonlar
2. Gömülü (‘built-in’) fonksiyonlar

Aynı şekilde modüller de iki farklı başlık altında incelenebilir:

1. Kendi tanımladığımız modüller
 - Standart Kütüphane Modülleri
 - Üçüncü Şahıs Modülleri
2. Hazır modüller

# Modüllerin İçe Aktarılması
> Python’da herhangi bir modülü kullanabilmek için öncelikle onu ‘içe aktarmamız’ gerekir. İçe aktarmak, bir modül içindeki fonksiyon ve nitelikleri başka bir program (veya ortam) içinden kullanılabilir hale getirmek demektir.
```python
import os    #modülü içe aktarmak "os" (operating system) kısaltmasıdır
dir(os)      #os modülünün bize hangi yararlı fonksiyonları ve nitelikleri sunduğunu öğrenmek için
os.name      #Bu nitelik, bize kodlarımızın hangi işletim sisteminde çalıştığını gösterir. 'posix' linux, 'nt' windows
```
**import modül_adı as farklı_isim**
```python
import modül_adı as farklı_bir_isim
```
**from modül_adı import isim1, isim2**,
