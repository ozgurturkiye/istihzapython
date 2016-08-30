## Sözlüklerin Metotları

## pop() metodu - sözlük elemanını siler.

hava_durumu_sozluk = {"İstanbul": "yağmurlu", "Adana": "güneşli", "İzmir": "açık"}

hava_durumu_sozluk.pop("Adana")  ## Sözlükten Adana anahtarını ve değerini siler

print(hava_durumu_sozluk)


## popitem() metodu - rastgele bir sözlük elemanını siler.

hava_durumu_sozluk.popitem()

print(hava_durumu_sozluk)
