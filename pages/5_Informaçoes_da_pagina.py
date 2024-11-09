import streamlit as st

def app():
    background_image_url = "https://raw.githubusercontent.com/euandr/web_app_streamlit/refs/heads/main/Images_Background/infor_fundo.avif"
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
    st.title("Principais arquivos e programas utilizados na pagina!")
    st.markdown(
        """

        ### Arquivos e Programas:
        clique no botao abaixo se deseja vizualizar os arquivos do projeto:
        """
    )

    if 'visualizar' not in st.session_state: 
        st.session_state.visualizar = False
    if st.button("Visualizar"):
        st.session_state.visualizar = not st.session_state.visualizar

    if st.session_state.visualizar:

                    # Listar os arquivos e exibir seu conteúdo (opcional)
            arquivos = {
                "Login.py": "Login.py",
                "dados.py": "dados.py",
                "atualizar_senha.py": "pages/2_Atualizar_senha.py",
                "Cadastrar-se.py": "pages/1_Cadastrar-se.py",
                "Deletar_Usuario.py": "pages/3_Deletar_Usuario.py",
                "Lista_de_usuario.py": "pages/4_Lista_de_usuarios.py",
                "InformaÇões_da_pagina.py": "pages/5_Informaçoes_da_pagina.py"
            }

            for nome, caminho in arquivos.items():
                st.subheader(nome)
                with open(caminho, "r") as file:
                    conteudo = file.read()
                    st.code(conteudo, language='python')

            # Fornecer link para download do pacote ZIP
            st.markdown(
                """
                ### Download dos Arquivos:
                Você pode baixar todos os arquivos em formato ZIP clicando no botão abaixo:
                """
            )
            
            with open('app__.zip', 'rb') as file:
                st.download_button(
                    label="Baixar Arquivos ZIP",
                    data=file,
                    file_name='projeto.zip',
                    mime='application/zip'
                )
            


if __name__ == "__main__":
    app()
