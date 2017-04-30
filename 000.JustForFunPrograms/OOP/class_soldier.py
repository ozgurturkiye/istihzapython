class Soldier():
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost
    #.cost = {"wood": 0, "brick": 0, "iron": 0, "grain": 0}
    self.attack = 0
    self.defence_infantry = 0
    self.defence_cavalry = 0
    self.speed = 0
    self.transport_capacity = 0
    self.speed = 0
    self.training_time = 0
    self.precondition_survey = []
    self.precondition_training = []

#Sıralı parametre olarak göndersek nasıl olur düşüncesi
class Asker():
  def __init__(self, *args):
    self.name = args[0]
    self.cost = args[1]
    #.cost = {"wood": 0, "brick": 0, "iron": 0, "grain": 0}
    self.attack = args[2]
    self.defence_infantry = 0
    self.defence_cavalry = 0
    self.speed = 0
    self.transport_capacity = 0
    self.speed = 0
    self.training_time = 0
    self.precondition_survey = []
    self.precondition_training = []


class Phalanx():
  def __init__(self, name):
    self.name = name
    self.cost = {"wood": 100, "brick": 130, "iron": 55, "grain": 30}
    self.attack = 15
    self.defence_infantry = 40
    self.defence_cavalry = 50
    self.speed = 7
    self.transport_capacity = 35
    self.speed = 1
    self.training_time = "0:17:20"
    self.precondition_survey = None
    self.precondition_training = {"barracks": 1}


class Kılıçlı():
  def __init__(self, name):
    self.name = name
    self.cost = {"wood": 140, "brick": 150, "iron": 185, "grain": 60}
    self.attack = 65
    self.defence_infantry = 35
    self.defence_cavalry = 20
    self.speed = 6
    self.transport_capacity = 45
    self.speed = 1
    self.training_time = "0:24:00"
    self.precondition_survey = {"academy": 3, "armor_foundry": 1}
    self.precondition_training = {"barracks": 1}
