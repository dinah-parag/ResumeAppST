import streamlit as st
import pandas as pd

st.sidebar.title("Navegação")
section = st.sidebar.radio("Selecione uma seção:", ["Sobre", "Habilidades", "Experiência", "Educação", "Contato"])

skills = {
    "Python": 65,
    "JavaScript": 50,
    "SQL": 50,
    "Streamlit": 40,
    "Análise de Dados": 70,
}

st.title("Dinah Dantas") 
st.subheader("Estudante de Ciência de Dados")

if section == "Sobre":

    st.markdown("""
    Com prática com SQL, Python, CSS, HTML e Java, 
    aprender novas habilidadess, resolução de problemas e organização são um grande motivadores para mim, assim como colaborar com equipes diversas para criar soluções inovadoras.
    """)

elif section == "Habilidades":
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

#elif section == "Experiência":

#elif section == "Educação":

#elif section == "Contato":