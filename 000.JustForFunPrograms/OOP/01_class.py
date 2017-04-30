# Üç Temel sınıf tanımlama yöntemi

class Sınıf:
    pass

class Sınıf():
    pass

class Sınıf(object):
    pass

#class inheritence - Sınıf mirasları

class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    def __init__(self, isim, rütbe):
        super().__init__(isim, rütbe)
        self.güç = 100

    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı.')

class Süvari(Oyuncu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.güç = 200
    
    def hareket_et(self):
        super().hareket_et()
        print("Süvari koşuyor... ve hedefe ulaştı")
