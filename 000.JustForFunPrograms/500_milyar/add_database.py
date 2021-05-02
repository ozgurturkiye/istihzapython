import sqlite3


with sqlite3.connect('vt.sqlite') as vt:
    im = vt.cursor()

    veriler = [
  ["""Türkiye'nin başkenti neresidir?
  A)Ankara
  B)İstanbul
  C)Bursa
  D)Malkara""", "A", "1"],
  ["""Türkiye'nin en yüksek dağı neresidir?
  A)Palandöken
  B)Ağrı
  C)Uludağ
  D)Merkez
  """, "B", "1"],
  ["""Bir kenarı 4 cm olan karenin çevresi kaç cm'dir?
  A)4
  B)8
  C)12
  D)16
  """, "D", "2"],
  ["""Dünyanın en derin çukuru neresidir?
  A)Mariana çukuru
  B)Tuz Gölü
  C)Hazar Denizi
  D)Hint Okyanusu""", "A", "3"]
  ]

    im.execute("""CREATE TABLE IF NOT EXISTS questions
        (question, answer, difficulty)""")

    for veri in veriler:
        im.execute("""INSERT INTO questions VALUES
            (?, ?, ?)""", veri)

    vt.commit()
