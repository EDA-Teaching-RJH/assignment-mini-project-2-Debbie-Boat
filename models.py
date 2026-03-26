from validators import validate_email, validate_student_id


class Student:
    VALID_DEGREES = ["ECE", "BIO", "MECH", "EEE"]

    def __init__(self, name, degree, student_id, email):
        if not name:
            raise ValueError("Name cannot be empty")

        if degree not in self.VALID_DEGREES:
            raise ValueError("Invalid degree")

        if not validate_student_id(student_id):
            raise ValueError("ID must be 6 digits")

        if not validate_email(email):
            raise ValueError("Invalid email")

        self.name = name
        self.degree = degree
        self.student_id = student_id
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.degree}"


class UndergraduateStudent(Student):
    def __init__(self, name, degree, student_id, email,
                 foundation=False, industry=False, repeater=False):
        super().__init__(name, degree, student_id, email)
        self.foundation = foundation
        self.industry = industry
        self.repeater = repeater

    def __str__(self):
        return f"UG: {super().__str__()}"


class GraduateStudent(Student):
    def __init__(self, name, degree, student_id, email, research_topic):
        super().__init__(name, degree, student_id, email)
        self.research_topic = research_topic

    def __str__(self):
        return f"PG: {super().__str__()} - {self.research_topic}"


class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        if student.student_id in [s.student_id for s in self.students]:
            print("Student already enrolled")
        else:
            self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]

    def __str__(self):
        return f"{self.name} ({self.code}) - {len(self.students)} students"

    # Extension
    def __add__(self, other):
        new_course = Course(self.name + "+" + other.name, self.code + "+" + other.code)

        unique = {}
        for s in self.students + other.students:
            unique[s.student_id] = s

        new_course.students = list(unique.values())
        return new_course