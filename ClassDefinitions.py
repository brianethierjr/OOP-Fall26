#Create the following classes: student, faculty, and courses.
#Add the following functions to the class definitions on top of the already existing ones:
#Student - assign_adivor(); Faculty - enroll_students(); Courses - teaching_faculty(), enrolled_students()
#Hint: Use myStudentsList to store students objects, myFacultyList to store Faculty Objects, and myCoursesList to store courses.


class Faculty:
    def __init__(self):
        self.name = ""
        self.id = ""
        self.department = ""
        self.myStudentsList = []

    def create_faculty(self):
        self.name = input("Enter Faculty name: ")
        self.id = input("Enter Faculty ID: ")
        self.department = input("Enter Faculty department: ")

    def display_faculty(self):
        print("Faculty name: " + self.name)
        print("Faculty ID: " + self.id)
        print("Faculty department: " + self.department)

    def enroll_students(self, student):
        self.myStudentsList.append(student)


class Student:
    def __init__(self):
        self.name = ""
        self.year = ""
        self.major = ""
        self.advisor = None

    def create_student(self):
        self.name = input("Enter Student name: ")
        self.year = input("Enter Student year: ")
        self.major = input("Enter Student major: ")

    def display_student(self):
        print("Student name: " + self.name)
        print("Student year: " + self.year)
        print("Student major: " + self.major)

    def assign_advisor(self, faculty):
        self.advisor = faculty


class Courses:
    def __init__(self):
        self.course = ""
        self.credits = ""
        self.department = ""
        self.faculty = None
        self.myStudentsList = []

    def create_course(self):
        self.course = input("Enter Course name: ")
        self.credits = input("Enter Course credits: ")
        self.department = input("Enter Course department: ")

    def display_course(self):
        print("Course name: " + self.course)
        print("Course credits: " + self.credits)
        print("Course department: " + self.department)

    def teaching_faculty(self, faculty):
        self.faculty = faculty

    def enrolled_students(self, student):
        self.myStudentsList.append(student)



myFacultyList = []
myStudentList = []
myCourseList = []





num_faculty = int(input("How many faculty members do you want to create? "))

for i in range(num_faculty):
    fac = Faculty()
    fac.create_faculty()
    myFacultyList.append(fac)

for x in myFacultyList:
    x.display_faculty()



num_students = int(input("How many students do you want to create? "))

for i in range(num_students):
    stu = Student()
    stu.create_student()
    myStudentList.append(stu)

for stu in myStudentList:
    faculty_id = input("Enter Faculty ID for " + stu.name + "'s advisor: ")

    for x in myFacultyList:
        if x.id == faculty_id:
            stu.assign_advisor(x)
            x.enroll_students(stu)

for x in myStudentList:
    x.display_student()




num_courses = int(input("How many courses do you want to create? "))

for i in range(num_courses):
    cou = Courses()
    cou.create_course()
    myCourseList.append(cou)

for cou in myCourseList:
    faculty_id = input("Enter Faculty ID for " + cou.course + ": ")

    for x in myFacultyList:
        if x.id == faculty_id:
            cou.teaching_faculty(x)




for cou in myCourseList:
    student_name = input("Enter Student name to enroll in " + cou.course + ": ")

    for x in myStudentList:
        if x.name == student_name:
            cou.enrolled_students(x)

for x in myCourseList:
    x.display_course()
