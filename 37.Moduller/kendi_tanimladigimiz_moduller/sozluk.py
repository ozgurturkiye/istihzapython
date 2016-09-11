## Sözlük Modülü

sozluk = {"kitap": "book",
          "bilgisayar": "computer",
          "defter": "notebook"}

def ara(sozcuk):
    hata = "{} kelimesi sözlükte yok!!!"
    return sozluk.get(sozcuk, hata.format(sozcuk))  ## sözlüklerin get() metodu 1. argüman aranan kelime, 2. argüman kelime yoksa yapılacak iş

def ekle(sozcuk, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sozluk[sozcuk] = anlam
    print(mesaj.format(sozcuk))

def sil(sozcuk):
    try:
        sozluk.pop(sozcuk)
    except KeyError as err:
        print(err, "kelimesi bulunamadı!")
    else:
        print("{} kelimesi sözlükten silindi!".format(sozcuk))
