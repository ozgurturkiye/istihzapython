# Kendi Tanımladığımız Modüller
## Modüllerin Tanımlanması

> Hatırlarsanız bu bölümün başında, ‘modül nedir?’ sorusuna şu cevabı vermiştik:

> Bazı işlevleri kolaylıkla yerine getirmemizi sağlayan birtakım fonksiyonları ve nitelikleri içinde barındıran araçlar...

Esasında Python’daki modülleri şöyle de tanımlayabiliriz:

> Diyelim ki bir program yazıyorsunuz. Yazdığınız bu programın içinde karakter dizileri, sayılar, değişkenler, listeler, demetler, sözlükler ve fonksiyonlar var. Programınız da .py uzantılı bir metin dosyası içinde yer alıyor. İşte bütün bu öğeleri ve veri tiplerini içeren .py uzantılı dosyaya ‘modül’ adı verilir. Yani şimdiye kadar yazdığınız ve yazacağınız bütün Python programları aynı zamanda birer modül adayıdır.

Gelin isterseniz yukarıdaki bu tanımın doğruluğunu test edelim.
```python
import os
os.__file__   #output: '/usr/lib/python3.5/os.py'
```
İşte buradan aldığımız çıktı bize os modülünün kaynak dosyasının nerede olduğunu gösteriyor. Dosyayı açtığınızda, gerçekten de bu modülün aslında sıradan bir Python programı olduğunu göreceksiniz.
## Kendi modülümüzü tanımlayalım
> sözlük.py adlı programımızın içeriği şöyle olsun:
```python
sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}
def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))
```
> Şimdi, eğer bu sözlük.py dosyasını, mesela masaüstüne kaydettiyseniz, masaüstünün bulunduğu konumda bir komut satırı açın ve Python’ın etkileşimli kabuğunu başlatın.

```python
import sözlük
sözlük.__file__   #output: Dosya neredeyse onu söyle :)
sözlük.ara("bilgisayar")   #output: computer
```
# Modüllerin Yolu
> Kütüphane modüllerini her yerden içe aktarabiliyoruz.Ama kendi yazdığımız modülleri içe aktarabilmemiz için, bu modüllerin o anda içinde bulunduğumuz dizin altında yer alması gerekiyor. Kütüphane modülleri gibi kendi modüllerimizi her yerden içe aktarabilmek için iki seçeneğimiz var: Birincisi, modülün yolunu sys.path listesine ekleyebiliriz. İkincisi, modülümüzü sys.path içinde görünen dizinlerden birine kopyalayabilir veya taşıyabiliriz.

1. 
```python
import sys
sys.path
sys.path.append(r'/home/istihza/programlar')   #Dosyamızın olduğu dizini listeye ekliyoruz.
```
Gördüğünüz gibi, sys.path komutunun çıktısı aslında basit bir listeden başka bir şey değildir. 

2. Kendi yazdığımız bir modülü her yerden içe aktarabilmenin ikinci yönteminin, ilgili modül dosyasını sys.path çıktısında görünen dizinlerden herhangi birine kopyalamak. Yaygın olarak tercih edilen konum, Python kurulum dizini içindeki site-packages adlı dizindir.

> Python, içe aktarmak istediğimiz bir modülü bulabilmek için dizinleri ararken sys.path listesindeki dizin adlarını soldan sağa doğru okur. Modül dosyasını bulduğu anda da arama işlemini sona erdirir ve modülü içe aktarır. Eğer siz içe aktarma sırasında bir dizine öncelik vermek isterseniz o dizini append() metoduyla sys.path listesinin sonuna eklemek yerine, insert() metoduyla listenin en başına ekleyebilirsiniz:

```python
sys.path.insert(0, r'dizin/adı')
```
# Modüllerde Değişiklik Yapmak
> Tıpkı kütüphane modüllerini işlerken yaptığımız gibi, dir() fonksiyonundan yararlanarak, içe aktardığımız bu modül içindeki kullanılabilir fonksiyon ve nitelikleri görebilirsiniz:
```python
dir(sözlük)
```
Bu komut bize şöyle bir çıktı verir:

```python
['__builtins__', '__cached__', '__doc__',
'__file__', '__loader__', '__name__',
'__package__', '__spec__', 'ara', 'sözlük']
```
> kendi yazdığımız sözlük modülü içinde de ara() adlı bir fonksiyon ve sözlük adlı bir nitelik var.
```python
sözlük.sözlük
sözlük.ara('kitap')
```
## Modülde değişiklik yapmak
Modülde yapılan değişikliklerin etkileşimli kabukta etkinleşebilmesi için o modülü yeniden yüklememiz lazım. Bunu iki şekilde yapabiliriz:

