#Python programlama dilinde koşullu durumları belirtmek için üç adet deyimden yararlanıyoruz:
#if
#elif
#else

#İşleç Anlamı
# > büyüktür
# < küçüktür
# >= büyük eşittir
# <= küçük eşittir
# == eşittir
# != eşit değildir


yas = int(input("Terchi yapabilmek için yaşınızı giriniz"))

if yas > 18:
	tercih = input("Partiye gelmek istiyor musunuz! Evet - Hayır - Kararsız \n")
	
	if tercih == "Evet":
		print("Hobaa yarın partide görüşürüz!")
	elif tercih == "Hayır":
		print("Büyük eğlenceyi kaçırdın")
	elif tercih == "Kararsız":
		tercih2 = input("Yarın işiniz var mı? Evet - Hayır")
		if tercih2 == "Evet":
			print("Bir daha ki sefere görüşmek üzere")
		else:
			print("Gel yarın bea ne olcak!")
	else:
		print("Evet - Hayır - Kararsız seçeneklerinden birini seçiniz")
else:
	print("Üzgünüm yaşınız tutmuyor")


