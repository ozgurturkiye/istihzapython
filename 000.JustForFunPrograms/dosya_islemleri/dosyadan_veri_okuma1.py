#3. Program: Kullanıcı adı ve parola ile doğru giriş yapıldığında(dosyadan kontrol edilecek)
#Dosyada kullanıcı adı parola durumuna göre 3 ayrı çözüm
##1. usernamepassword
##2. username password
##3. username
###  password


#1. Durumun çözümü (usernamepassword) dosyada şeklinde kayıtlı
username = input("Kullanıcı adını giriniz: ")
password = input("Parolayı giriniz: ")
kontrol = username+password

with open("durum1.txt", "r") as f:
	veri1 = f.read()   #read() metodu ile karakter dizisi olarak okuyoruz sonunda "\n" var!

veri_edit = veri1[:-1]   #Sondaki "\n" karakterini siliyoruz

if veri_edit == kontrol:
	print("Tebrikler")
else:
	print("Hatalı giriş")

print("Kullanıcı adı ve parola", repr(kontrol), type(kontrol)) #Bakalım gerçekten ne var
print("Dosyadan okunan veri", repr(veri1), type(veri1)) #Bakalım gerçekten ne var
print("Düzenlenmiş veri", repr(veri_edit), type(veri_edit)) #Bakalım gerçekten ne var
