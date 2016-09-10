## Özyinelemeli (Recursive) Fonksiyonlar

## Recursive Ornek_2

def sayac(sayi, sinir):
    print(sayi)
    if sayi == sinir:
        return "bitti"
    else:
        ##print(sayi)
        return sayac(sayi + 1, sinir)
        ##print(sayi)
    
print(sayac(0,10))
