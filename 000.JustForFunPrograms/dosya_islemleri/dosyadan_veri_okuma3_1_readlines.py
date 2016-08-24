#3. Program: Kullanıcı adı ve parola ile doğru giriş yapıldığında(dosyadan kontrol edilecek)
#Dosyada kullanıcı adı parola durumuna göre 3 ayrı çözüm
##1. usernamepassword
##2. username password
##3. username
###  password


#3. Durumun çözümü (username\npassword) dosyada şeklinde kayıtlı
#readlines() metodu kullanılarak
username = input("Kullanıcı adını giriniz: ")
password = input("Parolayı giriniz: ")

with open("durum3.txt", "r") as f:
	veri1 = f.readlines()   #readlines() metodu ile liste olarak okuyoruz

#veri1 liste öğelerinin sonunda ki \n karakterlerini siliyoruz
username_edit = veri1[0][:-1]   #Sondaki "\n" karakterini siliyoruz ve kayıt
password_edit = veri1[1][:-1]   #Sondaki "\n" karakterini siliyoruz ve kayıt

if username_edit == username and password_edit == password:
	print("Tebrikler")
else:
	print("Hatalı giriş")

print("Kullanıcı adı ve parola", repr(username), type(username), repr(password), type(password)) #Bakalım gerçekten ne var
print("Dosyadan okunan veri", repr(veri1), type(veri1)) #Bakalım gerçekten ne var
print("Düzenlenmiş veri[0]", repr(username_edit), type(username_edit)) #Bakalım gerçekten ne var
print("Düzenlenmiş veri[1]", repr(password_edit), type(password_edit)) #Bakalım gerçekten ne var
