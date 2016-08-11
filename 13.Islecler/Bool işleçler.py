#http://belgeler.istihza.com/py3/islecler.html
#Bununla ilgili genel kuralımız şu: 0 değeri ve boş veri tipleri False‘tur. 
#Bunlar dışında kalan her şey ise True‘dur.


bool()       # output: False
bool(0)      # output: False
bool("")     # output: False

bool("0")    # output: True
bool(" ")    # output: True
bool(1)      # output: True
bool("elma") # output: True

a = ""
bool(a)      # output: False

b = "123"
bool(b)      # output: True

#Example

kullanıcı_adı = input("Kullanıcı adı: ")
parola = input("Parola: ")

if kullanıcı_adı == "Özgür" and parola == "321":
	print("Giriş başarılı")
else:
	print("Kullanıcı adı veya parola hatalı!")

#Not harf dönüşümü örneği

x = int(input("Notunuz: "))

if x > 100 or x < 0:
    print("Böyle bir not yok")

#x, 90 ile 100 arasında bir sayı ise
elif x >= 90 and x <= 100:
    print("A aldınız.")

elif x >= 80 and x <= 89:
    print("B aldınız.")

elif x >= 70 and x <= 79:
    print("C aldınız.")

elif x >= 60 and x <= 69:
    print("D aldınız.")

elif x >= 0 and x <= 59:
    print("F aldınız.")

