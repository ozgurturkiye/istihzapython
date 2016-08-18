#Liste üreteçleri - (List Comprehensions)
#Aşağıdaki 0-100 arası liste oluşturmak için 3 yöntem
liste = [i for i in range(100)]

liste1 = []

for i in range(100):
    liste1 += [i]

liste2 = list(range(100))

print(liste)
print(liste1)
print(liste2)

#0-100 arası çift sayılardan oluşan liste oluşturmak
liste = [i for i in range(100) if i % 2 == 0]
print(liste)

#Buraya da 0-100 arası 10 ar 10 ar artan liste oluşturalım. Tabi üreteçler ile
