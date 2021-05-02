+r"""008_binary_kodlama_sistemi - Program hakkında açıklamalar -
 +
 +Türk alfabesindeki (sadece büyük harf) harfleri ve boşluk karakterini
 +basit bir kodlama sistemine göre binary karşılıklarını yazan kodlar. 
 +
 +Onlu sayma sistemindeki sayıların ikili sayma sistemindeki
 +karşılıklarını yazdırmaktan başka birşey yapmıyoruz aslında :)
 +
 +Geliştirmek için hazır bir sözlük kullanmak yerine anlık olarak
 +onlu sistemdeki sayıyı; ikili sistemdeki sayıya çevirilebilir.
 +
 +"""
 +
 +sayBitSoz = {" ": "00000000",   ## Boşluk
 +             "A": "00000001",   ##  1
 +             "B": "00000010",   ##  2
 +             "C": "00000011",   ##  3
 +             "Ç": "00000100",   ##  4
 +             "D": "00000101",   ##  5
 +             "E": "00000110",   ##  6
 +             "F": "00000111",   ##  7
 +             "G": "00001000",   ##  8
 +             "Ğ": "00001001",   ##  9
 +             "H": "00001010",   ## 10
 +             "I": "00001011",   ## 11
 +             "İ": "00001100",   ## 12
 +             "J": "00001101",   ## 13
 +             "K": "00001110",   ## 14
 +             "L": "00001111",   ## 15
 +             "M": "00010000",   ## 16
 +             "N": "00010001",   ## 17
 +             "O": "00010010",   ## 18
 +             "Ö": "00010011",   ## 19
 +             "P": "00010100",   ## 20
 +             "R": "00010101",   ## 21
 +             "S": "00010110",   ## 22
 +             "Ş": "00010111",   ## 23
 +             "T": "00011000",   ## 24
 +             "U": "00011001",   ## 25
 +             "Ü": "00011010",   ## 26
 +             "V": "00011011",   ## 27
 +             "Y": "00011100",   ## 28
 +             "Z": "00011101"    ## 29
 +             
 +    }
 +
 +kardiz = input("Ad Soyad...:")
 +
 +for karakter in kardiz:
 +    print(karakter, sayBitSoz[karakter])
