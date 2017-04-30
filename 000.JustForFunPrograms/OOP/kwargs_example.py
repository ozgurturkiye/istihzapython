#Bu bölümde **kwargs kullanım örneklerini anlatalım

class Asker():
  def __init__(self, **kwargs):
    self.name = kwargs.get('name')
    print(type(kwargs))  #Sözlüktür
    print(kwargs)        #İçeriği görüntüleyelim
    print("---------------------")
    print(kwargs.get('name'))   #name isimli bir parametre gönderilidiğini varsayıyoruz
    
    #Bu kullanım önerilmez name yok ise program patlar :)
    #print(kwargs['name'])   #Bu şekilde kullanırsan eğer name yoksa program Hata verir
    
    self.cost = kwargs.get('cost')

#Asker sınıfını örneklendirirme 

#1. Hatasız çalışır
print("Birinci örneklendirirme")
a = Asker(name = "Özgür")


#2. Hatasız çalışır
print("İkinci örneklendirirme")
sözlük = {"name": "Özdemir"}
b = Asker(**sözlük)


#3. Hatasız çalışır
print("Üçüncü örneklendirirme")
c = Asker(**{"name": "Şehnaz"})


#4. Hatasız çalışır. Sözlük gönderme olayı mutlaka ** kullanıyoruz
sözlük = {"kedi": "kakası", "eşşek": "sıpası"}
d = Asker(name = "Hobaa", **sözlük)



