## Kümeler

## Tanımlama

bos_kume = set()
print(type(bos_kume))               ## output: <class 'set'>

kume = {'Python', 'C++', 'Ruby', 'PHP'}
print(kume, type(kume))             ## output: {'Python', 'C++', 'Ruby', 'PHP'}

liste = ["elma","armut","üzüm"]     ## Listeden küme oluşturmak
kume_1 = set(liste)
print("KÜME 1..:", kume_1)          ## output: {'armut','üzüm','elma'}


demet = ("elma","armut","üzüm")     ## Demetden küme oluşturmak
kume_2 = set(demet)
print("KÜME 2..:", kume_2)          ## output: {'armut','üzüm','elma'}


kardiz = "elma, armut, üzüm"        ## Karakter dizisinden küme oluşturmak
kume_3 = set(kardiz)
print("KÜME 3..:", kume_3)          ## output: {'a', 'u', 't', 'z', ' ', 'm', 'l', 'r', 'ü', ',', 'e'}
                                    ## DİKKAT: Üstteki satırda her elemandan 1 tane var

sozluk = {"elma": "meyve",          ## Sözlükten küme oluşturmak
          "armut": "meyve",
          "üzüm": "meyve"}         
kume_4 = set(sozluk)
print("KÜME 4..:", kume_4)          ## output: {'armut','üzüm','elma'} DİKKAT: Sadece anahtarları kümeye attı. değerler?

## Hem anahtar, hem de değerleri kümeye atmak için

liste_2 = [(anahtar, deger) for anahtar, deger in sozluk.items()]
kume_5 = set(liste_2)
print("KÜME 5..:", kume_5)          ## output: {('armut', 'meyve'), ('üzüm', 'meyve'), ('elma', 'meyve')}
