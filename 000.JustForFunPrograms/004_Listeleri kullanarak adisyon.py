#Listeleri kullanarak 1 masanın hesabını tutan program 

urunler = ["cay", "kahve", "su"]  #urunleri tanımlıyoruz

#henüz dictionaries veri tipini öğrenmediğimiz  ve 
##Python'da associated liste olmadığı için(çünkü dictionaries var)
#her bir isme urunlerdeki index değerini atıyoruz.
cay, kahve, su = 0, 1, 2

#Ürinlerin fiyatlarını tutacağımız fiyatlar listesini oluşturuyoruz
#fiyatlar = [i for i in range(len(urunler))
fiyatlar = [2, 5, 1.5]

#Masanın hesabının tutulacağı masa1 listesini oluşturuyoruz.
masa1 = [0 for i in range(len(urunler))]

#Lets begin

giriş = """
(1) cay
(2) kahve
(3) su
(4) HESABI YAZDIR!
"""

print(giriş)

while True:
    soru = input("Girmek istediğiniz ürünün numarasını girin \n (Çıkmak için q): \n YAZDIRMAK İÇİN(4) ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        cay_adedi = int(input("İçilen çay adedini girin: "))
        masa1[cay] += cay_adedi
        print("Masada içilen toplam çay: {}".format(masa1[cay]))

    elif soru == "2":
        kahve_adedi = int(input("İçilen kahve adedini girin: "))
        masa1[kahve] += kahve_adedi
        print("Masada içilen toplam kahve: {}".format(masa1[kahve]))

    elif soru == "3":
        su_adedi = int(input("İçilen su adedini girin: "))
        masa1[su] += su_adedi
        print("Masada içilen toplam su: {}".format(masa1[su]))

    elif soru == "4":
    	print("Hesaplanıyor....")
    	print("Toplam cay ucreti = {}TL".format(masa1[cay] * fiyatlar[cay]))
    	print("Toplam kahve ucreti = {}TL".format(masa1[kahve] * fiyatlar[kahve]))
    	print("Toplam su ucreti = {}TL".format(masa1[su] * fiyatlar[su]))
    	#Bu kısımda for döngüsü kullanılarak 2 liste toplam ücreti bulmak için sıra ile birbiri ile çarpılacak
    	toplam = 0
    	for i in range(len(masa1)):
    		toplam += masa1[i] * fiyatlar[i]
    	print("HESAP: {}TL".format(toplam))
    		
    	#print("Toplam ödenmesi gereken tutar {}TL".format())
    	#print("Toplam çay fiyatı {}  {}".format(masa1[cay], fiyatlar[cay])
    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)
