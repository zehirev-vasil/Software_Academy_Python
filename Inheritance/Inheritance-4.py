class Human:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class School:

    def __init__(self, name):
        self.name = name


class Student(Human):

    def __init__(self, first_name, last_name,  student_id):
        super().__init__(first_name=first_name, last_name=last_name)
        self.id = student_id


class Grade:

    def __init__(self, grade_id):
        self.grade_id = str(grade_id)
        self.lectors = []

    def add_lector(self, lector):
        self.lectors.append(lector)


class Lector(Human):

    def __init__(self, first_name, last_name, subjects=None):
        super().__init__(first_name, last_name)
        self.subjects = [subjects] if subjects else []

    def add_subject(self, subject):
        self.subjects.append(subject)


class Subject:

    def __init__(self, name, count_of_lectures, count_of_practices):
        self.name = name
        self.count_of_lectures = count_of_lectures
        self.count_of_practices = count_of_practices


new_lector = Lector('Vasil', 'Zehirev', 'Mathematics')
print(new_lector)