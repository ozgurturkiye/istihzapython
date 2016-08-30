## Sözlüklerin Metotları

## values() metodu - Sözlükteki değerleri verir.

sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}

print(sozluk.values())            ## output: dict_values(['1','0','2','3'])

liste = list(sozluk.values())     ## output: ['1','0','2','3']
print(liste)

demet = tuple(sozluk.values())    ## output: ('1','0','2','3')
print(demet)

kardiz = "".join([str (i) for i in sozluk.values()]) ## output: 1023
print(kardiz)
