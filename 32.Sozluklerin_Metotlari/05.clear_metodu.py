## Sözlüklerin Metotları

## clear() metodu - sözlüğü boşaltır

sozluk = {"a": "1", "b": "2"}

sozluk.clear()
print(sozluk)           ## output: {}

del sozluk
print(sozluk)           ## output: NameError: name 'sozluk' is not defined
