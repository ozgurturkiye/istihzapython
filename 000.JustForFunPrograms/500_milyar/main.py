import sys
import sqlite3
import random
import signal
import os
import time

class Question(): # Sorular sınıfı
  with sqlite3.connect('vt.sqlite') as vt:  #vt.sqlite isimli veritabanını kullan.
    im = vt.cursor()

    im.execute("""SELECT * FROM questions WHERE difficulty = "1" """)
    question_easy = im.fetchall()
    question_easy = random.sample(question_easy, 3) # Rasgele üç örnek aldık

    im.execute("""SELECT * FROM questions WHERE difficulty = "2" """)
    question_normal = im.fetchall()
    question_normal = random.sample(question_normal, 3)

    im.execute("""SELECT * FROM questions WHERE difficulty = "3" """)
    question_hard = im.fetchall()
    question_hard = random.sample(question_hard, 3)

    questions = question_easy + question_normal + question_hard # Her bir zorluk derecesinden listeleri birleştir


class Announcer(): # Yarışma sunucusu sınıfı
  name = ""

  def __init__(self):
    self.name = "Özgür"

  def wait_for_question(self):
    print(yarışmacı.name, "sorunuz hazırlanıyor...")
    for i in range(6):
        print("*", end="", flush=True) # flush kullanmazsa sonda yazıyor.
        time.sleep(0.5)
    print("")

  def ask_question(self, arg1, arg2, arg3):
    print(arg1, "Doğru Şık:", arg2, "Zorluk:", arg3) # Soruyu göster
    print("*" * 20, "5 Saniye içinde cevabı giriniz!!!", "*" * 20)

  def say_thanks(self):
    print("Tebrikler doğru cevap, toplam ödülünüz:", yarışmacı.level_money_price[yarışmacı.level])

  def say_good_bye(self):
    print("Yanlış Cevap! Yarışma bitti.")
    if yarışmacı.level >= 6:
      print("Ödülünüz:", yarışmacı.level_money_price[6], "TL")
    elif yarışmacı.level >= 3:
      print("Ödülünüz:", yarışmacı.level_money_price[3], "TL")
    else:
      print("Hiç ödül kazanamadınız!")

    self.finish_programme()

  def finish_programme(self):
    sys.exit(0)


class Competitor(): # Yarışmacı
  name = ""
  level = 0 # Bu örnek niteliğine döndürülebilir mi?
  level_money_price = [0, 150, 500, 1000, 3000, 5000, 10000, 25000, 50000, 100000, 500000]

  def __init__(self):
    self.name = input("Lütfen adınızı giriniz: ")
    self.answer = ""

  def answer_question(self):
    self.answer = input("Lütfen doğru şıkkı giriniz:").upper() # user answer

  def answer_is_right(self, verilen_cevap):
      signal.alarm(0)
      if self.answer == verilen_cevap:
          return True
      else:
          return False

  def level_up(self):
    self.level += 1

  def level_control(self):
    if self.level == 9:# 15 soruyu da bilirse büyük ödülü kazanır
      print("Büyük ödülü kazandınız ödülünüz ***1000000TL***")
      sunucu.finish_programme()


sunucu = Announcer()
yarışmacı = Competitor()
sorular = Question() # Burada sorular zorluk derecesine göre sıralanıp sorular listesi geliyor.

def handler(signum, frame):
    print('5 saniyede cevap girmediniz! ', signum)
    sunucu.say_good_bye()

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)


for soru, cevap, zorluk in sorular.questions:
  os.system("clear") # Her sorunun başında ekranı temizle
  sunucu.wait_for_question()
  sunucu.ask_question(soru, cevap, zorluk) # Soru sor
  signal.alarm(5)
  yarışmacı.answer_question() # Take user answer
  if yarışmacı.answer_is_right(cevap): # Verilen cevap doğru şık ile aynı mı
    yarışmacı.level_up()
    yarışmacı.level_control()
    sunucu.say_thanks()
  else:
    sunucu.say_good_bye()
