class Student():

  students = []
  result = []
  
  def __init__(self, name, homework, quizzes, tests):
    self.name = name
    self.homework = homework
    self.quizzes = quizzes
    self.tests = tests
  
  @classmethod
  def get_class_average(cls):           # Doğru çalıştıramadık henüz
    print("Sınıf metodu çalıştırıldı")
    for student in cls.students:
      print(student)


  def average(self, numbers):
    return float(sum(numbers)) / len(numbers)
    
  def get_average(self):
    self.homework = self.average(self.homework)
    self.quizzes = self.average(self.quizzes)
    self.tests = self.average(self.tests)
    self.generic_average = 0.1 * self.homework + 0.3 * self.quizzes + 0.6 * self.tests # ortalama ağırlıklar
  
  def get_letter_grade(self):
    if self.generic_average >= 90:
      return "A"
    elif self.generic_average >= 80:
      return "B"
    elif self.generic_average >= 70:
      return "C"
    elif self.generic_average >= 60:
      return "D"
    else:
      return "F"



lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


students = [lloyd, alice, tyler]

ogr = Student(**lloyd)

#ogr2 = Student(**listem[0])
students_obj = ["","",""]
for i in range(len(students)-1):
  students_obj[i] = Student(**students[i]) #students_obj listesi içinde nesneleri tutuyoruz
  

