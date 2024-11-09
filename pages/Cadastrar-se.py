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

# st.markdown("---")
linha()

st.markdown("<h1 style='text-align: center;'>Cadastro</h1>", unsafe_allow_html=True)
st.write("Informe os dados a seguir:")
username = st.text_input('Nome de Usuário')
password = st.text_input('Senha', type='password') 



#  centralizando botão login
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    botao_centro = st.button('Cadastrar')

if botao_centro:
    if username and password:
        success = dados.register(username, password)
        if success: 
            st.success('Cadastro realizado com sucesso!')
        else:
            st.error('Falha no cadastro. Tente novamente.')
    else:
        st.error("Por favor, preencha todos os campos!")
# st.markdown("---")
linha()

