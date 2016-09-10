## Özyinelemeli (Recursive) Fonksiyonlar

## Recursive Ornek_4

def topla(sayilar):
    if len(sayilar) < 1:
        return 0
    else:
        ilk, son = sayilar[0], sayilar[1:]
        return ilk + topla(son)

sayi_listesi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(topla(sayi_listesi))
