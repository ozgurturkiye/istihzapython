# Bu çalışmalar Sınıflar içine sözlükler gönderme üzerine yapılacak
# Gönderilen kwargs parametrelerine daha sonra ulaşabilmek için 
# self.kwargs = kwargs  yapmak gerekli.

class Soldier():
  def __init__(self, **kwargs):
    print(kwargs)
    self.sözlük = kwargs  #Bu kısım önemli, ki dışarıdan erişebilelim


dict_translate = {"book": "kitap", "pencil": "kalem"}

dict_number = {"one": 1, "two": 2, "tree": 3}

kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}


# Bir sözlük gönderme
a = Soldier(**dict_translate)

# İki sözlük gönderme
b = Soldier(**dict_translate, **dict_number)

# Bir isimli parametre iki sözlük  gönderme
c = Soldier(name="Özgür", **dict_translate, **dict_number)

# İç içe sözlük gönderme
d = Soldier(**kişiler)
print(d.sözlük)
print(d.sözlük["Ahmet Özkoparan"])
print(d.sözlük["Ahmet Özkoparan"]["Memleket"])

