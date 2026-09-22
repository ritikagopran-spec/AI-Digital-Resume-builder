import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Classic Resume with Photo")
st.title("Classic Resume - With Photo")

with st.form("form"):
    name = st.text_input("Full Name", "Anchal Gopran")
    addr1 = st.text_input("Address Line 1", "Dev Gopran, Mathura")
    addr2 = st.text_input("Address Line 2", "Uttar Pradesh - 281001")
    email = st.text_input("Email", "anchal@gmail.com")
    contact = st.text_input("Contact No", "6789054321")
    objective = st.text_area("Objective", "I want to excel in this field with hard work, perseverance and dedication.")
    course = st.text_input("Course", "B.Tech CSE")
    board = st.text_input("Board", "AKTU")
    year = st.text_input("Passing Year", "2028")
    perc = st.text_input("Percentage", "85%")
    skills = st.text_area("Technical Skills", "Computer: MS-CIT, Python, Typing: English 40, Hindi 30")
    hobbies = st.text_area("Hobbies", "Reading Books, Travelling, Coding")
    exp = st.text_area("Experience", "Fresher / AI Resume Builder Project")
    photo = st.file_uploader("Upload Your Photo", type=["jpg","jpeg","png"])
    btn = st.form_submit_button("Generate PDF with Photo")

if btn:
    pdf = FPDF()
    pdf.add_page()
    pdf.rect(5, 5, 200, 287)

    if photo:
        with open("temp.jpg","wb") as f:
            f.write(photo.getbuffer())
        pdf.image("temp.jpg", x=160, y=8, w=28, h=32)

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
    col_w = [46.5, 46.5, 46.5, 46.5]
    headers = ["Courses", "University/Board", "Passing Year", "Percentage"]
    for i,h in enumerate(headers):
        pdf.cell(col_w[i],7,h,border=1,align="C")
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

    st.success("Photo wala resume ready!")
    st.download_button("Download Resume", data=bytes(pdf.output()), file_name=f"{name}_Resume.pdf", mime="application/pdf")
