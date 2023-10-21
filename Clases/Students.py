class Student():
    # Class attributes
    static_object_count = 0

    def __init__(self, first_name, last_name, course, subject, university, email, cellphone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.subject = subject
        self.university = university
        self.email = email
        self.cellphone = cellphone

        Student.static_object_count += 1

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def university(self):
        return self._university

    @university.setter
    def university(self, value):
        self._university = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def cellphone(self):
        return self._cellphone

    @cellphone.setter
    def cellphone(self, value):
        self._cellphone = value

    def student_info(self):
        print("Student information")
        print("First name: ", self.first_name)
        print("Last name: ", self.last_name)
        print("Course: ", self.course)
        print("Subject: ", self.subject)
        print("University: ", self.university)
        print("Email: ", self.email)
        print("Cellphone: ", self.cellphone)


class StudentTest:
    _students = []

    @staticmethod
    def create_students():
        student_1 = Student("Juan", "Perez", "Python", "Programming", "Udemy", "juan@abv.bg", "123456789")
        student_2 = Student("Maria", "Gomez", "Python", "Programming", "Udemy", "maria@abv.bg")
        student_3 = Student("Pedro", "Garcia", "Python", "Programming", "Udemy", "pedro@abv.bg", "123456789")

        StudentTest._students.append(student_1)
        StudentTest._students.append(student_3)
        StudentTest._students.append(student_2)

    @staticmethod
    def run_tests():
        StudentTest.create_students()

        for student in StudentTest._students:
            student.student_info()

        print("Number of students: ", Student.static_object_count)


# Run the tests
StudentTest.run_tests()
