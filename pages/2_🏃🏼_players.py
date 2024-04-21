import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)
df_data = st.session_state["data"] #dataset


clubes = df_data["Club"].value_counts().index #definindo lista de clubes
club = st.sidebar.selectbox("Clube", clubes)  #criando o select box com o nome Clube e dados clubes

df_players = df_data[(df_data["Club"] == club)]    #filtrando tabela pelo clube selecionado
players = df_players["Name"].value_counts().index  #definindo lista de jodgadores
player = st.sidebar.selectbox("Jogador", players)  #criando o select box pelo nome do jogador

player_stats = df_data[df_data["Name"] == player].iloc[0] #filtrando tabela pelo nome do jogador

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")