#format() metodunun basit şekilde kullanımı

print("{} ve {} güzel bir ikilidir".format("Python", "Django"))
# output: Django ve Python iyi bir ikilidir!

#example 2
isim = input("İsminizi giriniz: ")
print("Hoşgeldin {}!".format(isim))

#example 3
kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

print("""{} noktasından {} noktasına, 14:30 hareket saatli
sefer için {} adına {} adet bilet ayrılmıştır!""".format(kalkış,
                                                         varış,
                                                         isim_soyisim,
                                                         bilet_sayısı))
                                                         
#example 4

print("{:c}".format(65))  # output: A
print("{:d}".format(65))  # output: 65
print("{:x}".format(65))  # output: 41  exadecimal karşılığı
print("{:b}".format(2))   # output: 10 binary karşılığı
