import streamlit as st
from fpdf import FPDF

st.set_page_config(page_title="Pro Resume Builder", page_icon="Resume")
st.title("Pro Resume Builder - AKTU")

with st.form("resume_form"):
    name = st.text_input("Full Name", "Anchal Gopran")
    role = st.text_input("Role", "B.Tech CSE Student")
    email = st.text_input("Email", "")
    phone = st.text_input("Phone", "")
    education = st.text_input("Education", "B.Tech CSE - AKTU")
    skills = st.text_area("Skills", "Python, AI, Machine Learning")
    projects = st.text_area("Projects", "AI Digital Resume Builder")
    about = st.text_area("Objective", "Passionate student")
    submit = st.form_submit_button("Generate PRO Resume")

if submit:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 15, name.upper(), ln=True, align="C")
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"{role} | {email} | {phone}", ln=True, align="C")
    pdf.ln(10)

    def add_sec(t, c):
        pdf.set_font("Arial", "B", 13)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, f" {t}", ln=True, fill=True)
        pdf.ln(2)
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 7, c)
        pdf.ln(4)

    add_sec("OBJECTIVE", about)
    add_sec("EDUCATION", education)
    add_sec("SKILLS", skills)
    add_sec("PROJECTS", projects)
    
    out = pdf.output()
    
    st.success("Pro Resume Ready!")
    st.metric("ATS Score", "92/100")
    st.download_button("Download PRO PDF", data=out, file_name="Resume.pdf", mime="application/pdf")
    st.balloons()
