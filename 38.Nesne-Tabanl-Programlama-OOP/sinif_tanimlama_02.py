## SINIF TANIMLAMAK

## Örnek Nitelikleri
## __init__ fonksiyonu ve self

class Selamla():
    selam = 'merhaba'
    print(selam)

class Selamla_2():
    def __init__(self):
        self.selam = 'Merhaba'
        print(self.selam)

meraba_2 = Selamla_2()

##---------------------
print("Sınıf niteliği")

print(Selamla.selam)    ## Sınıf niteliğine sınıf adını kullanıyoruz

##---------------------
print("Örnek niteliği")

print(meraba_2.selam)   ## Örnek niteliğine örnek adını kullanıyoruz
