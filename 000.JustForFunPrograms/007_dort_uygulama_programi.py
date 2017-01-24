#Bu kısımda 4 uygulama programı yazalım bakalım Python'da ne kadar ilerlemişiz.
#1. Program: 4 işlem yapan hesap makinası
#2. Program: Kullanıcı ad, soyad, doğum tarihi, cinsiyet bilgilerini alıp dosyaya kaydeden program
#3. Program: Kullanıcı adı ve parola ile doğru giriş yapıldığında(dosyadan kontrol edilecek) 
            ##dosyadan kayıtlı kullanıcı bilgilerini çeken ekrana yazdıran program
#4. Program: Girilen ismin binary karşılığını dosyaya yazan ve 
            ##dosyadaki binary veriyi karakter dizisi(unicode - utf8) olarak okuyan program


#1. Program - Hesap makinası Let's begin :)
metin = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
Seçiminizi yapınız
Çıkmak için (q) ya basınız
"""
#devam edecek :)
d ="Devam etmek için bir tuşa basınız"
while True:
    try:
        print(metin)
        sec = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
        
        def sayi_gir():
          number1 = int(input("Birinci Sayı: "))
          number2 = int(input("İkinci Sayı: "))
          return number1, number2
        
        if sec == "1":
            sayi1, sayi2 = sayi_gir()
            sonuc = sayi1 + sayi2
            print("{} + {} = {}".format(sayi1, sayi2, sonuc))
            input(d)
        elif sec == "2":
            sayi1, sayi2 = sayi_gir()
            sonuc = sayi1 - sayi2
            print("{} - {} = {}".format(sayi1, sayi2, sonuc))
            input(d)
        elif sec == "3":
            sayi1, sayi2 = sayi_gir()
            sonuc = sayi1 * sayi2
            print("{} * {} = {}".format(sayi1, sayi2, sonuc))
            input(d)
        elif sec == "4":
            try:
              sayi1, sayi2 = sayi_gir()
              sonuc = sayi1 / sayi2
              print("{} / {} = {}".format(sayi1, sayi2, sonuc))
              input(d)
            except ZeroDivisionError:
              print("0'a bölünmez")
        elif sec == "Q":
            break
        elif sec == "q":
            break
        else:
            print("Lütfen Belirtilen Seçeneklerden Birini Seçiniz")
    except:
        print("Lütfen Rakam Giriniz")
