# Example of basic unittest for exam score average
print("Karne notu hesaplama programına hoş geldiniz!")

def set_course_name(course_name):
    """Learn course name"""
    # if course name is "" return false and call yourself
    return course_name

def set_exam_number() -> int:
    """Set exam number with user input"""
    exam_number = int(input("Kaç sınav oldunuz.:"))
    return exam_number

def set_other_exam_number() -> int:
    """Set other exam number with user input"""
    other_exam_number = int(input("Kaç sözlü oldunuz.:"))
    return other_exam_number

def set_exam_scores(exam_number) -> list:
    """Get exam_scores from user and return exam list [33, 60, 100] example"""
    exams = []
    for i in range(exam_number):
        score = int(input(f"{(i + 1)}'inci sınav notunu giriniz: "))
        exams.append(score)
    return exams 

def set_other_exam_scores(other_exam_number):
    """Get other_exam_scores from user and return list [] if it's not empty"""
    other_exams = []
    if other_exam_number:
        for i in range(other_exam_number):
            score = int(input(f"{(i + 1)}'inci sınav notunu giriniz: "))
            other_exams.append(score)
    return other_exams

def get_result(exams, other_exams, total_exam_count):
    """Takes two list, total_exam_count and return result"""
    total_score = sum(exams) + sum(other_exams)
    result = (total_score / total_exam_count) 
    return result

def main():
    """Fonksiyonların çalışma sırasını bunun içine bir saklayalım bakalılm """

    # Başlama noktası
    course_name = input("Lütfen ders adını giriniz: ")
    course = set_course_name(course_name)

    exam_number = set_exam_number()
    other_exam_number = set_other_exam_number()

    total_exam_count = exam_number + other_exam_number # total exam count

    exam_scores = set_exam_scores(exam_number)
    other_exam_scores = set_other_exam_scores(other_exam_number)

    result = get_result(exam_scores, other_exam_scores, total_exam_count)
    print(course, result)
    print(f"Ders: {course}, ortalama: {result}")

if __name__ == "__main__":
    # execute only if run as a script
    main()
