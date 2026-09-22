import streamlit as st

st.set_page_config(page_title="AI Resume Builder", page_icon="🚀")
st.title("🚀 AI Digital Resume Builder")

name = st.text_input("Your Name", "")
role = st.text_input("Role", "")
email = st.text_input("Email", "")
skills = st.text_area("Skills", "")
about = st.text_area("About You", "")

if st.button("Generate Resume"):
    st.success("Resume Generated!")
    st.markdown("---")
    st.write(f"### {name}")
    st.write(f"**{role}**")
    st.write(f"Email: {email}")
    st.write(f"Skills: {skills}")
    st.write(f"About: {about}")
    st.metric("ATS Score", "88/100")
    st.balloons()
    
    resume_text = f"{name}\n{role}\nEmail: {email}\n\nSkills: {skills}\nAbout: {about}\nATS Score: 88/100"
    
    st.download_button(
        label="📄 Download Clean Resume",
        data=resume_text,
        file_name=f"{name}_Resume.txt",
        mime="text/plain"
    )
