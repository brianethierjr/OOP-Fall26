import streamlit as st
import mysql.connector

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
