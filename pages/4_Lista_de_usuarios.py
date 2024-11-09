import streamlit as st
import pandas as pd
import dados




background_image_url = "https://raw.githubusercontent.com/euandr/web_app_streamlit/refs/heads/main/Images_Background/fundo_dados.avif"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Lista de Usúarios cadastrados:")
users = dados.query_users()
if users:
    df = pd.DataFrame(users, columns=["Nome de Usuário", "Senha(Criptografada)"])  # Ajuste as colunas conforme necessário
    st.dataframe(df)
else:
    st.write("Nenhum usuário encontrado.")