1. Birincisi, etkileşimli kabuğu kapatıp yeniden açtıktan sonra import sözlük komutuyla sözlük modülünü tekrar içe aktarabiliriz.

2. İkincisi, importlib adlı bir kütüphane modülünden yararlanarak kendi modülümüzün tekrar yüklenmesini sağlayabiliriz. Bu modülü şöyle kullanıyoruz:
```python
import importlib
importlib.reload(sözlük)
```
> Dediğimiz gibi, modülden silinen öğeler, reload() ile yeniden yüklendikten sonra dahi kullanılır durumda kalmaya devam eder. Ama eğer modül içinde varolan bir öğe üzerinde değişiklik yaparsanız o değişiklik, reload() sonrası modülün görünümüne yansıyacaktır. Yani mesela, modülde halihazırda varolan sil() fonksiyonu üzerinde bir değişiklik yaparsanız, bu değişiklik reload() ile yeniden yükleme sonrasında etkileşimli kabuğa yansıyacaktır.

# Üçüncü Şahıs Modülleri
> Bu modülleri kullanabilmek için, öncelikle bunları modül geliştiricisinin koyduğu yerden bilgisayarımıza indirmemiz gerekir.

> Eğer bir modül https://pypi.python.org/pypi adresinde ise, bu modülü sistem komut satırında şu şekilde kurabilirsiniz:
```python
#Örnek --> pip3 install modül_adı
pip3 install django
```
> Eğer bir üçüncü şahıs modülünü https://pypi.python.org/pypi adresinden değil de başka bir kaynaktan indiriyorsanız, kurulum için birkaç farklı seçenek olabilir. Eğer indireceğiniz dosya .tar.gz veya .zip gibi sıkıştırılmış bir klasör olarak iniyorsa öncelikle bu sıkıştırılmış klasörü açın. Eğer klasör içeriğinde setup.py adlı bir dosya görürseniz bu dosyanın bulunduğu konumda bir komut satırı açın ve şu komutu verin:

`sudo python3 setup.py install`

# __all__ Listesi
> Okuyunuz: http://belgeler.istihza.com/py3/moduller.html#all-listesi

# Modüllerin Özel Nitelikleri
> Python’da bütün modüllerin ortak olarak sahip olduğu bazı nitelikler vardır. Bunlar: 

`{'__doc__', '__package__', '__loader__', '__name__', '__spec__'}`

## __doc__ Niteliği
> Teknik dilde, üç tırnak içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi (documentation string) adı verilir. Modüllerin __doc__ niteliğini kullanarak, bir modül dosyasının en başında bulunan belgelendirme dizilerine erişebiliriz.

```python
import os
os.__doc__    #output: Uzun bir tanıtım
```
## __name__ Niteliği
1. Mesela masaüstünde deneme.py adlı bir dosya oluşturup içine sadece şunu yazalım:
`print(__name__)`

2. Şimdi önce bu dosyayı bağımsız bir program olarak çalıştıralım:

`python deneme.py`
Programımızı bu şekilde çalıştırdığımızda alacağımız çıktı şu olacaktır: `__main__`

Demek ki __name__ niteliğinin değeri "__main__" imiş...

3. Şimdi de deneme.py dosyasının bulunduğu konumda Python’ın etkileşimli kabuğunu çalıştıralım ve şu komut yardımıyla bu dosyayı bir modül olarak içe aktaralım:

`import deneme`
Bu defa şu çıktıyı aldık: `deneme`

Gördüğünüz gibi, `__name__` niteliğinin değeri bu kez de modül dosyasının adı oldu.

İşte bu özellikten yararlanarak, yazdığınız programların bağımsız çalıştırılırken ayrı, modül olarak içe aktarılırken ayrı davranmasını sağlayabilirsiniz.

## __loader__ Niteliği
> Python’da içe aktarılan bütün modüllerin __loader__ adlı bir niteliği bulunur. Bu nitelik, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli bilgiler veren birtakım araçlar sunar:

## __spec__ Niteliği
> __spec__ niteliği de bize modüller hakkında çeşitli bilgiler sunan birtakım araçları içinde barındırır. Mesela bir modülün ad ve konum bilgilerine ulaşmak için bu niteliği kullanabiliriz:

## __package__ Niteliği
> Henüz bu niteliğin ne olduğunu anlayacak bilgiye sahip olmadığımız için, bu niteliğin incelemesini ‘Paketler’ konusunu işlediğimiz bölüme bırakıyoruz.
