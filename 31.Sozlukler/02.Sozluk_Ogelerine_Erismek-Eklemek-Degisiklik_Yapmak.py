## Sozlukler - Öğelerine erişmek

## Öğelerine erişmek

sozluk = {"kitap": "book",
          "bilgisayar": "computer",
          "programlama": "programming",
          "dil": "language",
          "defter": "notebook"}
print(sozluk["kitap"])              ## output: book
print("1--------")

## hepsini yazdıralım

for i in sozluk:
    print(sozluk[i])                ## output: hepsini alt alta yazar (aynı sırayla yazmayabilir)
print("2--------")

## Öğe eklemek

sozluk["kalem"] = "pen"

for i in sozluk:
    print(sozluk[i])
print("3--------")

## Öğe üzerinde değişiklik yapmak

sozluk["kalem"] = "pencil"

for i in sozluk:
    print(sozluk[i])
