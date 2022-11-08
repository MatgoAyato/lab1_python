groupmates = [
    {
        "name": "Никита ",
        "surname": "Люблин",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 4, 3]
    },
    {
        "name": "Генадий",
        "surname": "Левин",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Александр",
        "surname": "Правин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Василий",
        "surname": "Жабрин",
        "exams": ["Ин.язык", "ИС", "Web"],
        "marks": [5, 5, 4]
    },
    {
        "name": "Маским",
        "surname": "Астахин",
        "exams": ["Информатика", "АиГ", "Физика"],
        "marks": [4, 5, 3]
    }
]
sred_mark=float(input("Введите среднюю оценку: "))
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        if (sred_mark < (sum(student["marks"])/len(student["marks"]))):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)

