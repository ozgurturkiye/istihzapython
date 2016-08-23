#Dosya Okumak
#2 yöntemde aynı işi yapar "r" ye gerek yok
fihrist = open("fihrist.txt", "r")
fihrist = open("fihrist.txt")

# read(), readline() ve readlines() adlı üç farklı metottan yararlanacağız.
# read() Tüm içeriği karakter dizisi olarak verir
# readline() İçeriği satır satır karakter dizisi olarak verir
# readlines() İçeriği her satır bir öğe olacak şekilde liste olarak verir

#Örnek fihrist.txt dosyası içeriği 
#Not: Bu metotlarından herhangi biri ile dosyayı okuduğunuzda imleç başa dönmez.
"""
Ahmet Özbudak : 0533 123 23 34
Mehmet Sülün  : 0532 212 22 22
Sami Sam      : 0542 333 34 34
"""

fihrist = open("fihrist.txt")
print(fihrist.read())
#output: Tüm içerik aynen gelir

print(fihrist.readline())
#output: Ahmet Özbudak : 0533 123 23 34

print(fihrist.readlines()) 
#output:['Ahmet Özbudak : 0533 123 23 34\n', 'Mehmet Sülün  : 0532 212 22 22\n', 'Sami Sam      : 0542 333 34 34']

#Konu ayrıca detaylıca okunmalı
