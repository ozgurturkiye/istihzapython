# Python'da ifade ve deyim farkı
Python’daki iki önemli kavramı açıklığa kavuşturmamız gerekiyor: Bu kavramlar şunlar:

1. ifade
2. deyim

### Öncelikle ‘ifade’ kavramından başlayalım.

> İngilizcede *expression* denen ‘ifadeler’, bir değer üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, işleçler, öteki veri tipleri, liste üreteçleri, sözlük üreteçleri, küme üreteçleri, fonksiyonlar hep birer ifadedir. Örneğin:

```python
>>> 5

>>> 23 + 4

>>> [i for i in range(10)]

>>> len([1, 2, 3])
```
### Şimdi ‘deyim’ kavramına bir bakalım.

> İngilizcede *statement* olarak adlandırılan ‘deyimler’ ise ifadeleri de kapsayan daha geniş bir kavramdır. Buna göre bütün ifadeler aynı zamanda birer deyimdir. Daha doğrusu, ifadelerin bir araya gelmesi ile deyimler oluşturulabilir.

> Deyimlere birkaç örnek verelim:
```python
>>> a = 5

>>> if a:
...     print(a)

>>> for i in range(10):
...     print(i)
```
> Python programlama dilinde deyimlerle ifadeleri ayırt etmenin kolay bir yolu da eval() fonksiyonundan yararlanmaktır. Eğer deyim mi yoksa ifade mi olduğundan emin olamadığınız bir şeyi eval() fonksiyonuna parametre olarak verdiğinizde hata almıyorsanız o parametre bir ifadedir. Eğer hata alıyorsanız o parametre bir deyimdir. Çünkü eval() fonksiyonuna parametre olarak yalnızca ifadeler verilebilir.
Birkaç örnek verelim:
```python
eval('a = 5')   #output: SyntaxError: invalid syntax --> Çünkü a = 5 kodu bir deyimdir. Unutmayın, Python’da bütün değer atama işlemleri birer deyimdir.
eval('5 + 25')  #output: 30   --> Bildiğiniz gibi, 5 + 25 kodu bir ifadedir. Çalışır :)
```
