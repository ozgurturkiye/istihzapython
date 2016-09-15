r"""

    KONU - Alternatif İnşacılar

    - Bu liste, her bir kitap için, sırasıyla o kitabın
      * ISBN numarasını,
      * yazarını,
      * ismini
      * yayınevini
      gösteren birer demetten oluşuyor.
      Amacımız, bu listeden çeşitli olcutlere göre
      sorgulama yapabilen bir program yazmak.
      Yazdığımız program; isbn, isim, eser ve yayınevi
      olcutlerine göre bu listeden veri alabilmemizi sağlayacak.

"""

## Version - 1

liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(olcut=None, deger=None):
    for li in liste:
        if not olcut and not deger:
            print(*li, sep=', ')

        elif olcut == 'isbn':
            if deger == li[0]:
                print(*li, sep=', ')

        elif olcut == 'yazar':
            if deger == li[1]:
                print(*li, sep=', ')

        elif olcut == 'eser':
            if deger == li[2]:
                print(*li, sep=', ')

        elif olcut == 'yayınevi':
            if deger == li[3]:
                print(*li, sep=', ')

## Version - 2

def sorgula_2(olcut=None, deger=None):
    kitap_sozlugu = {'isbn'     : [li for li in liste if li[0] == deger],
                     'yazar'    : [li for li in liste if li[1] == deger],
                     'eser'     : [li for li in liste if li[2] == deger],
                     'yayınevi' : [li for li in liste if li[3] == deger]}

    for oge in kitap_sozlugu.get(olcut, deger):
        print(*oge, sep = ', ')

## Version - 3 - Sorgu sınıfı oluşturarak

class Sorgu():
    def __init__(self, deger=None, sira=None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

        if not deger and not sira:
            l = self.liste
        else:
            l = [li for li in self.liste if deger == li[sira]]

        for i in l:
            print(*i, sep = ', ')

    @classmethod
    def isbnden(cls, isbn):
        cls(isbn, 0)

    @classmethod
    def yazardan(cls, yazar):
        cls(yazar, 1)

    @classmethod
    def eserden(cls, eser):
        cls(eser, 2)

    @classmethod
    def yayınevinden(cls, yayınevi):
        cls(yayınevi, 3)
