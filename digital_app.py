import streamlit as st
from fpdf import FPDF
from PIL import Image
import os

st.set_page_config(page_title="Resume")
st.title("Resume")

with st.form("myform"):
    name = st.text_input("Name", "")
    addr1 = st.text_input("Address 1", "")
    addr2 = st.text_input("Address 2", "")
    email = st.text_input("Email", "")
    contact = st.text_input("Contact", "")
    objective = st.text_area("Objective", "")
    course = st.text_input("Course", "")
    board = st.text_input("Board", "")
    year = st.text_input("Year", "")
    perc = st.text_input("Percentage", "")
    skills = st.text_input("Skills", "")
    hobbies = st.text_input("Hobbies", "")
    exp = st.text_input("Experience", "")
    photo = st.file_uploader("Photo Upload", type=["jpg","jpeg","png"])
    submit = st.form_submit_button("Generate")

if submit:
    pdf = FPDF()
    pdf.add_page()
    pdf.rect(5,5,200,287)

    if photo:
        img = Image.open(photo)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        img.save("temp_photo.jpg")
        pdf.image("temp_photo.jpg", x=160, y=8, w=30, h=35)

    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"RESUME",ln=True,align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(0,6,name,ln=True)
    pdf.set_font("Arial","",10)
    pdf.set_x(12)
    pdf.cell(0,5,addr1,ln=True)
    pdf.set_x(12)
    pdf.cell(0,5,addr2,ln=True)
    pdf.set_x(12)
    pdf.cell(0,5,f"Email: {email} | Contact: {contact}",ln=True)
    pdf.ln(5)

    pdf.set_fill_color(200,200,200)
    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(186,7," Objective",ln=True,fill=True)
    pdf.set_x(12)
    pdf.set_font("Arial","",10)
    pdf.multi_cell(186,5,objective)
    pdf.ln(3)

    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(186,7," Education",ln=True,fill=True)
    pdf.set_x(12)
    pdf.set_font("Arial","B",10)
    pdf.cell(46,7,"Course",border=1)
    pdf.cell(46,7,"Board",border=1)
    pdf.cell(47,7,"Year",border=1)
    pdf.cell(47,7,"Per %",border=1,ln=True)
    pdf.set_x(12)
    pdf.set_font("Arial","",10)
    pdf.cell(46,7,course,border=1)
    pdf.cell(46,7,board,border=1)
    pdf.cell(47,7,year,border=1)
    pdf.cell(47,7,perc,border=1,ln=True)
    pdf.ln(5)

    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(186,7," Skills",ln=True,fill=True)
    pdf.set_x(12)
    pdf.set_font("Arial","",10)
    pdf.cell(0,6,skills,ln=True)
    pdf.ln(3)

    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(186,7," Hobbies",ln=True,fill=True)
    pdf.set_x(12)
    pdf.set_font("Arial","",10)
    pdf.cell(0,6,hobbies,ln=True)
    pdf.ln(3)

    pdf.set_font("Arial","B",11)
    pdf.set_x(12)
    pdf.cell(186,7," Experience",ln=True,fill=True)
    pdf.set_x(12)
    pdf.set_font("Arial","",10)
    pdf.cell(0,6,exp,ln=True)

    st.success("Done!")
    st.download_button("Download PDF", bytes(pdf.output()), file_name="resume.pdf")
