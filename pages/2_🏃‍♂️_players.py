import streamlit as st

#configurando a tela
st.set_page_config(
    page_title="Players",
    page_icon="🏃‍♂️",
    layout="wide"
)

df_data = st.session_state['data'].sort_values(by="Overall", ascending=False) #trazendo os dados da página principal


clubes = df_data["Club"].value_counts().index #definindo valores únicos para por na cx de seleção
club = st.sidebar.selectbox("Clube", clubes) #criando caixa de seleção

df_players = df_data[(df_data["Club"] == club)] #usando filtro padrão do python

players = df_players["Name"].value_counts().index #definindo valores únicos para por na cx de seleção
player = st.sidebar.selectbox("Jogador", players) #criando caixa de seleção

player_stats = df_data[df_data["Name"] == player].iloc[0] #dado selecionado

st.image(player_stats["Photo"]) #plotando imagem da caixa de seleção
st.title(player_stats["Name"])  #exibindo o nome do jogador

st.markdown(f"**Clube:** {player_stats['Club']}") #f' indica que o texto receberá variáveis no código
st.markdown(f"**Posição:** {player_stats['Position']}") 

col1, col2, col3, col4 = st.columns(4) #criando colunas/qtde de posições lado a lado

col1.markdown(f"**Idade:** {player_stats['Age']}") #plotando idade
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}") #plotando altura - transformado em metros
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}") #plotando peso - transformado em kg

st.divider() #criando uma linha para separar as informações

st.subheader(f"Overall {player_stats['Overall']}") #subtitulo - o overall vai de 0 à 100
st.progress(int(player_stats['Overall']))  #barra de progresso


col1, col2, col3, col4 = st.columns(4) #criando colunas/qtde de posições lado a lado


#metric recebe labels, value e  delta 
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisão", value=f"£ {player_stats['Release Clause(£)']:,}")