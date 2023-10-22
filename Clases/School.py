class School:

    def __init__(self, name):
        self.name = name


class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id


class Grade:

    def __init__(self, grade_id):
        self.grade_id = str(grade_id)
        self.lectors = []

    def add_lector(self, lector):
        self.lectors.append(lector)


class Lector:

    def __init__(self, subjects=None):
        self.subjects = [subjects]

    def add_subject(self, subject):
        self.subjects.append(subject)


class Subject:

    def __init__(self, name, count_of_lectures, count_of_practices):
        self.name = name
        self.count_of_lectures = count_of_lectures
        self.count_of_practices = count_of_practices
