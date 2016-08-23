#Resim Dosyalarının Türünü Tespit Etme
##Asla unutmayın dosya uzantıları ile dosya biçimleri arasında doğrudan bir bağlantı yoktur.

#JPG
#FF  D8      FF      E0      ?   ?   4A      46      49      46      00
#FF  D8      FF      E0      ?   ?   45  78  69  66  00

#Yukarıda gördükleriniz birer on altılı (hex) sayıdır. Bunlar onlu düzende sırasıyla şu sayılara karşılık gelir:
#255 216 255 224 ? ? 74 70 73 70 0
#255 216 255 224 ? ? 45 78 69 66 0 #canon

#74 70 73 70          => ‘J’, ‘F’, ‘I’, ‘F’
#45 78 69 66 #canon   => ‘E’, ‘x’, ‘i’, ‘f’  karakter karşılıkları

#Dosyanın jpg olup olmadığını kontrol etmek. Büyük küçük harf duyarlı unutma
f = open(dosya_adı, 'rb')
data = f.read(10)
if data[6:11] in [b"JFIF", b"Exif"]:
    print("Bu dosya JPEG!")
else:
    print("Bu dosya JPEG değil!")
    
#Birden fazla dosya kontrol etme
dosyalar = ["d1.jpg", "d2.jpg", "d3.jpeg"]  #dosya isimlerinin listeye alıyoruz

for f in dosyalar:
    okunan = open(f, 'rb').read(10)
    if okunan[6:11] in [b'JFIF', b'Exif']:
        print("Evet {} adlı dosya bir JPEG!".format(f))
    else:
        print("{} JPEG değil!".format(f))
