## deneme.py

## Etkileşimli kabukta deneyebilir ya da bu dosyadan çalıştırabilirsin


#### Etkileşimli kabukta aşağıdaki komutları ver
#### Bu kodlar siparis_takip dizininin içindeyken etkileşimli kabuk oturumu açınca çalışır.
##
##import siparis_takip
##
##dir(siparis_takip)
##
##siparis_takip.__package__         ## Paket'mi kontrol ediyoruz.

## output: 'siparis_takip'


#### deneme.py dosyasını aşağıdaki kodlarla çalıştır
#### Bu kodlar siparis_takip dizininin bir üst dizinindeyken (komut satırında) deneme.py komutuyla çalışır.

import siparis_takip

print(dir(siparis_takip))

print(siparis_takip.__package__)    ## Paket'mi kontrol ediyoruz.

## output: siparis_takip

## Modülleri içe aktarmak için

from siparis_takip import siparis
