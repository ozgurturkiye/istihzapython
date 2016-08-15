## Nufus Cuzdani - Kullanıcıdan kimlik bilgilerini alarak;bu bilgileri
##                  nüfus cüzdanı şablonuna yerleştiren program

print("....Lütfen Kimlik Bilgilerinizi giriniz.....")
TC      = input("TC No.............:")
soyad   = input("Soyadınız.........:").upper()   #Girilen veriyi büyük harfe çeviriyor
ad      = input("Adınız............:").upper()
baba_ad = input("Baba Adınız.......:").upper()
ana_ad  = input("Anne Adınız.......:").upper()
d_yeri  = input("Doğum Yeriniz.....:").upper()
d_tarih = input("Doğum Tarihiniz...:").upper()

nufus_cuzdani_sablon = """
********************************************
********************************************
*                     |                    *
*                     |  ||||||||||||||||  *
*                     |  |              |  *
*                     |  |              |  *
*                     |  |              |  *
*                     |  |    RESİM     |  *
*                     |  |              |  *
*                     |  |              |  *
*                     |  |              |  *
*                     |  |              |  *
*                     |  ||||||||||||||||  *
*                     |                    *
*------------------------------------------*
* T.C. KİMLİK NO : {0:<24}*   #format metodunda 0. index değerini 24 karakter içinde sola yasla yapar
*------------------------------------------*
* SOYADI         : {1:<24}*   #format metodunda 1. index değerini 24 karakter içinde sola yasla yapar
*------------------------------------------*
* ADI            : {2:<24}*
*------------------------------------------*
* BABA ADI       : {3:<24}*
*------------------------------------------*
* ANA ADI        : {4:<24}*
*------------------------------------------*
* D.Y.:{5:<10}|D.T.:{6:<20}*
*------------------------------------------*
********************************************
"""

print(nufus_cuzdani_sablon.format(TC, soyad, ad, baba_ad, ana_ad, d_yeri, d_tarih))
