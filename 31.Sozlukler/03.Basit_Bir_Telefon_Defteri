## Sozlukler - Basit bir telefon defteri

#### V.1
##telefon_defteri = {"ahmet öz" : "0532 532 32 32",
##                   "mehmet su": "0543 543 42 42",
##                   "seda naz" : "0533 533 33 33",
##                   "eda ala" : "0212 212 12 12"}
##
##sorgu = input("Telefon numarasını öğrenmek istediğiniz kişiyi giriniz...:")
##
##cevap = "{} adlı kişinin telefon numarası:{}"
##
##print(cevap.format(sorgu, telefon_defteri[sorgu]))


## hatayı önlemek için
## V.2

telefon_defteri = {"ahmet öz" : "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz" : "0533 533 33 33",
                   "eda ala"  : "0212 212 12 12"}

sorgu = input("Telefon numarasını öğrenmek istediğiniz kişiyi giriniz...:")
sorgu = sorgu.lower()

if sorgu in telefon_defteri:
    cevap = "{} adlı kişinin telefon numarası:{}"
    print(cevap.format(sorgu, telefon_defteri[sorgu]))
else:
    olumsuz_cevap = "{} adlı kişinin telefon numarası kayıtlı değildir"
    print(olumsuz_cevap.format(sorgu))
