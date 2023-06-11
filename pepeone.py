class Student:
    listofstudents = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.allgrades = []
    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
                lecture.allgrades +=[grade]
            else:
                lecture.grades[course] = [grade]
                lecture.allgrades =[grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за домашние задания: {(sum(self.allgrades)/len(self.allgrades))}\n'f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' f'Завершенные курсы: {",".join(self.finished_courses)}'
    def __lt__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) < (sum(other.allgrades)/len(other.allgrades))
    def __le__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) > (sum(other.allgrades)/len(other.allgrades))
    def __eq__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) is (sum(other.allgrades)/len(other.allgrades))

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecture(Mentor):
    listoflectures = []
    def __init__(self,name, surname):
        self.grades = {}
        self.courses_attached = []
        self.allgrades = []
        self.name = name
        self.surname = surname
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'f'Средняя оценка за домашние задания: {(sum(self.allgrades)/len(self.allgrades))}\n' 
    def __lt__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) < (sum(other.allgrades)/len(other.allgrades))
    def __le__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) > (sum(other.allgrades)/len(other.allgrades))
    def __eq__(self,other):
        return (sum(self.allgrades)/len(self.allgrades)) is (sum(other.allgrades)/len(other.allgrades))
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.allgrades +=[grade]
            else:
                student.grades[course] = [grade]
                student.allgrades = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' 
def std(listofstudents,course):
    sum_1 = 0
    length = 0
    for student in listofstudents:
        sum_1 += (sum(student.grades.get(course)))
        length += (len(student.grades.get(course)))
    print(sum_1/length)
def std(listoflectures,course):
    sum_1 = 0
    length = 0
    for lecture in listoflectures:
        sum_1 += (sum(lecture.grades.get(course)))
        length += (len(lecture.grades.get(course)))
    print(sum_1/length)
    



best_student = Student('Ruoy', 'Eman', 'your_gender')
worst_student = Student('Helly','Coptstrong','Boeing AH-64 Apache')
best_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Python','Java']
worst_student.finished_courses = ['Git']
best_student.finished_courses = ['Git']
cool_reviewer = Reviewer('Some', 'Buddy')
bad_reviewer = Reviewer ('Buddy','Some')
cool_lecture = Lecture('Some','Buddy')
strange_lecture = Lecture('Soddy','Bome')
Student.listofstudents.append(best_student)
Student.listofstudents.append(worst_student)
Lecture.listoflectures.append(cool_lecture)
Lecture.listoflectures.append(strange_lecture)
cool_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Java','Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
bad_reviewer.rate_hw(worst_student, 'Java', 2)
bad_reviewer.rate_hw(worst_student, 'Java', 1)
bad_reviewer.rate_hw(worst_student, 'Java', 2)
bad_reviewer.rate_hw(worst_student, 'Python', 2)
bad_reviewer.rate_hw(worst_student, 'Python', 2)
bad_reviewer.rate_hw(worst_student, 'Python', 2)
#print(best_student.grades)
strange_lecture.courses_attached += ['Python','Java']
cool_lecture.courses_attached += ['Python']
best_student.rate_hw(cool_lecture, 'Python', 10)
best_student.rate_hw(cool_lecture, 'Python', 10)
best_student.rate_hw(cool_lecture, 'Python', 10)
worst_student.rate_hw(strange_lecture, 'Java', 2)
worst_student.rate_hw(strange_lecture, 'Java', 1)
worst_student.rate_hw(strange_lecture, 'Java', 3)
worst_student.rate_hw(strange_lecture, 'Python', 2)
worst_student.rate_hw(strange_lecture, 'Python', 1)
worst_student.rate_hw(strange_lecture, 'Python', 3)
std(Lecture.listoflectures,'Python')
std(Student.listofstudents,'Python')
#print(cool_lecture.grades)
# print (best_student)
# print(cool_reviewer)
# print(cool_lecture)
# print(worst_student)
# print(worst_student == best_student)
# print(worst_student > best_student)
# print(worst_student < best_student)
# print(cool_lecture.listoflectures)
# print(*worst_student.grades)
# print('Python'.values((worst_student.grades)))
# print(''.join(map(str, Student.listofstudents)))
# print(Student.listofstudents)
# print(sum(worst_student.grades.get('Python')))