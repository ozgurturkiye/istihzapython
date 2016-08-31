## Kümelerin Metotları

## metotları listele

##print(dir(set))
##
##for i in dir(set):
##    if '__' not in i:
##        print(i)

## add() metodu
kume = set(["elma", "armut", "kebap"])
kume.add("çilek")
print(kume)

## difference() metodu
k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])

print(k1.difference(k2))
print(k2.difference(k1))
print(k1-k2)

## difference_update() metodu
k1.difference_update(k2)
print(k1)
print(k2)

## discard() metodu (kümede olmayan bir elemanı silmek istersek hata vermez)
hayvanlar = set(["kedi", "köpek", "kuş", "at", "arslan"])
print(hayvanlar)
hayvanlar.discard("tavşan") 
hayvanlar.discard("kuş")
print(hayvanlar)

## remove() metodu (kümede olmayan bir elemanı silmek istersek hata verir)
hayvanlar.remove("tavşan")      ## output: KeyError: 'tavşan'
