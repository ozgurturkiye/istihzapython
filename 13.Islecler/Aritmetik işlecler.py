#Kaynak: http://belgeler.istihza.com/py3/islecler.html
#İngilizce’de operator adı verilen işleçler, 
#sağında ve solunda bulunan değerler arasında bir ilişki kuran işaretlerdir.

# +	toplama
# -	çıkarma
# *	çarpma
# /	bölme
# **	kuvvet
# %	modülüs
# //	taban bölme

print(45 + 33)       # output: 78
print("45" + "33")   # output: 4533
#print("45" + 33)    # output: TypeError
print(45 * 5)        # output: 225
print("45" * 5)      # output: 4545454545
#print("45" * "5")   # output: TypeError

print("istihza" + ".com")   # output: istihza.com
#print("istihza" - ".com")  # output: TypeError
print(25 / 4)               # output: 6.25 
print(543 % 10)             # output: 3 -> Bölme işleminin kalanını verir
print(5 // 2)               # output: 2 -> Tam sayı bölme
