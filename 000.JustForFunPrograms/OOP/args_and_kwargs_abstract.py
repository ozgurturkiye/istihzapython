#Başta kafamız çok karışsa da 
#Parametrelerin handi tipte olduğunu öğrenerek başladık
# *args demet  **kwargs sözlük  - sonrası anlam kazanıyor
# args[0] şeklinde kwargs.get('KEY') şeklinde kullanılıyor.
# kwargs.get('KEY') kullanmak önemli 
# kwargs['KEY'] olmadığı takdirde hata verip programı sonlandırıyor.
# sözlük göndermek için argüman kısmına **sözlük yazıyoruz. Önemlidir.


class Asker():
  def __init__(self, *args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    
    self.isim = args[0]
    self.rütbe = args[1]
    self.güç = kwargs.get('güç')
    self.kwargs = kwargs


cost = {"odun": 50, "tuğla": 70, "demir": 100, "tahıl": 30 }
a = Asker("Özgür", "Bay", güç = 22, **cost)

print(a.isim, a.rütbe, a.güç, a.kwargs.get('odun'), a.kwargs.get('tuğla'))
