#Kaynak: http://belgeler.istihza.com/py3/listelerin_ve_demetlerin_metotlari.html

#append() Bir listeye öğe eklemek için kullanıyoruz.
#append() metodu yalnızca tek parametre alır.
##Yani bu metodu kullanarak bir listeye birden fazla öğe ekleyemezsiniz: 
liste = ["elma", "armut", "çilek"]
liste.append("erik")  #result: ['elma', 'armut', 'çilek', 'erik'] 

#extend() listeleri ‘genişletir’.
li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1. extend(li2)

print(li1)  #output: [1, 3, 4, 10, 11, 12]
#Eğer append(li2) metodunu kullansaydık 
## output: [1, 3, 4, [10, 11, 12]] olurdu.(istenmeyen sonuç)

#insert()  öğeleri listenin istediğimiz bir konumuna yerleştirir.
liste = ["elma", "armut", "çilek"]
liste.insert(0, "erik")   #result: ['erik', 'elma', 'armut', 'çilek']

#remove() Bu metot listeden öğe silmemizi sağlar.
liste.remove("elma")

#reverse() metodu liste öğelerini ters çevirmek
meyveler = ["elma", "armut", "çilek", "kiraz"]
meyveler.reverse() #öğeleri sıralamasını ters çevirir

#reversed() Fonksiyonu nu da kullanabilirsin
print(*reversed(meyveler))        #1. yöntem
print(list(reversed(meyveler)))   #2. yöntem
for i in reversed(meyveler):      #3. yöntem
	print(i)

#pop()
##Tıpkı remove() metodu gibi, bu metot da bir listeden öğe silmemizi sağlar:
##Bu metot parametresiz olarak kullanıldığında listenin son öğesini listeden atar.
liste = ["elma", "armut", "çilek"]
#liste.pop()   #son öğe atılır
#liste.pop(0)  #0. öğe atılır

#sort() listenin öğelerini belli bir ölçüte göre sıraya dizmemizi sağlar.

#index() bir liste öğesinin liste içindeki konumunu söyler
liste.index("elma")

#count() bir öğenin o veri tipi içinde kaç kez geçtiğini söyler:
liste.count("elma")

#copy() listeleri, birbirlerini etkilemeyecek şekilde kopyalamak için
liste_kopya = liste.copy()

#clear() bir listenin içeriğini silmektir.






