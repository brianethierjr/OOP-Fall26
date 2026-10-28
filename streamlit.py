#Create my Resume

import streamlit as st
from PIL import Image

col1, col2 = st.columns((4,5))

with col1:
    st.title("Brian Ethier")
    st.header("Student, Data Analytics and Economics")

with col2:
    image = Image.open('BrianEthierJr.png')
    st.image(image, width=200)

st.title("Brian Ethier")
st.header("Undergraduate Student of Data Analytics and Economics")

st.markdown("About Me")
st.text("I am a student of OOP learning Python.")
st.text("Expected to graduate with Cum Laude Honors")
st.divider()

st.markdown("Qualifications")
st.text("BBA in Data Analytics and Economics (Expected)")
st.text("John Brown University")
st.divider()

st.markdown("Work Experience")
st.text("Summer Intern - Ashwood Grove Health Insurance")
st.text("Residential Crew Manager - Iron Jet LLC")
st.text("Manager - Quesadaddies")
st.text("Social Media and Recruitment Chair - JBU Rugby Club")
st.text("Campus Ambassador - Water for Good")
st.divider()

st.markdown("Projects")
st.text("INTEGRIS Health Project - Data Visualization")
st.text("Python Web Application - Object Oriented Programming")
st.text("Cross-Sectional and Time-Series Predictive Analytics Paper - Predicitve Analytics and Business Decision Modeling")
st.text("Quesadaddies Report 2024 Q3 - 2026 Q2 - Personal Business Project")
st.divider()

st.markdown("Contact Me")
st.text("ethierb@jbu.edu")
st.text("(555)555-555")
st.text("2000 W University St, Siloam Springs, AR, USA 72761")
st.button("Send Message")
st.divider()
