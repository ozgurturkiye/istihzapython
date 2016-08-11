dilekçe = """
                                                    tarih: {}


T.C.
{} ÜNİVERSİTESİ
{} Fakültesi Dekanlığına


Fakülteniz {} Bölümü {} numaralı öğrencisiyim. Ekte sunduğum belgede
belirtilen mazeretim gereğince {} Eğitim-Öğretim Yılı  {}.
yarıyılında öğrenime ara izni (kayıt dondurma) istiyorum.

    Bilgilerinizi ve gereğini arz ederim.

        İmza

Ad              : {}
Soyad           : {}
T.C. Kimlik No. : {}
Adres           : {}
Tel.            : {}
Ekler           : {}
"""


tarih           = input("tarih: ")
üniversite      = input("üniversite adı: ")
fakülte         = input("fakülte adı: ")
bölüm           = input("bölüm adı: ")
öğrenci_no      = input("öğrenci no. :")
öğretim_yılı    = input("öğretim yılı: ")
yarıyıl         = input("yarıyıl: ")
ad              = input("öğrencinin adı: ")
soyad           = input("öğrencinin soyadı: ")
tc_kimlik_no    = input("TC Kimlik no. :")
adres           = input("adres: ")
tel             = input("telefon: ")
ekler           = input("ekler: ")

print(dilekçe.format(tarih, üniversite, fakülte, bölüm,
                     öğrenci_no, öğretim_yılı, yarıyıl,
                     ad, soyad, tc_kimlik_no,
                     adres, tel, ekler))
