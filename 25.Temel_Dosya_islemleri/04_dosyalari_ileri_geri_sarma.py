#Dosyayı İleri-Geri Sarmak
#f.read() ile okuduğun anda dosyanın sonuna gider tekrar f.read() yaparsan "" ike karşılaşırsın

f.seek(0) #Dosyanın kaçınce BYTE'ına gitmek istiyorsak o paramatereyi veriyoruz
f.tell()  #dosyanın hangi bayt konumunda bulunduğumuzu öğrenmek
