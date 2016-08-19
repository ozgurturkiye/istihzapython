#onlu, sekizli, on altılı ve ikili sayma sistemleri
#Rakamlar, sayıları göstermeye yarayan simgelerdir.

sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]

print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))

for i in range(17):
    print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))

#Espirimizi yapalım
##İnsanlar 10’a ayrılır: İkili sistemi bilenler ve bilmeyenler!

#Sayma Sistemlerini Birbirine Dönüştürme
##Fonksiyon kullanarak

#bin() Bu fonksiyon bir sayının ikili (binary) sayı sistemindeki karşılığını verir:
bin(2)  #output: '0b10' ->Bu fonksiyonun çıktı olarak bir karakter dizisi verdiğine dikkat edin.

#hex()
hex(10)  #output: 'Oxa'

#oct()
oct(10)  #output: '0o12'

#int() herhangi bir sayı veya sayı değerli karakter dizisini tam sayıya (integer) dönüştürmek için kullanılıyor.
int('7bc', 16)   #output: 1980
int('1100', 2)   #output: 12
int('1100', 8)   #output: 576
int('1100', 16)  #output: 4352

#Biçimlendirme Yoluyla

'{:b}'.format(12)   #output: 1100  -->bir sayıyı ikili düzendeki karşılığına dönüştür
'{:x}'.format(1980) #output: '7bc' -->bir sayıyı hex() düzendeki karşılığına dönüştür
'{:o}'.format(1980) #output: '3674'-->octal(8'li) karşılığı

#Örnek uygulama
n = '7bc'
"{} sayısının onlu karşılığı {} sayısıdır.".format(n, int(n, 16))
#output: '7bc sayısının onlu karşılığı 1980 sayısıdır.'
#Örnek format() metodu uygulama 
"|{:->10b}|".format(2)  #output: |--------10|
