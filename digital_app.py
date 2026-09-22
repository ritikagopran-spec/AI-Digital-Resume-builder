import streamlit as st

st.set_page_config(page_title="AI Resume Builder", page_icon="🚀")

st.title("🚀 AI Digital Resume Builder")
st.write("AKTU University - B.Tech Mini Project")

name = st.text_input("Your Name", "ANCHAL")
role = st.text_input("Role", "B.Tech CSE Student")
email = st.text_input("Email", "ritikagopran@gmail.com")
skills = st.text_area("Skills", "Python, AI, Web Dev")
about = st.text_area("About You", "I am a passionate student...")

if st.button("Generate Resume"):
    st.success("Resume Generated!")
    st.write(f"### {name}")
    st.write(f"**{role}**")
    st.write(f"Email: {email}")
    st.write(f"### Skills: {skills}")
    st.write(f"### About: {about}")
    st.balloons()

st.metric("ATS Score", "88/100")
