#Listeler ile ilgili temel bilgiler
## 1:Listeler değiştirilebilir(mutable) veritipidir
## 2:Listeler farklı veri tiplerinin aynı anda barındırabilir
## 3:

##Liste Tanımlamak
liste0 = []
liste1 = list()
liste2 = ["öğe1", "öğe2", "öğe3"]

##Liste ve karakter dizisi karşılaştırma
kardiz = "İstanbul Büyükşehir Belediyesi"
print(kardiz[0])  #output: "İ"

liste = kardiz.split()
print(liste[0])  #output: "İstanbul"

#list() fonksiyonu

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_listesi = list(alfabe)
print(harf_listesi)

#range türünde bir veriyi list türünde bir veriye dönüştürme
print(list(range(10)))  #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Liste öğelerini yazdırmak
meyveler = ["elma", "armut", "çilek", "kiraz"]

for meyve in meyveler:
    print(meyve)

#Listeleri Birleştirmek
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller + yorumlanan_diller
print(programlama_dilleri)  #output: ['C', 'C++', 'C#', 'Java', 'Python', 'Perl', 'Ruby']
