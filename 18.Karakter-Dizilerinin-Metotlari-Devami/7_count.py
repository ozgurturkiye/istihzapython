## count() istenen karakteri sayar


## count() - ornek_1
metin = """
Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır diyebiliriz.
"""
print(metin)
karakter = input("Yukarıdaki metinde sayısını bumak istediğiniz karakteri yazınız...:")

print(karakter,"karakterinden",metin.count(karakter),"adet bulunmaktadır!!!")
##
##
#### count() - ornek_2 (Bir karakterden an fazla 1 tane kullanmaya zorluyoruz)
##parola = input("parolanız: ")
##kontrol = True
##for i in parola:
##    if parola.count(i) > 1:
##        kontrol = False
##if kontrol:
##    print('Parolanız onaylandı!')
##else:
##    print('Parolanızda aynı harfi bir kez kullanabilirsiniz!')


#### count() - ornek_3 (kullanıcının girdigi bir kelime içindeki bütün har2erin o kelime içinde
####kaç kez geçtigini bulmak.)
##kelime = input("Herhangi bir kelime: ")
##
##for harf in kelime:
##    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))
## Buradaki sorunu halletmek için şöyle düzenleyebiliriz
##kelime = input("Herhangi bir kelime: ")
##sayac = ""
##
##for harf in kelime:
##    if harf not in sayac:
##        sayac += harf
##        
##for harf in sayac:
##    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,kelime,kelime.count(harf)))
