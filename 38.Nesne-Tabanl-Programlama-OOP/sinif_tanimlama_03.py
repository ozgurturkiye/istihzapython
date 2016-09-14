## SINIF TANIMLAMAK

class Calisan():
    def __init__(self):
        self.kabiliyetleri = []
        self.unvani = ''


ahmet = Calisan()   ## Calisan sınıfından ahmet adlı bir örnek çıkarıyoruz

mehmet = Calisan()  ## Calisan sınıfından mehmet adlı bir örnek çıkarıyoruz

ahmet.kabiliyetleri.append('konuşkan')      ## ahmet'in örnek niteiklerinden kabiliyetleri listesine 'konuşkan' niteliğini ekliyoruz
ahmet.kabiliyetleri.append('cana yakın')    ## ahmet'in örnek niteiklerinden kabiliyetleri listesine 'cana yakın' niteliğini ekliyoruz

print(ahmet.kabiliyetleri)  ## ahmet örneğinin kabiliyetlerini yazdırıyoruz
print(mehmet.kabiliyetleri) ## mehmet örneğinin kabiliyetlerini yazdırıyoruz

mehmet.unvani = 'müdür'
ahmet.unvani = 'şef'

print("ahmet'in Ünvanı...:", ahmet.unvani)
print("mehmet'in Ünvanı..:", mehmet.unvani)
