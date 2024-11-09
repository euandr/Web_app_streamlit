import streamlit as st
import dados

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

background_image_url = "https://raw.githubusercontent.com/euandr/progr_Web/refs/heads/master/cadastro_fundo.jpeg"
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
linha()

st.markdown("<h1 style='text-align: center;'>Deletar Usuario</h1>", unsafe_allow_html=True)
st.write("Informe o nome do usuario a ser deletado:")
username = st.text_input('Nome de Usuário')

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    botao_centro = st.button('Deletar')

if botao_centro:
    if username :
        success = dados.delete_user(username)
        if success:
            st.success('Usuario excluido com sucesso!')
        else:
            st.error('Usuario não encontrado! Tente novamente!')
    else:
        st.error("Por favor, preencha todos os campos!")
linha()