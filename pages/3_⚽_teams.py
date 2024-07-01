import streamlit as st

#configurando a tela
st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state['data'].sort_values(by="Overall", ascending=False) #trazendo os dados da página principal

clubes = df_data["Club"].value_counts().index #definindo valores únicos para por na cx de seleção
club = st.sidebar.selectbox("Clube", clubes) #criando caixa de seleção

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name") #usando filtro padrão do python - name setado para não mostrar números

st.image(df_filtered.iloc[0] ["Club Logo"]) #imagem do clube
st.markdown(f"## {club}") #nome do club

#definindo as colunas que serão plotadas
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", 
           "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d" ,min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%f" ,min_value=0, max_value=df_filtered["Wage(£)"].max()
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country")  
             }
        )
