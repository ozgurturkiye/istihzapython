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
masa1 = [i for i in range(len(urunler))]

#Lets begin

giriş = """
(1) cay
(2) kahve
(3) su
(4) HESABI YAZDIR!
"""

print(giriş)

while True:
    soru = input("Girmek istediğiniz ürünün numarasını girin \n (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        cay_adedi = int(input("İçilen çay adedini girin: "))
        masa1[cay] += cay_adedi
        print("Masada içilen toplam çay: {}".format(masa1[cay]))

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)
