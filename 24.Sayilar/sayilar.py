#Python’da üç tür sayı olduğunu biliyoruz:
#1.Tam Sayılar (integers)
#2.Kayan Noktalı Sayılar (floating point numbers veya kısaca floats)
#3.Karmaşık Sayılar (complex numbers)
"""
Fonksiyon	      Görevi	                                       Örnek
int()         	Bir veriyi tam sayıya dönüştürür	             int('2')
float()	        Bir veriyi kayan noktalı sayıya dönüştürür	   float(2)
complex()     	Bir veriyi karmaşık sayıya dönüştürür	         complex(2)
"""

#Tam Sayıların Metotları
#bit_length()   integer sayının bellekte kaç bit yer kapladığını söyler
sayı = 10
sayı.bit_length()  #output : 4
(10).bit_length()  #output : 4  Dikkat sayıyı parantez içine almazsan hata verir sebebi sayıyı float olarak algılaması

#Kayan Noktalı Sayıların Metotları
#as_integer_ratio()
#is_integer() Bir kayan noktalı sayının ondalık kısmında 0 harici bir sayının olup olmadığını kontrol etmek için
(12.0).is_integer() # output: True

#Karmaşık Sayıların Metotları
#imag   İşte imag adlı nitelik, bize bir karmaşık sayının sanal kısmını verir:
#real   real adlı nitelik bize bir karmaşık sayının gerçek kısmını verir:
c = 12+4j
c.imag    #output: 4.0
c.real    #output: 12.0
# Bu iki metot (imag ve real) parantezsiz kullanılıyor, eğer parantezli yazarsak c değişkenini float sanıyor

#Aritmetik Fonksiyonlar
##Bilgi: Gömülü fonksiyonlar, Python programlama dilinde,
###herhangi bir özel işlem yapmamıza gerek olmadan, kodlarımız içinde doğrudan kullanabileceğimiz fonksiyonlardır.
#abs() Bu fonksiyon bize bir sayının mutlak değerini verir:
#divmod() Bu fonksiyon, bir sayının bir sayıya bölünmesi işleminde bölümü ve kalanı verir:
##Bu sonuçtan gördüğünüz gibi, aslında divmod() fonksiyonu şu kodlarla aynı işi yapıyor:
14 // 3, 14 % 3
#max()
#min()
#sum() Bu fonksiyon bir dizi içinde yer alan bütün sayıları birbiriyle toplar. 
a = [10, 20, 43, 45 , 77, 2, 0, 1]
print(sum(a))  #output: 198

