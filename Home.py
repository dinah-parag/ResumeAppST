import streamlit as st
import pandas as pd

st.title("Dinah Dantas") 
st.subheader("Estudante de Ciência de Dados")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Sobre", "Habilidades", "Experiência", "Educação", "Projetos", "Contato"])



with tab1:
    st.subheader("-- Sobre --")
    st.markdown("""
                Com prática com SQL, Python, CSS, HTML e Java, aprender novas habilidadess, resolução de problemas e organização são um grande motivadores para mim, assim como colaborar com equipes diversas para criar soluções inovadoras.
""")

skills = {
    "Python": 65,
    "JavaScript": 55,
    "SQL": 50,
    "HTML/CSS": 55,
    "Streamlit": 40,
    "Git/Github": 65
}

with tab2:
    st.subheader("-- Habilidades Técnicas --")
    for skill, level in skills.items():
        st.markdown(f"**{skill}**")
        st.progress(level)
        df_skills = pd.DataFrame({
            "Habilidade": list(skills.keys()),
            "Proficiência": list(skills.values())
        })

with tab3:
    st.subheader("-- Experiência Profissional --")
    with st.expander("Estágio em Cicência de Dados | Prefeitura de Jaboatão dos Guararapes | ATUAL"):
        st.markdown("""
                    *Março 2024 - Atual*  
                    - Coleta e limpeza de dados para projetos de análise;
                    - Desenvolvimento de modelos preditivos para melhorar a eficiência dos serviços públicos;
                    - Apresentação de resultados para stakeholders usando visualizações claras e concisas.
                    """)

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

with tab4:
    st.subheader("-- Formação Acadêmica --")
    st.write("Tecnologia em Ciência de Dados | **Uninter** | Conclusão prevista para 2027")  
    st.write("Curso Data Science & Machine Learning | **Tera** | Concluído em 2022")
    st.write("Mestrado em Planejamento Perritorial | **UDESC** | Concluído em 2022")
    st.write("Bacharelado em Geografia | **UFPE** | Concluído em 2020")

with tab5:
    st.subheader("-- Projetos --")
#    st.markdown("""
#                **Análise de Dados de Vendas**: Projeto de análise de dados de vendas usando Python e SQL para identificar tendências e oportunidades de crescimento.
#                """)
#    st.markdown("""
#                **Dashboard de Visualização de Dados**: Desenvolvimento de um dashboard interativo usando Streamlit para visualizar dados de marketing e vendas.
#                """)

with tab6:
    st.header("Entre em contato")
    st.write("Email: [dinahdantass@email.com](mailto:dinahdantass@email.com)")
    st.write("LinkedIn: [linkedin.com/in/dinah-r-dantas-384a26198/](https://www.linkedin.com/in/dinah-r-dantas-384a26198/)")
    st.write("GitHub: [github.com/dinah-parag](https://github.com/dinahparag)")