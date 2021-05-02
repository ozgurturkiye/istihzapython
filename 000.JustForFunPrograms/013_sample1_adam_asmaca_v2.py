
def welcome():
  """ This will be welcome screen on the game"""
  print("""
 [H]=======ADAM-ASMACA======[-][o][x]
 |                                 |
 |          Hoşgeldiniz!           |
 |           Sürüm 0.1             |
 |    Devam etmek için kullanıcı   |
 |         adınızı girin.          |
 |                                 |
 |=================================|
""")

class User:
  """Base class for a user of game."""

  def __init__(self):
    """Constructor. Called when game started to create User attribute.
    (name, point, mistake, known_character_count, guested_characters)"""

    self.name = input("Choose your player name: ")
    self.point = 0
    self.mistake = 0
    self.mistakes_all = ["0", "/", "|", "\\", "/", "\\"]
    self.mistakes_first = ["","","","","",""]
    self.known_character_count = 0
    self.guested_characters = [] # This will be like ["a", "b", "c" .....]
    self.word_copy = []

  def print_user_name(self):
    print(self.name)


class Game:
  """Class for game objects.
  Word list - it will be sqlite database"""

  word_pool = ["iskorpit", "kalemlik", "bilgisayar"]

  def __init__(self, user):
    """Constructor. Called when game start"""
    
    self.word = self.word_pool[0].upper() # select random word in database
    self.word_length = len(self.word) # We will use this with total mistake
    user.word_copy = ["_" for i in range(self.word_length) ]


class Control:
  """Game Controller Class"""

  word_list = list("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ")

  def user_general_info(self, user, game):
    """This method print all user general info"""
    print("""
  user name: {}
  word length: {}
  User mistake: {} 
  word status: {} 
  guested characters: {}
  """.format(user.name, game.word_length, user.mistake, 
  user.word_copy, user.guested_characters,))

    print("""
   _________
  |         |
  |         {}
  |        {}{}{}
  |        {} {}
  |
  |
 ----
    
    """.format(*user.mistakes_first))

  def is_mistake_full(self, user):  # 6 is limit for mistake
    if user.mistake > 5:
      print("Game Over, You Lose!")
      exit()
    else:
      pass

  def is_all_char_found(self, user, game):
    if user.known_character_count >= game.word_length:
      print("Congratulations You Won!")
      exit()
    else:
      pass
    
  def get_one_char(self, user, game):
    self.get_char = input("Bir harf giriniz: ").upper()

    if self.get_char == "":
      print("Boş giremezsiniz!")
      self.get_one_char(user, game)
    elif len(self.get_char) > 1:
      print("Tek harf girmelisiniz!")
      self.get_one_char(user, game)
    elif self.get_char not in self.word_list:
      print("Yalnızca latin harfleri girebilirsiniz!")
      self.get_one_char(user, game)
    elif self.get_char in user.guested_characters:
      print("Daha önce girilen harfleri giremezsiniz!")
      self.get_one_char(user, game)
    else:
      print("Kelime kontrol ediliyor...") # Letter passed
  
  def is_char_in_word(self, user, game):
    if self.get_char in game.word:
      print("Tebrikler bu harf var!")
      for i in range(len(game.word)):
        if self.get_char == game.word[i]:
          user.word_copy[i] = self.get_char
          user.known_character_count += 1
          self.is_all_char_found(user, game)   
      print(user.word_copy)
    else:
      print("Üzgünüm '{}' harfi kelimede yok.".format(self.get_char))
      # user mistake list changing for hanging 
      user.mistakes_first[user.mistake] = user.mistakes_all[user.mistake] 
      user.mistake += 1
      self.is_mistake_full(user)
    
    user.guested_characters.append(self.get_char)

  def make_user_guest(self, user, game):
    self.user_guest = input("Tahminde bulunmak ister misiniz: E-H").upper()
    if self.user_guest == "E":
      self.guest = input("Tahmininizi yazınız: ").upper()
      if self.guest == game.word:
        print("Tebrikler kazandınız!")
        exit()
      else:
        user.mistakes_first[user.mistake] = user.mistakes_all[user.mistake]
        user.mistake += 1
        if user.mistake >= game.word_length:
          print("Oyunu kaybettiniz!")
          exit()
      print("Tahmin tutmadı harf tahmin etmeye devam!")
    else:
      print("Harf tahmin etmeye devam!")
  

def main():
  welcome()
  user = User()
  game = Game(user)
  control = Control()
  while True:
    control.user_general_info(user, game)
    control.is_mistake_full(user) # user.mistake control
    control.is_all_char_found(user, game) # all character is found?
    control.get_one_char(user, game)
    control.is_char_in_word(user, game)
    control.make_user_guest(user, game)

  
if __name__ == "__main__":
    main()
