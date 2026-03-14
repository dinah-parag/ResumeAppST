import streamlit as st
import pandas as pd

skills = {
    "Python": 65,
    "JavaScript": 55,
    "SQL": 50,
    "HTML/CSS": 55,
    "Streamlit": 40,
    "Git/Github": 65
}

st.header("Habilidades Técnicas")
for skill, level in skills.items():
    st.markdown(f"**{skill}**")
    st.progress(level)
    df_skills = pd.DataFrame({
        "Habilidade": list(skills.keys()),
        "Proficiência": list(skills.values())
        })

st.divider()

st.bar_chart(df_skills.set_index("Habilidade"))