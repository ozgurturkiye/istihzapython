## Sözlüklerin Metotları

## fromkeys() metodu - yeni bir sözlük oluşturur.

hava_durumu_demet = "İstanbul", "Adana", "İzmir"

hava_durumu_sozluk = dict.fromkeys(hava_durumu_demet,"güneşli")

print(hava_durumu_sozluk)

## output: {'İstanbul': 'güneşli', 'Adana': 'güneşli', 'İzmir': 'güneşli'}
