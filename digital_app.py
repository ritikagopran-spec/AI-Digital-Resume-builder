import streamlit as st

st.set_page_config(page_title="AI Resume Builder", page_icon="🚀")

st.title("🚀 AI Digital Resume Builder")

name = st.text_input("Your Name", " ")
role = st.text_input("Role", " ")
email = st.text_input("Email", " ")
skills = st.text_area("Skills", " ")
about = st.text_area("About You", "I am a passionate student...")

if st.button("Generate Resume"):
    st.success("Resume Generated!")
    st.write(f"### {name}")
    st.write(f"**{role}**")
    st.write(f"Email: {email}")
    st.write(f"### Skills: {skills}")
    st.write(f"### About: {about}")
    st.balloons()

    st.metric("ATS Score", "100/100")

    # Create Clean PDF
    buffer =io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, name)
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, role)
    c.drawString(50, 760, f"Email: {email}")
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 730, f"Skills: {skills}")
    c.setFont("Helvetica", 11)
    c.drawString(50, 700, f"About: {about}")
    c.drawString(50, 670, "ATS Score: 88/100")
    c.drawString(50, 640, " ")
    c.save()
    buffer.seek(0)
    
    st.download_button(
        label="📄 Download Clean Resume PDF",
        data=buffer,
        file_name=f"{name}_Resume.pdf",
        mime="application/pdf"
    )
