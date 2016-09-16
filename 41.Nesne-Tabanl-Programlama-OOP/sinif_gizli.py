## sinif_gizli.py - Gizli Üyeler

class Sinif():
    __gizli = 'Gizli'

    def ornek_metodu(self):
        print(self.__gizli)
        print("Örnek Metodu")

    @classmethod
    def sinif_metodu(cls):
        print("Sınıf Metodu")

    @staticmethod
    def statik_metod():
        print("Statik Metod")

r"""
    Etkileşimli kabukta şu komutları ver:

    >>> import sinif
    >>> s = sinif.Sinif()
    >>> s.__gizli
        HATA                 ## Sınıf dışından ulaşılamaz!
    >>> sinif.Sinif.__gizli    
        HATA                 ## Sınıf dışından ulaşılamaz!

    >>> s.ornek_metodu()     ## ornek_metodu içinden normal bir şekilde erişiliyor
    'Gizli'
    'Örnek Metodu' 

    --Gizli Üye Tanımlama Kuralları--
    Bir üyenin gizli olabilmesi için başında en az iki adet,
    ucunda da en fazla bir adet alt çizgi bulunmalıdır.
    Yani şunlar birer gizli üyedir:

    __gizli = 'gizli'
    __gizli_ = 'gizli'
    __gizli_uye = 'gizli'
    __gizli_uye_ = 'gizli'
    
"""
