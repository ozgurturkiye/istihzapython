#PNG dosyları
#PNG dosyasının ilk 8 baytı mutlaka aşağıdaki değerleri içeriyor:

#onlu değer	137 80 78 71 13 10 26 10
#on altılı değer	89 50 4e 47 0d 0a 1a 0a
#karakter değeri	\211 P N G \r \n \032 \n

f = open("falanca.png", "rb")
okunan = f.read(8)

okunan == b"\211PNG\r\n\032\n"   #Kontrol ediyoruz True or False

#GIF
#Bir dosyanın GIF olup olmadığına karar verebilmek için ilk 3 baytını okumanız yeterli olacaktır. 
#16.05.2016 itibariyle GIF standardının şu sürümleri bulunmaktadır:
##87a - Mayıs 1987
##89a - Temmuz 1989
#Dolayısıyla standart bir GIF dosyasının ilk 6 baytı şöyledir:

‘GIF87a’ veya ‘GIF89a’

#TIFF
#TIFF dosyası şunlardan herhangi biri ile başlar: ‘II’ veya ‘MM’
#Dolayısıyla, bir TIFF dosyasını tespit edebilmek için dosyanın ilk 2 baytına bakmanız yeterli olacaktır

#BMP
#BMP dosyaları ‘BM’ ile başlar. 

#Genel Örnek
for f in dosyalar:
    okunan = open(f, 'rb').read(10)
    if okunan[6:11] in [b'JFIF', b'Exif']:
        print("{} adlı dosya bir JPEG!".format(f))
    elif okunan[:8] == b"\211PNG\r\n\032\n":
        print("{} adlı dosya bir PNG!".format(f))
    elif okunan[:3] == b'GIF':
        print("{} adlı dosya bir GIF!".format(f))
    elif okunan[:2] in [b'II', b'MM']:
        print("{} adlı dosya bir TIFF!".format(f))
    elif okunan[:2] in [b'BM']:
        print("{} adlı dosya bir BMP!".format(f))
    else:
        print("Türü bilinmeyen dosya: {}".format(f))
