# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('desenvolvimento.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem vindo, Igreja do Evangelho quadrangular!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Nós somos uma igreja que prega o evangelho do senhor!")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Jesus nos ama")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.subheader("------ **criado por Edvaldo e Nicole** -----")

menu = ["Texto_Colunas",
        "Texto_Markdown",
        "Inserir_Figura"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")
    
if choice == "Texto_Colunas":       
    st.subheader("Texto formatado em colunas")
    st.write("Veja a seguir uma opção de formatação em colunas")    
    cols01 = st.columns(2)    
    cols01[0].write('salmos 1')
    cols01[1].write('salmos 2')
elif choice == "salmos 3":
    st.subheader("salmos 4")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
