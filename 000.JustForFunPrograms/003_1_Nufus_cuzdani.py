## Nufus Cuzdani - Kullanıcıdan kimlik bilgilerini alarak;bu bilgileri
##                  nüfus cüzdanı şablonuna yerleştiren program
## Satır 35 için bilgilendirme -format metodunda 0. index değerini 24 karakter içinde sola yasla yapar
## Satır 37 için bilgilendirme -format metodunda 1. index değerini 24 karakter içinde sola yasla yapar

print("....Lütfen Kimlik Bilgilerinizi giriniz.....")
TC      = input("TC No.............:")
soyad   = input("Soyadınız.........:").upper()   #Girilen veriyi büyük harfe çeviriyor
ad      = input("Adınız............:").upper()
baba_ad = input("Baba Adınız.......:").upper()
ana_ad  = input("Anne Adınız.......:").upper()
d_yeri  = input("Doğum Yeriniz.....:").upper()
d_tarih = input("Doğum Tarihiniz...:").upper()

#Doğum yeri 10 karakterden uzunsa 10 karakterden sonrasını kırpıyoruz(sığmıyor :))
if len(d_yeri) > 10:
	d_yeri = d_yeri[:10] #0. karakterden 10. karaktere kadar al

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
* T.C. KİMLİK NO : {0:<24}*
*------------------------------------------*
* SOYADI         : {1:<24}*
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
