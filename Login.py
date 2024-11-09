
import streamlit as st
import dados




dados.criar_tabelas()
# Definir a configuração da página primeiro
st.set_page_config(
    page_title="Seja Bem-Vindo!",
    page_icon=":earth:"
)


def linha():
    st.markdown(
    """
    <style>
    .horizontal-line {
        border-top: 2px solid black;
        width: 100%;  /* Ajuste a largura conforme necessário */
        margin: 30px auto;  /* Centraliza a linha horizontal */
    }
    </style>
    <div class="horizontal-line"></div>
    """,
    unsafe_allow_html=True
)

background_image_url = "https://raw.githubusercontent.com/euandr/progr_Web/refs/heads/master/fundo_login.jpg"
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
# st.markdown("---")

linha()
st.markdown("<h1 style='text-align: center;'>LOGIN</h1>", unsafe_allow_html=True)
username = st.text_input('Nome de Usuário')
password = st.text_input('Senha', type='password') 



#  centralizando botão login
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    botao_centro = st.button('Entrar')
if botao_centro:
    if username and password:
        user = dados.login(username, password)
        if user: 
            st.success('Login realizado com sucesso!')
        else:
            st.error('Usuário inexistente ou os dados estão errados.')
    else:
        st.error("Por favor, preencha todos os campos!")
# st.markdown("---")
linha()