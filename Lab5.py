# Define the Classes as given below:
# Student_Master (stu_id, stu_name, stu_major, stu_courses, stu_cgpa)
# Faculty_Master (fac_id, fac_name, fac_department, fac_teaches_courses)

# Do the following functionalities:
# 1. Write a menu-driven program or a GUI based program.
# 2. Create at least 5 objects for Student_Master and Faculty_Master classes.
# 3. Create two database tables for these two classes.
# 4. Write the values of the students and faculty objects in the Database tables.
# 5. Read back from the database, and display all the details of the students and faculty.

# http://localhost/phpmyadmin5.2.3/

import streamlit as st
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="brian_ethier_lab5"
)

cursor = db.cursor()

#  Student Table

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        stu_id INT PRIMARY KEY,
        stu_name VARCHAR(100),
        stu_major VARCHAR(100),
        stu_courses VARCHAR(100),
        stu_cgpa DECIMAL(4,2)
    )
""")

print("Student table created successfully!")

# Faculty Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Faculty (
        fac_id INT PRIMARY KEY,
        fac_name VARCHAR(100),
        fac_department VARCHAR(100),
        fac_teaches_courses VARCHAR(100)
    )
""")

print("Faculty table created successfully!")

class Student:
    def __init__(self):
        self.studID = 0
        self.studName = ""
        self.studMajor = ""
        self.studCourses = ""
        self.studCumGPA = 0.0

    def EnterInfoStudScr(self):
        if not self.studID or not self.studName or not self.studMajor or not self.studCourses:
            st.error("Please enter all required information")
            return

        try:
            cursor.execute("""
                        INSERT INTO Students 
                        (stu_id, stu_name, stu_major, stu_courses, stu_cgpa)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (
                self.studID,
                self.studName,
                self.studMajor,
                self.studCourses,
                self.studCumGPA
            ))

            db.commit()
            st.success("Student information successfully inserted!")

        except mysql.connector.Error as error:
            db.rollback()
            st.error(f"Database error: {error}")

    def UpdateStudScr(self):

        try:
            cursor.execute("""
                    UPDATE Students 
                    SET stu_name = %s,
                        stu_major = %s, 
                        stu_courses = %s, 
                        stu_cgpa = %s
                    WHERE stu_id = %s
                """, (
                self.studName,
                self.studMajor,
                self.studCourses,
                self.studCumGPA,
                self.studID
            ))

            db.commit()

            if cursor.rowcount > 0:
                st.success("Student information updated!")
            else:
                st.warning("Student not found or no changes made.")

        except mysql.connector.Error as error:
            db.rollback()
            st.error(f"Database error: {error}")

    def DeleteStudScr(self):

        cursor.execute("""
                    DELETE FROM Students 
                    WHERE stu_id = %s
                """, (self.studID,))
        db.commit()

        if cursor.rowcount > 0:
            st.success("Student information deleted!")
        else:
            st.warning("Student not found.")

    def printStudScr(self):

        cursor.execute("SELECT * FROM Students")

        records = cursor.fetchall()

        st.write("Student List")

        st.dataframe(
            records,
            use_container_width=True
        )

class Faculty:
    def __init__(self):
        self.facID = 0
        self.facName = ""
        self.facDept = ""
        self.facCourses = ""

    def EnterInfoFacScr(self):
        if not self.facID or not self.facName or not self.facDept or not self.facCourses:
            st.error("Please enter all required information")
            return

        try:
            cursor.execute("""
                                INSERT INTO Faculty
                                (fac_id, fac_name, fac_department, fac_teaches_courses)
                                VALUES (%s, %s, %s, %s)
                            """, (
                self.facID,
                self.facName,
                self.facDept,
                self.facCourses
            ))

            db.commit()
            st.success("Faculty information entered!")

        except mysql.connector.Error as error:
            db.rollback()
            st.error(f"Database error: {error}")

    def UpdateFacScr(self):
        cursor.execute("""
                            UPDATE Faculty
                            SET fac_name = %s,
                                fac_department = %s,
                                fac_teaches_courses = %s
                            WHERE fac_id = %s
                        """, (
            self.facName,
            self.facDept,
            self.facCourses,
            self.facID
        ))

        db.commit()

        if cursor.rowcount > 0:
            st.success("Faculty information updated!")
        else:
            st.warning("Faculty not found.")

    def DeleteFacScr(self):
        cursor.execute("""
                            DELETE FROM Faculty
                            WHERE fac_id = %s
                        """, (self.facID,))

        db.commit()

        if cursor.rowcount > 0:
            st.success("Faculty deleted!")
        else:
            st.warning("Faculty not found.")


    def printFacListScr(self):

        cursor.execute("SELECT * FROM Faculty")

        records = cursor.fetchall()

        st.write("Faculty List")

        st.dataframe(
            records,
            use_container_width=True
        )

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"


if st.session_state.screen == "welcome":
    st.title("Welcome!")
    st.write("Are you a faculty or student?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Faculty", use_container_width=True):
            st.session_state.screen = "faculty"
            st.rerun()

    with col2:
        if st.button("Student", use_container_width=True):
            st.session_state.screen = "student"
            st.rerun()


elif st.session_state.screen == "student":

    st.markdown(
        '<div class="student-title">Student</div>',
        unsafe_allow_html=True
    )

    st.write("Student Management System")

    action = st.selectbox(
        "Choose an action",
        ["Add Student", "Edit Student", "Remove Student", "Display Students"]
    )

    # Add Student

    if action == "Add Student":

        st.subheader("Enter Student Information")

        studID = st.number_input(
            "Student ID",
            min_value=1,
            step=1,
            key="add_stud_id"
        )

        studName = st.text_input(
            "Student Name",
            key="add_stud_name"
        )

        studMajor = st.text_input(
            "Student Major",
            key="add_stud_major"
        )

        studCourses = st.text_input(
            "Student Courses",
            key="add_stud_courses"
        )

        studCumGPA = st.number_input(
            "Student Cumulative GPA",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="add_stud_gpa"
        )

        if st.button("Add Student"):

            student = Student()

            student.studID = studID
            student.studName = studName
            student.studMajor = studMajor
            student.studCourses = studCourses
            student.studCumGPA = studCumGPA

            student.EnterInfoStudScr()

    # Edit student
    elif action == "Edit Student":

        st.subheader("Edit Student Information")

        studID = st.number_input(
            "Enter Student ID to Edit",
            min_value=1,
            step=1,
            key="edit_stud_id"
        )

        studName = st.text_input(
            "Updated Student Name",
            key="edit_stud_name"
        )

        studMajor = st.text_input(
            "Updated Student Major",
            key="edit_stud_major"
        )

        studCourses = st.text_input(
            "Updated Student Courses",
            key="edit_stud_courses"
        )

        studCumGPA = st.number_input(
            "Updated Student Cumulative GPA",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            key="edit_stud_gpa"
        )

        if st.button("Update Student"):

            student = Student()

            student.studID = studID
            student.studName = studName
            student.studMajor = studMajor
            student.studCourses = studCourses
            student.studCumGPA = studCumGPA

            student.UpdateStudScr()


    # Remove student
    elif action == "Remove Student":

        st.subheader("Remove Student")

        studID = st.number_input(
            "Enter Student ID to Remove",
            min_value=1,
            step=1,
            key="delete_stud_id"
        )

        if st.button("Delete Student"):

            student = Student()

            student.studID = studID

            student.DeleteStudScr()



    # Display Student
    elif action == "Display Students":

        st.subheader("Student List")

        student = Student()

        student.printStudScr()


    # Back to home
    st.divider()

    if st.button("Back to Welcome", key="student_back"):
        st.session_state.screen = "welcome"
        st.rerun()




elif st.session_state.screen == "faculty":

    st.markdown(
        '<div class="faculty-title">Faculty</div>',
        unsafe_allow_html=True
    )

    st.write("Faculty")

    action = st.selectbox(
        "Choose from the following:",
        ["Add Faculty", "Edit Faculty", "Remove Faculty", "Display Faculty"]
    )

    # Add faculty
    if action == "Add Faculty":

        st.subheader("Enter Faculty Information")

        facId = st.number_input(
            "Faculty ID",
            min_value=1,
            step=1,
            key="add_fac_id"
        )

        facName = st.text_input(
            "Faculty Name",
            key="add_fac_name"
        )

        facDept = st.text_input(
            "Faculty Department",
            key="add_fac_dept"
        )

        facCourses = st.text_input(
            "Faculty Courses",
            key="add_fac_courses"
        )

        if st.button("Add Faculty"):
            faculty = Faculty()

            faculty.facID = facId
            faculty.facName = facName
            faculty.facDept = facDept
            faculty.facCourses = facCourses

            faculty.EnterInfoFacScr()


    # Edit Faculty
    elif action == "Edit Faculty":

        st.subheader("Edit Faculty Information")

        facId = st.number_input(
            "Enter Faculty ID to Edit",
            min_value=1,
            step=1,
            key="edit_fac_id"
        )

        facName = st.text_input(
            "Updated Faculty Name",
            key="edit_fac_name"
        )

        facDept = st.text_input(
            "Updated Faculty Department",
            key="edit_fac_dept"
        )

        facCourses = st.text_input(
            "Updated Faculty Courses",
            key="edit_fac_courses"
        )

        if st.button("Update Faculty"):
            faculty = Faculty()

            faculty.facID = facId
            faculty.facName = facName
            faculty.facDept = facDept
            faculty.facCourses = facCourses

            faculty.UpdateFacScr()

    # Remove Faculty
    elif action == "Remove Faculty":

        st.subheader("Remove Faculty")

        facId = st.number_input(
            "Enter Faculty ID to Remove",
            min_value=1,
            step=1,
            key="delete_fac_id"
        )

        if st.button("Delete Faculty"):
            faculty = Faculty()

            faculty.facID = facId

            faculty.DeleteFacScr()

    # Display Faculty
    elif action == "Display Faculty":

        st.subheader("Faculty List")

        faculty = Faculty()

        faculty.printFacListScr()

    # Back to home

    st.divider()

    if st.button("Back to Welcome", key="faculty_back"):
        st.session_state.screen = "welcome"
        st.rerun()

