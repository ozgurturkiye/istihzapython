## Miras (Inheritance) Alma - Taban Sınıf ve Alt Sınıflar
## miras_alma.py modülü üzerinde yapılacak örnek işlemler uygula_miras_alma.py dosyasında

class Oyuncu():         ## Taban Sınıf ve metodları
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı...')

    def puan_kaybet(self):
        print('puan kaybedildi...')

## 1. Yöntem - Tüm metot ve nitelikleri olduğu gibi miras alma


##class Asker(Oyuncu):    ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
##    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir
##
##class Isci(Oyuncu):     ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
##    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir
##
##class Yonetici(Oyuncu): ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
##    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir


## 2. Yöntem - Miras alınan metotlarında değişiklik yapma veya nitelik ekleme
        

##class Asker(Oyuncu):
##    memleket = 'Ankara' ## Yeni bir sınıf niteliği ekliyor
##
##    def hareket_et(self):   ## Metodun ismi aynı olduğu için miras alınan metodun yerine geçiyor!!!
##        print('Yeni hareket et')
##
##class Isci(Oyuncu):     ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
##    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir
##
##class Yonetici(Oyuncu): ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
##    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir
##


## self.guc değerinin her bir alt sınıfta farklı olabilmesi
##        isim ve rutbe değerlerinin de
## miras alınan taban sınıftan aynen aktarılabilmesi için (super() fonksiyonu)

class Asker(Oyuncu):
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)   ## Buradaki super() fonksiyonu sayesinde miras alınan isim ve rutbe
        self.guc = 100                  ## değerleri korunurken, guc değeri Asker alt sınıfına özgü olarak 100 verildi!!!
        
## Miras alınan metot için de kullanılabilir

    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı')

class Isci(Oyuncu):     ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir

class Yonetici(Oyuncu): ## Alt Sınıf (Oyuncu sınıfından türetilmiş)
    pass                ## Miras alınan sınıfın bütün nitelik ve metotları alt sınıfa oldugu gibi devredilir

