## index()


#### index() - ornek_1
##kardiz = "Python"
##print(kardiz.index("P"))    ## output: 0

#### print(kardiz.index("p")) ## Büyük-Küçük harf duyarlı


#### index() - ornek_2
##kardiz = "adana"
##for i in range(len(kardiz)):
##    print(kardiz.index("a",i))
    
## output:
## 0
## 2
## 2
## 4
## 4


#### index() - ornek_3 (Var bir sıkıntısı hata verebiliyor)
kardiz = input("Metin girin: ")
aranacak = input("Aradığınız harf: ")

for i in range(len(kardiz)):
    print("i'nin değeri: ", i)
    if i == kardiz.index(aranacak, i):
        print("%s. sırada 1 adet %s harfi bulunuyor" %(i, aranacak))
    else:
        print("%s. sırada %s harfi bulunmuyor" %(i, aranacak))
