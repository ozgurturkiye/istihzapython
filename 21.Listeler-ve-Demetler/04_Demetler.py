#Demetler listelere çok benzer, demetler değiştirilemez veri tipidir
#Demetler listelerden hızlı çalışır

#Demet tanımlamak için 4 yöntem

demet1 = ()
demet2 = tuple()
demet3 = ("ahmet", "mehmet", 23, 45)
demet4 = "ahmet", "mehmet", 23, 45     #Parantez kullanmadan da tanımlayabiliriz
demet5 = ("ozgur",)   #Sondaki virgüle dikkat onu koymazsak karakter dizisi olur.

#Başka ver tiplerini demete dönüştürme

tuple('abcdefg')                    #output: ('a', 'b', 'c', 'd', 'e', 'f', 'g')
tuple(["ahmet", "mehmet", 34, 45])  #output: ('ahmet', 'mehmet', 34, 45)

#Demetlerin Öğelerine Erişmek

demet = ('elma', 'armut', 'kiraz')
demet[0]   # 'elma' öğesine ulaşırız

#indeksleme ve dilimleme kuralları aynen demetler için de geçerlidir.
