## Sözlük Modülüyle Çalış - Örnekler

import sozluk   ## sozluk.py modülünü içe aktarıyoruz

print("Sözlükte bulunan kelimeler ve anlamları aşağıda listelenmiştir!!!")
print(sozluk.sozluk)
print("Sözlük modülünün fonksiyonları aşağıda listelenmiştir!!!!")
print(dir(sozluk))

menu = """....Yapmak istediğiniz işlemi seçiniz....
..........Sözcük aramak için (1).........
..........Sözcük eklemek için (2)........
..........Sözcük silmek için (3).........
...Sözlük'teki kelimeleri listele (4)....
...............ÇIKIŞ için (0)............"""

print(menu)

dongu = 1

while dongu == 1:
    durum = input("Yapmak istediğiniz işlemin numarasını giriniz....")
    if durum == "0":
        print("Çıkılıyor")
        dongu = 0
    elif durum == "1":
        key   = input("Anlamını öğrenmek istediğiniz kelimeyi giriniz...:")
        print(sozluk.ara(key))
    elif durum == "2":
        key   = input("Eklemek istediğiniz kelimeyi giriniz...:")
        value = input("Eklemek istediğiniz kelimenin anlamını giriniz...:")
        print(sozluk.ekle(key, value))
    elif durum == "3":
        key   = input("Silmek istediğiniz kelimeyi giriniz...:")
        print(sozluk.sil(key))
    elif durum == "4":
        print(sozluk.sozluk)
