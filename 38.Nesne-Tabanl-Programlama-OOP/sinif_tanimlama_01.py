## SINIF TANIMLAMAK

## Fonksiyon olarak tanımlanınca çalışması için fonksiyonun çağırılması gerekli

##def calisan():
##    kabiliyet = []
##    unvani = 'işçi'
##
##    print(kabiliyet)
##    print(unvani)

##calisan()   ## Fonksiyon çağırılıyor

## sınıf olarak tanımlama

class Calisan():
    kabiliyet = []
    unvani = 'işçi'
    maasi = 1500
    memleketi = '..'
    dogum_tarihi = ''

    print(kabiliyet)
    print(unvani)
    print(maasi)
    print(memleketi)

##print(Calisan.kabiliyet)
##print(Calisan.unvani)
##print(Calisan.maasi)
##print(Calisan.memleketi)

class Asker():
    rutbesi = 'Er'
    techizat = ['G3', 'kasatura', 'süngü', 'el bombası']
    birlik = '4. Piyade Tugayı'


Ahmet = Calisan()
print(Ahmet)

Mehmet = Asker()
print(Mehmet.birlik)
Mehmet.rutbesi = 'Albay'
print(Mehmet.rutbesi)
print(Mehmet.birlik)
