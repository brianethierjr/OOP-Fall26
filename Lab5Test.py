# Define the Classes as given below:
# Student_Master (stu_id, stu_name, stu_major, stu_courses, stu_cgpa)
# Faculty_Master (fac_id, fac_name, fac_department, fac_teaches_courses)

# Do the following functionalities:
# 1. Write a menu-driven program or a GUI based program.
# 2. Create at least 5 objects for Student_Master and Faculty_Master classes.
# 3. Create two database tables for these two classes.
# 4. Write the values of the students and faculty objects in the Database tables.
# 5. Read back from the database, and display all the details of the students and faculty.

import streamlit as st
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="StudentDB"
)
cursor = db.cursor()


# Student Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Student_Master (
    stu_id INT PRIMARY KEY,
    stu_name VARCHAR(50),
    stu_major VARCHAR(50),
    stu_courses VARCHAR(255),
    stu_cgpa FLOAT
)
""")

print("Student table created successfully!")

# Faculty Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Faculty_Master (
    fac_id INT PRIMARY KEY,
    fac_name VARCHAR(50),
    fac_department VARCHAR(50),
    fac_teaches_courses VARCHAR(255)
)
""")

print("Faculty table created successfully!")




class Student:
    def __init__(self):
        self.studID = 0
        self.studName = ""
        self.studMajor = ""
        self.studCourses = ""
        self.studCumGPA = ""

    def EnterInfoStudScr():
        if not studID or not studName or not studMajor or not studCourses:
            st.error("Please enter all required information")
            return

        st.success("Student information entered")

    def printStudListScr():


class Faculty:
        def __init__(self):
            self.facID = 0
            self.facName = ""
            self.facDept = ""
            self.facCourses = ""

        def EnterInfoFacScr():
            if not facID or not studName or not studMajor or not studCourses:
                st.error("Please enter all required information")
                return
            st.success("Faculty information entered")

        def printFacListScr():

students = []
faculty = []

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"


if st.session_state.screen == "welcome":
    st.title("Welcome!")
    st.write("Are you a faculty or student?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Faculty"):
            st.session_state.screen = "faculty"
            st.rerun()

    with col2:
        if st.button("Student"):
            st.session_state.screen = "student"
            st.rerun()

elif st.session_state.screen == "faculty":
    st.markdown(
        '<div class="faculty-title">Faculty</div>',
        unsafe_allow_html=True
    )
    facId = st.number_input("Faculty ID")
    facName = st.text_input("Faculty Name")
    facDept = st.text_input("Faculty Department")
    facCourses = st.text_input("Faculty Courses")

    if st.button("Faculty")

elif st.session_state.screen == "student":
    st.markdown(
        '<div class="student-title">Student</div>',
        unsafe_allow_html=True
    )

    studID = st.number_input("Student ID")
    studName = st.text_input("Student Name")
    studCourses = st.text_input("Student Courses")
    studMajor = st.text_input("Student Major")
    studCumGPA = st.text_input("Student Cumulative GPA")
