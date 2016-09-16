## Miras (Inheritance) Alma - Taban Sınıf ve Alt Sınıflar
## uygula_miras_alma.py dosyası miras_alma.py modülünü içe aktararak
## (import ederek) işlemler yapar

import miras_alma   ## miras_alma.py modülünü içe aktar

## -------------------------------------
asker_1 = miras_alma.Asker('Ahmet', 'Er')

print(asker_1.isim, asker_1.rutbe, asker_1.guc, sep = ', ')

asker_1.guc = 50

print(asker_1.isim, asker_1.rutbe, asker_1.guc, sep = ', ')
## -------------------------------------
print("-"*30)

isci_1 = miras_alma.Isci('Mehmet', 'Usta')
isci_2 = miras_alma.Isci('Mahmut', 'Kalfa')

print(isci_1.isim, isci_1.rutbe, isci_1.guc, sep = ', ')
print(isci_2.isim, isci_2.rutbe, isci_2.guc, sep = ', ')
## -------------------------------------
print("-"*30)

yonetici_1 = miras_alma.Yonetici('Erhan', 'Supervisor')

yonetici_1.puan_kazan()
## -------------------------------------
print("-"*30)

isci_1.hareket_et()
isci_1.puan_kaybet()
## -------------------------------------
print("-"*30)

asker_2 = miras_alma.Asker('Kemal', 'Albay')
yonetici_2 = miras_alma.Yonetici('Erhan', 'Müdür')

print(asker_2.isim)
print(asker_2.rutbe)
print(asker_2.guc)
print(yonetici_2.isim)
print(yonetici_2.rutbe)
print(yonetici_2.guc)
asker_2.hareket_et()
yonetici_2.hareket_et()
