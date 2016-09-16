## sinif.py - Aleni Üyeler

class Sinif():
    sinif_niteligi = 0

    def ornek_metodu(self):
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
    >>> dir(s)             ## dir() komutunun çıktısında görünen ve
        normal yollardan erişebildiğimiz bütün bu öğeler birer aleni üyedir.

    >>> s.statik_metod()
    
    >>> s.ornek_metodu()
    
    >>> s.sinif_metodu()

    >>> s.sinif_niteligi
    
"""
