import streamlit as st
import pandas as pd

st.sidebar.title("Navegação")
section = st.sidebar.radio("Selecione uma seção:", ["Sobre", "Habilidades", "Experiência", "Educação", "Contato"])

skills = {
    "Python": 65,
    "JavaScript": 55,
    "SQL": 50,
    "HTML/CSS": 55,
    "Streamlit": 40,
    "Git/Github": 65
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

elif section == "Experiência":
    st.header("Experiência Profissional")
    
   # with st.expander("Estágio em Cicência de Dados | Prefeitura de Jaboatão dos Guararapes | Atual"):
    #    st.markdown("""
      #  *Março 2024 - Atual*  
       # - Coleta e limpeza de dados para projetos de análise;
        #- Desenvolvimento de modelos preditivos para melhorar a eficiência dos serviços públicos;
       # - Apresentação de resultados para stakeholders usando visualizações claras e concisas.
       # """)

    with st.expander("Professora de Inglês | **Aliança América** | ATUAL"):
        st.markdown("""
                    *Março 2023 - Atual*  
                    - Planejamento e execução de aulas de inglês para alunos de diferentes níveis;
                    - Desenvolvimento de materiais didáticos personalizados para atender às necessidades dos alunos.
                    """)

    with st.expander("Gerente de Dados | **Absolute Marketing** | 2020 - 2021"):
        st.markdown("""
                    *Março 2020 - 2021*  
                    - Coleta e limpeza de dados para empresa na área de educação financeira.
                    """)

    with st.expander("Apoio Secretarial | **IMPA (Instituto de Matemática Pura e Aplicada)** | 2018 - 2019"):
        st.markdown("""
                    *Agosto 2018 - Outubro de 2019*  
                    - Armazenamento e organização de documentos físicos e digitais;
                    - Suporte na comunicação interna e externa.
                    """)



elif section == "Educação":
    st.header("Formação Acadêmica")
    st.write("Tecnologia em Ciência de Dados | **Uninter** | Conclusão prevista para 2027")  
    st.write("Curso Data Science & Machine Learning | **Tera** | Concluído em 2022")
    st.write("Mestrado em Planejamento Perritorial | **UDESC** | Concluído em 2022")
    st.write("Bacharelado em Geografia | **UFPE** | Concluído em 2020")


elif section == "Contato":
    st.header("Entre em contato")
    st.write("Email: [dinahdantass@email.com](mailto:dinahdantass@email.com)")
    st.write("LinkedIn: [linkedin.com/in/dinah-r-dantas-384a26198/](https://www.linkedin.com/in/dinah-r-dantas-384a26198/)")
    st.write("GitHub: [github.com/dinah-parag](https://github.com/dinahparag)")
