# Öğrenci ortalama not hesaplama

# 1- Ders Adı
# 2- Sınav Sayısı
# 3- Sınav çeşitleri (Yazılı, Sözlü, Proje)
# Not- Sınav notları 0-100 arasındadır.

def basla():
  """Tüm kodu bunun içine alalım ki main.py dan çalıştıralım """

  print("Karne notu hesaplama programına hoş geldiniz!")

  def lecture_name():
    """Learn lecture name"""
    # buraya yaz bro....
    lecture_name = input("Lütfen ders adını giriniz: ")
    return lecture_name

  def exam_count():
    """Learn exam count from user"""
    exam_count_number = input("Kaç sınav oldunuz.:")
    return int(exam_count_number)

  def sozlu_count():
    """Learn exam count from user if there is no sozlu notu write number 0 """
    sozlu_count_number = input("Kaç sözlü oldunuz.:")
    return int(sozlu_count_number)

  def exam_scores(exam_count_number):
    """Ask exam_count_number times for exam results and return as a list [33, 60, 100] example"""
    for i in range(exam_count_number):
      exams.append(int(input(f"{(i + 1)}'inci sınav notunu giriniz: ")))
    return exams 

  def sozlus_scores(sozlu_count_number):
    """Ask sozlu_count_number times for sozlus results and return as a list [33, 60, 100] example"""
    if sozlu_count_number:
      for i in range(sozlu_count_number):
        sozlus.append(int(input(f"{(i + 1)}'inci sozlu notunu giriniz: ")))
    return sozlus

  def result_score(exams, sozlus):
    """Takes two list and return karne notu"""
    total_exam_number_count = len(exams) + len(sozlus)
    total_score = sum(exams) + sum(sozlus)
    result = (total_score / total_exam_number_count) 
    return result

  # Başlama noktası
  lecture = lecture_name()
  exam_count_number = exam_count()
  sozlu_count_number = sozlu_count()
  total_count = exam_count_number + sozlu_count_number
  # Bilgileri aldık şimdi sınav notlarını almaya başlayalım
  exams = []
  sozlus = []  # Bu değişken isimleri insan anlar şekle döndürülecek :)

  exams = exam_scores(exam_count_number)
  sozlus = sozlus_scores(sozlu_count_number)  # yazarken gülüyorum :):):) böyle isim mi olur
  result = result_score(exams, sozlus)
  print(lecture, result)
  print(f"Ders: {lecture}, ortalama: {result}")

# bro ?????????
# nasıl patladı gitti program :)
