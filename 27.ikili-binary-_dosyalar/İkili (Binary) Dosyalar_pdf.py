#İkili (Binary) Dosyalar
##1.Metin dosyları 2.Binary Dosyalar => Aslında hepsi binary :)

# f = open(dosya_adı, 'rb')
#ikili dosyaları açarken "rb" "wb" "ab" "xb" vb. kullanıyoruz.

#PDF Dosyalarından Bilgi Alma
f = open("falanca.pdf", "rb")
f.read(10)  #output: b'%PDF-1.4\n%'

#Belgeyi pdf ye çeviren yazılımı bulma
f = open("falanca.pdf", "rb")
okunan = f.read()
producer_index = okunan.index(b"/Producer")
#producer_index değişkeni, ‘/Producer’ ifadesinin ilk baytının dosya içindeki konumunu tutuyor. 
#producer_index           # output:4077883
#okunan[producer_index]   # output:47
#chr(okunan[producer_index])   #output:"/"
okunan[producer_index:producer_index+50]  #output: b'/Producer (Acrobat Distiller 2.0 for Macintosh)\r/T'
