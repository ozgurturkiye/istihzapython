## Çoklu Miras Alma

r"""
Kısaltmaların Anlamları

    sn: sınıf niteliği
    on: örnek niteliği
    om: örnek metodu

"""

class Sinif_1:
    sn1 = 'Sınıf Niteliği - 1'

    def __init__(self):
        self.on1 = "Örnek Niteliği - 1"
        print(self.on1)

    def ornek_metot1(self):
        self.om1 = "Örnek Metodu - 1"
        return self.om1

class Sinif_2:
    sn2 = 'Sınıf Niteliği - 2'

    def __init__(self):
        self.on2 = "Örnek Niteliği - 2"
        print(self.on2)

    def ornek_metot2(self):
        self.om2 = "Örnek Metodu - 2"
        return self.om2


class AltSinif(Sinif_1, Sinif_2):
    def __init__(self):
        super().__init__()
