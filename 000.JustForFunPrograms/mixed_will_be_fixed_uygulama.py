#1. Program - Python shell de çalışan 5 temel uygulama denemesi :)
metin = """
(1) Toplama yap
(2) Faktoriyel bul
(3) Öğrenci listesi işlemleri
(4) İngilizce sözlük işlemleri
(5) Asker oluştur :)

-------------------------
Lütfen Seçiminizi yapınız
Çıkmak için (q) ya basınız
"""

d ="Devam etmek için bir tuşa basınız"

go_on_champion = "Devam etmek için bir tuşa basınız!"

ogrenci_liste = ["Ali Taş", "Mehmet İnce", "Ayşe Uzun"]

sozluk = {"book": "kitap", "window": "pencere", "cat": "kedi"}

class Asker(object):
    """ Asker sınıfı için gerekli açıklamaları burada yazacağız."""
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print("{} isimli asker başarıyla oluşturuldu.".format(self.name))
        self.attack()

    def attack(self):
        self.attack_power = self.power * 10
        print("Askerin normal gücü: ", self.power)
        print("Askerin saldırı gücü: ", self.attack_power)
        input(go_on_champion)



def topla(a, b): # Toplama yapan fonksiyon :)
    return a + b

def factorial(a): # Faktoriyel hesaplayan fonksiyon reqursive yalnız :)
    if a < 2:
        return 1
    else:
        return a * factorial(a - 1)



while True: # Q veya q seçilmediği sürece program çalışır.

    print(metin)
    choice = input("Yapmak istediğiniz işlemi seçiniz: ")

    if choice == "1":
        number1 = int(input("1. sayıyı giriniz: "))
        number2 = int(input("2. sayıyı giriniz: "))
        print("Sonuç: ", topla(number1, number2))
        input(go_on_champion)

    elif choice == "2":
        factorial_number = int(input("Faktoriyelini bulmak istediğiniz sayıyı giriniz: "))
        print("Sonuç: ", factorial(factorial_number))
        input(go_on_champion)

    elif choice == "3": # Tabi bunu nesne yönelimli yapsak çok daha şık olacak.
        liste_metin = """
        (1) Öğrenci listesini görüntüle
        (2) Yeni öğrenci ekle
        (3) Öğrenci ismi düzenle
        (4) Listeden öğrenci sil
        (5) Çıkış.
        """

        while True:
            print(liste_metin)
            liste_secim = input("Yapmak istediğiniz işlemi seçiniz: ")

            if liste_secim == "1":
                print(ogrenci_liste)

            elif liste_secim == "2":
                ogrenci_isim = input("Eklemek istediğiniz öğrenciyi giriniz: ")
                ogrenci_liste.append(ogrenci_isim)
                print("{} isimli öğrenci başarıyla eklendi.".format(ogrenci_isim))
                input(go_on_champion)

            elif liste_secim == "3":
                ogrenci_sirasi = int(input("Düzenlemek istediğiniz öğrenci sıra numarası giriniz: "))
                print(ogrenci_liste[ogrenci_sirasi], "isimli öğrenciyi düzenliyorsunuz")
                ogrenci_duzenleme = input("Yeni ismi giriniz: ")
                ogrenci_liste[ogrenci_sirasi] = ogrenci_duzenleme

            elif liste_secim == "4":
                ogrenci_sirasi = int(input("Silmek istediğiniz öğrenci sıra numarası giriniz: "))
                print(ogrenci_liste[ogrenci_sirasi], "isimli öğrenciyi sileceksiniz")
                ogrenci_sil = input("Silmek için 'E' iptal için 'H' ")
                if ogrenci_sil == "E":
                    print(ogrenci_liste[ogrenci_sirasi],"isimli öğrenci silindi")
                    del ogrenci_liste[ogrenci_sirasi]
                elif ogrenci_sil == "H":
                    print("İşlem iptal edildi")
                else:
                    print("Yanlış giriş yaptınız silme işlemi iptal edildi!")

                input(go_on_champion)

            elif liste_secim == "5":
                print("Liste menüsünden çıkıldı.")
                break
            else:
                print("Yanlış giriş.")


    elif choice == "4":
        sozluk_metin = """
        (1) Sözlüğü görüntüle
        (2) Yeni kelime ekle
        (3) Kelime ara
        (4) Çıkış.
        """

        while True:
            print(sozluk_metin)
            sozluk_secim = input("Yapmak istediğiniz işlemi seçiniz: ")

            if sozluk_secim == "1":
                print(sozluk)

            elif sozluk_secim == "2":
                sozluk_key = input("Eklemek istediğiniz kelimeyi giriniz: ")
                sozluk_value = input("Kelimenin anlamını giriniz: ")
                sozluk[sozluk_key] = sozluk_value

                print("{} kelimesi başarıyla eklendi.".format(sozluk[sozluk_key]))
                input(go_on_champion)

            elif sozluk_secim == "3":
                kelime = input("Aradığınız kelimeyi giriniz.")
                if kelime in sozluk:
                    print(kelime + ":" + sozluk[kelime])
                else:
                    print("Aradığınız kelime malesef büyük sözlüğümüzde yok!")

                input(go_on_champion)

            elif sozluk_secim == "4":
                print("Sözlükten çıkıldı.")
                break
            else:
                print("Yanlış giriş.")


    elif choice == "5":
        name = input("Askerinizin ismini giriniz: ")
        power = int(input("Askerinizin gücünü giriniz 0-100: "))
        soldier = Asker(name, power)


    elif choice == "Q" or choice == "q":
        print("Çıkılıyor....")
        break

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:")
