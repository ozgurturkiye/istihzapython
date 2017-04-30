# Sınıf içerisine, içinde sözlük olan sözlük gönderme :)
# Travian building modulü yazdık :)

class Building():
  def __init__(self, **kwargs):
    self.kwargs = kwargs
    print(kwargs)
    self.name = kwargs['name']
    self.wood = kwargs['wood']
    self.brick = kwargs['brick']
    self.iron = kwargs['iron']
    self.grain = kwargs['grain']
    self.built_time = kwargs['built_time']
    self.precondition = kwargs.get('precondition') #get kullandık patlamasın


trade_center = {"name": "trade_center", 
           "wood": 19, 
           "brick": 44, 
           "iron": 599, 
           "grain": 498, 
           "precondition": {"bazaar": 20, "stable": 10}, 
           "built_time": "15:00:00"}


# Sınıfı örneklendirip birkaç deneme yapalım
a = Building(**trade_center)
print(a.name)
print(a.kwargs['name'])
print(a.precondition.get('bazaar'))
print(a.kwargs.get('precondition').get('bazaar')) # get kullan patlamasın
