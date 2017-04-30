#class base güzel örnek hem veritabanı hem dosya işlemleri var

import sqlite3
import time

class Animal():

    def __init__(self):
        #Do something when instance created
        print("İşlem başlatıldı")

    @classmethod
    def show_record(cls):
        print("Kayit listesi.....")
        #Show record from the file
        with open("animals.txt", "r") as f:
            print(f.read())

    @classmethod
    def show_record_number(cls):
        print("Toplam kayit sayisi:")
        #Show number of record from file
        with open("animals.txt", "r") as f:
            print(len(f.readlines()))

    def add_record(self, name, gender):
        #Open and connect database
        with sqlite3.connect("ciftligim.sqlite") as vt:
            im = vt.cursor()

            animal_id = "---"
            registered = str(time.ctime())
            #We created a tuple to add multiple data
            all_data = (animal_id, name, gender, registered)
            im.execute("""INSERT INTO animals VALUES (?, ?, ?, ?)""", all_data)

            #Commitsiz olmaz :)
            vt.commit()

    def del_record(self, name):
        try:
            #Bu kısım silme işlemi yapılacak
            print(name)
            with open("animals.txt", "r") as f:
                data = f.readlines()

            data_clean = []
            for i in data:
                data_clean.append(i[:-1]) #Sondaki "\n" karakterini siliyoruz ve kayıt
            print("Sondaki ters slaşlar Temizlenmiş hali....")
            print(data_clean)
            #print(deleted_data)
            #try exept kullanmak gerekli hata için
            data_clean.remove(name)
            print("Silinmiş hali......")
            print(data_clean)
            #Burada her satırın sonuna \n eklenecek sonra dosayaya yazılacak
            for i in range(len(data_clean)):
                data_clean[i] = data_clean[i] + "\n"
            print("Dosyaya yazılmadan önceki son hali.......")
            print(data_clean)
            #Write the list to the file
            with open("animals.txt", "w") as f:
                f.writelines(data_clean)

        except ValueError:
            print("Kayıt SILINEMEDİ, Lütfen listeden eleman girin!")

#Make your choice !
intro = """
Seciminizi yapiniz!
1-Kayit Ekle(1)
2-Kayitlari Goster(2)
3-Kayit Sayisini Goster(3)
4-Kayit Sil(4)
Q-Çıkış (Q veya q)
"""
print(intro)

while True:
    answer = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if answer == "q":
        print("çıkılıyor...")
        break

    elif answer == "1":
        name       = input("Eklemek istediğiniz hayvanın adını giriniz: ")
        gender     = input("Hayvanın cinsiyetini giriniz: ")
        obj1 = Animal()
        obj1.add_record(name, gender)

    elif answer == "2":
        Animal.show_record()

    elif answer == "3":
        Animal.show_record_number()

    elif answer == "4":
        name = input("Silmek istediğiniz hayvanın adını giriniz: ")
        obj2 = Animal()
        obj2.del_record(name)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", intro)
