#1. Program - Python shell de çalışan metin tabanlı uçuş kontrol programı :)
metin = """
(1) Uçuş Saati Gir
(2) Mesai Saati Gir
(3) İstatistikleri Göster
-------------------------
Lütfen Seçiminizi yapınız
Çıkmak için (q) ya basınız
"""
#devam edecek :)
d ="Devam etmek için bir tuşa basınız"
while True:
    try:
        print(metin)
        sec = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
        
        def ucus_gir():
            name = input("Kullanıcı adı: ")
            start_date = int(input("Uçuş başlangıç tarihi: "))
            finish_date = int(input("Uçuş bitiş tarihi: "))
            return name, start_date, finish_date
        
        def mesai_gir():
            name = input("Kullanıcı adı: ")
            start_date = int(input("Mesai başlangıç tarihi: "))
            finish_date = int(input("Mesai bitiş tarihi: "))
            return name, start_date, finish_date    
          
        def istatistikleri_göster():
            istatistik_name = input("Kullanıcı adı: ")
            return istatistik_name
          
        if sec == "1":
            user_name, flight_start_date, flight_finish_date = ucus_gir()
            
            #Bu kısımda artık veriler nasıl kaydedilecekse o yapılacak
            #a. txt dosyası şeklinde b.sqlite3 şeklinde veya başka türlü
            print("Kullaıcı: {} \nUçuş başlangıç: {} \nUçuş bitiş: {}".format(user_name, flight_start_date, flight_finish_date))
            input(d)
        elif sec == "2":
            user_name, work_start_date, work_finish_date = mesai_gir()
            #Bu kısımda artık veriler nasıl kaydedilecekse o yapılacak
            print("Kullaıcı: {} \nUçuş başlangıç: {} \nUçuş bitiş: {}".format(user_name, work_start_date, work_finish_date))
            input(d)
        elif sec == "3":
            name = istatistikleri_göster()
            print("Kullaıcı_adı: {}".format(name))
            print("Burada istatistik bilgileri gösterilecek")
            input(d)
          
        elif sec == "Q":
            break
        elif sec == "q":
            break
        else:
            print("Lütfen Belirtilen Seçeneklerden Birini Seçiniz")
    except:
          print("Lütfen Rakam Giriniz")
