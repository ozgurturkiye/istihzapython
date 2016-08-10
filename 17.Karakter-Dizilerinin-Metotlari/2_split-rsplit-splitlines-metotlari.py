## split(), rsplit(), splitlines() Metodları

## split() - ornek_1
kardiz = "İstanbul Büyükşehir Belediyesi"
print(kardiz.split())

#### split() - ornek_2
##for i in kardiz.split():
##    print(i)
##
#### split() - ornek_3
##kardiz = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin: ")
##for i in kardiz.split():
##    print(i[0], end="")
##
#### split() - ornek_4
##kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
##kardiz = kardiz.split(",")
##print(kardiz)
##
#### rsplit(); split() metodunun yaptığı işi sağdan sola okuyarak yapar.
##
#### splitlines()
##metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
##tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
##Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
##düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
##gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
##komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
##adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
##dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
##halini almıştır diyebiliriz."""
##print(metin.splitlines())
##
####print(metin.splitlines(True))
