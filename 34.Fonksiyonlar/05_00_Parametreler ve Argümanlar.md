# Parametreler ve Argümanlar

> - Bir fonksiyonu tanımlarken belirlediğimiz adlara parametre, aynı fonksiyonu çağırırken belirlediğimiz adlara ise argüman deniyor.
> - Ancak şunu belirtmekte yarar var: Bu iki kavram genellikle birbirinin yerine kullanılır. Yani bu iki kavram arasındaki, yukarıda açıkladığımız farka pek kimse dikkat etmez. Dolayısıyla pek çok yerde hem parametre hem de argüman için aynı ifadenin kullanıldığını görebilirsiniz.

Gelelim parametrelerin çeşitlerine...

1. Sıralı (veya İsimsiz) Parametreler
 - Python’da, veriliş sırası önem taşıyan bu tür parametrelere `‘sıralı parametreler’ (veya isimsiz parametreler)` adı verilir.
 - `kayıt_oluştur("Ahmet", "Öz", "Debian", "Ankara")`
2. İsimli Parametreler
 - `kayıt_oluştur(soyisim="Öz", isim="Ahmet", işsis="Debian", şehir= "Ankara")`
 - Ancak burada dikkat etmemiz gereken bazı noktalar var. Python’da isimli bir parametrenin ardından sıralı bir parametre gelemez. 
3. Varsayılan Değerli Parametreler
 - Biz bu parametrelere kendimiz bir değer atamazsak Python bu parametrelere kendi belirlediği bazı öntanımlı değerleri atayacaktır.
  ```python
   def kur(kurulum_dizini="/usr/bin/"):
       print("Program {} dizinine kuruldu!".format(kurulum_dizini))
  
  kur()
  ```
