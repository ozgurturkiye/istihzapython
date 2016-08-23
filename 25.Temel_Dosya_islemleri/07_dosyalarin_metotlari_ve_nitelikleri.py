#Dosyaların Metot ve Nitelikleri
#Dosyalar da, tıpkı karakter dizileri ve listeler gibi, 
##Python programlama dilindeki veri tiplerinden biridir. Dolayısıyla tıpkı karakter dizileri ve listeler gibi, 
##dosya (file) adlı bu veri tipinin de bazı metotları ve nitelikleri vardır.

#truncate() Metodu
#Bu metot yardımıyla dosyalarımızı istediğimiz boyuta getirebiliyoruz.

with open("falanca.txt", "r+") as f:
	f.truncate(10)

#Bu kodlar, falanca.txt adlı dosyanın ilk 10 baytı dışındaki bütün verileri siler. 
#Yani dosyayı yalnızca 10 baytlık bir boyuta sahip olacak şekilde kırpar.

#Dosya metotları()
readable()    | read()        | write()
writable()    | readline()    | writelines()
truncate()    | readlines()
open()        | seek()
close()       | tell()

#Dosya nitelikleri
closed
mode
name
encoding

#örneklerden, ‘metot’ ile ‘nitelik’ kavramları arasındaki farkı anladığınızı zannediyorum. 
##Metotlar bir iş yaparken, nitelikler bir değer gösterir. Nitelikler basit birer değişkenden ibarettir. 
##Metotlar ise bir işin nasıl yapılacağı ile ilgili süreci tanımlar.

