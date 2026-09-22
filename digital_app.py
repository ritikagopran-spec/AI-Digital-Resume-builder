import streamlit as st
from fpdf import FPDF
import os
from PIL import Image

st.set_page_config(page_title="Resume")
st.title("Resume")

with st.form("form"):
    name = st.text_input("Full Name", " ")
    addr1 = st.text_input("Address Line 1", " ")
    addr2 = st.text_input("Address Line 2", " ")
    email = st.text_input("Email", " ")
    contact = st.text_input("Contact No", " ")
    objective = st.text_area("Objective", " ")
    course = st.text_input("Course", " ")
    board = st.text_input("Board", " ")
    year = st.text_input("Passing Year", " ")
    perc = st.text_input("Percentage", " ")
    skills = st.text_area("Technical Skills", " ")
    hobbies = st.text_area("Hobbies", " ")
    exp = st.text_area("Experience", " ")
    photo = st.file_uploader("Upload Your Photo", type=["jpg","jpeg","png"])
    btn = st.form_submit_button("Generate")

if btn:
    photo_path = None
    if photo:
        # Photo ko sahi tarike se save karna
        img = Image.open(photo)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        photo_path = "my_photo.jpg"
        img.save(photo_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.rect(5, 5, 200, 287)

    # PHOTO - Fixed position
    if photo_path and os.path.exists(photo_path):
        try:
            pdf.image(photo_path, x=160, y=8, w=28, h=32)
        except Exception as e:
            st.error(f"Photo error: {e}")

    pdf.set_font("Arial","B",14)
    pdf.cell(0,15,"RESUME",ln=True,align="C")
    pdf.ln(2)

    pdf.set_font("Arial","B",11)
    pdf.cell(0,6,name,ln=True,x=12)
    pdf.set_font("Arial","",10)
    pdf.cell(100,5,addr1,ln=False,x=12)
    pdf.set_font("Arial","B",10)
    pdf.cell(0,5,f"E-mail: {email}",ln=True)
    pdf.set_font("Arial","",10)
    pdf.cell(100,5,addr2,ln=False,x=12)
    pdf.set_font("Arial","B",10)
    pdf.cell(0,5,f"Contact No.: {contact}",ln=True)
    pdf.ln(5)

    def grey_bar(title):
        pdf.set_fill_color(210,210,210)
        pdf.set_font("Arial","B",11)
        pdf.cell(186,7,f" {title}",ln=True,fill=True,x=12)
        pdf.ln(2)

    def content(text):
        pdf.set_font("Arial","",10)
        pdf.set_x(12)
        pdf.multi_cell(186,5,text)
        pdf.ln(3)

    grey_bar("Objective:")
    pdf.set_font("Arial","I",10)
    pdf.set_x(18)
    pdf.multi_cell(180,5,objective)
    pdf.ln(3)

    grey_bar("Educational Qualifications:")
    pdf.set_font("Arial","B",10)
    pdf.set_x(12)
    for h in ["Courses", "University/Board", "Passing Year", "Percentage"]:
        pdf.cell(46.5,7,h,border=1,align="C")
    pdf.ln()
    pdf.set_font("Arial","",10)
    pdf.set_x(12)
    for val in [course, board, year, perc]:
        pdf.cell(46.5,7,val,border=1,align="C")
    pdf.ln()
    pdf.ln(5)

    grey_bar("Technical Skills:")
    content(f"• {skills}")
    grey_bar("Hobbies:")
    content(f"• {hobbies}")
    grey_bar("Experience:")
    content(f"• {exp}")

    st.success("Resume ban gaya!")
    st.download_button("Download Resume", data=bytes(pdf.output()), file_name=f"{name}_Resume.pdf", mime="application/pdf")
