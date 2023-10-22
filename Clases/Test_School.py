import unittest

from School import School, Student, Grade, Lector, Subject


class SchoolTest(unittest.TestCase):

    def test_create_school(self):
        school = School("My School")
        self.assertEqual(school.name, "My School")

    def test_create_student(self):
        student = Student("John Doe", 12345)
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.id, 12345)

    def test_create_grade(self):
        grade = Grade(10)
        self.assertEqual(grade.grade_id, "10")
        self.assertEqual(grade.lectors, [])

    def test_add_lector_to_grade(self):
        grade = Grade(10)
        lector = Lector("Mathematics")
        grade.add_lector(lector)
        self.assertEqual(grade.lectors, [lector])

    def test_create_lector(self):
        lector = Lector("Mathematics")
        self.assertEqual(lector.subjects, ["Mathematics"])

    def test_add_subject_to_lector(self):
        lector = Lector("Mathematics")
        lector.add_subject("Physics")
        self.assertEqual(lector.subjects, ["Mathematics", "Physics"])

    def test_create_subject(self):
        subject = Subject("Mathematics", 2, 1)
        self.assertEqual(subject.name, "Mathematics")
        self.assertEqual(subject.count_of_lectures, 2)
        self.assertEqual(subject.count_of_practices, 1)

if __name__ == "__main__":
    unittest.main()
