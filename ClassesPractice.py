class Course_class:
    def __init__(self, course_id, course_title, teacher_id,
                 department, year_of_offering):
        self.course_id = course_id
        self.course_title = course_title
        self.teacher_id = teacher_id
        self.department = department
        self.year_of_offering = year_of_offering

    def display_course(self):
        print("Course ID:", self.course_id)
        print("Course Title:", self.course_title)
        print("Teacher ID:", self.teacher_id)
        print("Department:", self.department)
        print("Year of Offering:", self.year_of_offering)
        print("-" * 30)


class Teacher_class:
    def __init__(self, teacher_id, teacher_name, department,
                 country, phone, emailid):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.department = department
        self.country = country
        self.phone = phone
        self.emailid = emailid

    def display_teacher(self):
        print("Teacher ID:", self.teacher_id)
        print("Name:", self.teacher_name)
        print("Department:", self.department)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.emailid)
        print("-" * 30)


class Student_class:
    def __init__(self, student_id, name, password, address,
                 phone, emailid, courses_enrolled=None):
        self.student_id = student_id
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.emailid = emailid
        self.courses_enrolled = (
            [] if courses_enrolled is None else courses_enrolled
        )

    def enroll_course(self, course_id):
        if course_id not in self.courses_enrolled:
            self.courses_enrolled.append(course_id)
            print("Course enrolled successfully!")
        else:
            print("Student is already enrolled in this course.")

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)
        print("Email:", self.emailid)
        print("Courses Enrolled:", self.courses_enrolled)
        print("-" * 30)


courses = []
teachers = []
students = []


def add_course():
    course_id = input("Enter course ID: ")
    course_title = input("Enter course title: ")
    teacher_id = input("Enter teacher ID: ")
    department = input("Enter department: ")
    year = input("Enter year of offering: ")

    courses.append(Course_class(
        course_id, course_title, teacher_id, department, year
    ))
    print("Course added successfully!")


def add_teacher():
    teacher_id = input("Enter teacher ID: ")
    teacher_name = input("Enter teacher name: ")
    department = input("Enter department: ")
    country = input("Enter country: ")
    phone = input("Enter phone: ")
    emailid = input("Enter email: ")

    teachers.append(Teacher_class(
        teacher_id, teacher_name, department,
        country, phone, emailid
    ))
    print("Teacher added successfully!")


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    password = input("Enter password: ")
    address = input("Enter address: ")
    phone = input("Enter phone: ")
    emailid = input("Enter email: ")

    students.append(Student_class(
        student_id, name, password, address, phone, emailid
    ))
    print("Student added successfully!")


def display_courses():
    if not courses:
        print("No courses available.")
    for course in courses:
        course.display_course()


def display_teachers():
    if not teachers:
        print("No teachers available.")
    for teacher in teachers:
        teacher.display_teacher()


def display_students():
    if not students:
        print("No students available.")
    for student in students:
        student.display_student()


def enroll_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")

    student = next(
        (s for s in students if s.student_id == student_id), None
    )
    course = next(
        (c for c in courses if c.course_id == course_id), None
    )

    if student is None:
        print("Student not found.")
    elif course is None:
        print("Course not found.")
    else:
        student.enroll_course(course_id)


# Create at least three objects of each class
courses.extend([
    Course_class("C101", "Python Programming", "T101",
                 "Computer Science", 2026),
    Course_class("C102", "Database Systems", "T102",
                 "Information Technology", 2026),
    Course_class("C103", "Web Development", "T103",
                 "Computer Science", 2026)
])

teachers.extend([
    Teacher_class("T101", "Alice Brown", "Computer Science",
                  "USA", "1111111111", "alice@example.com"),
    Teacher_class("T102", "David Smith", "Information Technology",
                  "UK", "2222222222", "david@example.com"),
    Teacher_class("T103", "Mary Jones", "Computer Science",
                  "Canada", "3333333333", "mary@example.com")
])

students.extend([
    Student_class("S101", "John", "pass101", "New York",
                  "4444444444", "john@example.com"),
    Student_class("S102", "Emma", "pass102", "London",
                  "5555555555", "emma@example.com"),
    Student_class("S103", "Ryan", "pass103", "Toronto",
                  "6666666666", "ryan@example.com")
])


while True:
    print("\n===== STUDENT COURSE MANAGEMENT =====")
    print("1. Add Course")
    print("2. Add Teacher")
    print("3. Add Student")
    print("4. Display All Courses")
    print("5. Display All Teachers")
    print("6. Display All Students")
    print("7. Enroll Student in Course")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_course()
    elif choice == "2":
        add_teacher()
    elif choice == "3":
        add_student()
    elif choice == "4":
        display_courses()
    elif choice == "5":
        display_teachers()
    elif choice == "6":
        display_students()
    elif choice == "7":
        enroll_student()
    elif choice == "8":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
