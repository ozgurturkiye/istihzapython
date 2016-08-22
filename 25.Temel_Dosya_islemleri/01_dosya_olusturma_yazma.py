#Kaynak: http://belgeler.istihza.com/py3/temel_dosya_islemleri.html
#Temel Dosya İşlemleri
#Python’daki ‘Dosya Girdi/Çıktısı’ (File I/O)

#Dosya Oluşturmak
# f = open(dosya_adı, kip)
tahsilat_dosyası = open("tahsilat_dosyası.txt", "w") #Bulunduğu dizinde tahsilat_soyası adında dosya açar
#istediğin dizinde dosya açmak için Not: Ters taksim kullanmalısın
dosya = open("/dosyayı/oluşturmak/istediğimiz/dizin/dosya_adı", "w")

#Dosyaya Yazmak
# dosya.write(yazılacak_şeyler)
ths = open("tahsilat_dosyası.txt", "w")
ths.write("Halil Pazarlama: 120.000 TL"),
ths.close()

##Python’da bir dosyayı “w” kipinde açtığımızda, eğer o adda bir dosya ilgili dizin içinde zaten varsa, 
##Python bu dosyayı sorgusuz sualsiz silip, yerine aynı adda başka bir boş dosya oluşturacaktır.
