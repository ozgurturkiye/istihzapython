## Kümelerin Metotları

## intersection() - kesişim -

k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.intersection(k2))          ## output: {1, 3}
print(k1&k2)                        ## output: {1, 3}

#### ornek_
##
##tr = "şçöğüıŞÇÖĞÜİ"
##
##parola = input("Sisteme giriş için yen parola belirleyiniz.")
##
##if set(tr) & set(parola):
##    print("Türkçe karakter kullanmayın!!!")
##else:
##    print("Şifre kabul edildi :) ")


## intersection_update()

t1 = set([1, 2, 4, 6])
t2 = set([1, 3, 6, 8])
t1.intersection_update(t2)
print(t1)

## isdisjoint() - kesişim kümesinin boş olup olmadığının sonucunu verir

print(t1.isdisjoint(t2))        ## output: False

## issubset() - altkümesi olup olmadığının sonucunu verir
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(a.issubset(b))            ## output: True (a, b'nin alt kümesidir)

## issuperset() - üstkümesi olup olmadığının sonucunu verir
a = set([1, 2, 3])
b = set([0, 1, 2, 3, 4, 5])
print(b.issuperset(a))          ## output: True (b, a kümesini kapsar)
