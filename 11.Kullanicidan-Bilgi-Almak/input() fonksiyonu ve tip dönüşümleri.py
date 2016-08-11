veri = input("Lütfen bir sayı giriniz: \n")

#Input() ile alınan veri her zaman karakter dizisi olarak gelir
print("Input ile alınan veri tipi", type(veri), "Değeri", veri)

#Tip dönüşümleri

string_yap  = str(veri)
integer_yap = int(veri)
float_yap   = float(veri)
complex_yap = complex(veri)


#format metodu kullanılarak yazdırma

metin = "Dönüştürülen tip: {} Değer: {}"
print(metin.format(type(string_yap), string_yap))
print(metin.format(type(integer_yap), integer_yap))
print(metin.format(type(float_yap), float_yap))
print(metin.format(type(complex_yap), complex_yap))
