from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average(self):
        lst = []
        for course in self.grades:
            for i in self.grades.setdefault(course):
                lst.append(i)
        if not lst:
            return 0
        return mean(lst)

    def rate_lector(self, lecturer, course, grades):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания:' \
              f' {round(self.average(), 1)} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.average() < other.average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def average(self):
        lst = []
        for course in self.courses_attached:
            for i in self.grades.setdefault(course):
                lst.append(i)
        if not lst:
            return 0
        return mean(lst)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(self.average(), 1)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average() < other.average()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


first_student = Student('Harry', 'Potter', 'Man')
second_student = Student('Hermione', 'Granger', 'Woman')
first_lector = Lecturer('Severus', 'Snape')
second_lector = Lecturer('Albus', 'Dumbledore')
first_reviewer = Reviewer('Minerva', 'McGonagall')
second_reviewer = Reviewer('Rubeus', 'Hagrid')

first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Java']

first_lector.courses_attached += ['Python']
second_lector.courses_attached += ['Git']
first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 10)
first_reviewer.rate_hw(second_student, 'Python', 9)

first_student.rate_lector(first_lector, 'Python', 6)
first_student.rate_lector(first_lector, 'Python', 7)
first_student.rate_lector(first_lector, 'Python', 5)
second_student.rate_lector(first_lector, 'Python', 10)
second_student.rate_lector(first_lector, 'Python', 7)
second_student.rate_lector(first_lector, 'Python', 4)

first_student.rate_lector(second_lector, 'Git', 10)
first_student.rate_lector(second_lector, 'Git', 10)
first_student.rate_lector(second_lector, 'Git', 10)
second_student.rate_lector(second_lector, 'Git', 6)
second_student.rate_lector(second_lector, 'Git', 8)
second_student.rate_lector(second_lector, 'Git', 7)

print(first_student)
print(second_student)
print(first_lector)
print(second_lector)
print(first_reviewer)
print(second_reviewer)
print(first_student < second_student)
print(first_lector > second_lector)


def average_student(students, course):
    lst = []
    for i in students:
        for a in i.grades.setdefault(course):
            lst.append(a)
    print(mean(lst))


students = [first_student, second_student]
average_student(students, 'Python')


def average_lector(lectors, course):
    lst = []
    for i in lectors:
        for a in i.grades.setdefault(course):
            lst.append(a)
    print(mean(lst))


lectors = [first_lector, second_lector]
average_lector(lectors, 'Python')
