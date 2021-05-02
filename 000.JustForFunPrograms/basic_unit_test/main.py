
# This is a basic example of unittest
#from circles import circle_area
from dictionary import add_word
from exams import basla

basla()

a = add_word("cat", "kedi")
print(a)

b = add_word("dog", "kopek")
print(b)

#ali yazmasını nasıl engelleyeceksin ki?
# anca type kontrolü olur bence, sayı yazdırılmaz

#print(circle_area(3))


# ali yazmasında sıkıntı yok sözlüğü biz oluşturuyoruz.
# sayı da ekleyebilir "3" = "three" gibi tabi string olarak
# önce istediğini ekleyebiliyor mu onu test edelim
# 
