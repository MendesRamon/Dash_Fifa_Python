#importando bibliotecas para o projeto
import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


#carrega os dados ao abrir a página home
if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

 #usando Markdown para formatação de texto
st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")
 #usando Markdown para formatação de texto e o sidebar para escrever um texto ao lado da página
st.sidebar.markdown("Desenvolvido por [Ramon Mendes](https://github.com/MendesRamon) no curso da Asimov Academy")


btn = st.link_button(
    "Acesse os dados no Kaggle", 
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
    ) #botão para acessar os dados do site

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)

#streamlit run 1_🏠_home.py no terminal