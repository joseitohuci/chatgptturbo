import streamlit
import os 
import openai
from dotenv import load_dotenv

emoji_robo = "🤖"
emoji_user = "🙋"

#load_dotenv()  # carrega as variáveis de ambiente do arquivo .env
#openai.api_key = os.getenv('SENHA_OPEN_AI')

openai.api_key = ["ClaveOPENAI"]

streamlit.title(f'{emoji_robo} Pergunte ao Jarvis')
streamlit.write('***')

if 'hst_conversa' not in streamlit.session_state:
    streamlit.session_state.hst_conversa = []
pregunta = streamlit.text_input('Digite sua pregunta: ')

col1, col2 = streamlit.columns(2)

with col1:
    btn_enviar = streamlit.button("Enviar Pregunta")
with col2:
    btn_limpar = streamlit.button("Limpar Conversacion")
if btn_enviar: 
    streamlit.session_state.hst_conversa.append({"role": "user", "content": pregunta})
    retorno_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = streamlit.session_state.hst_conversa,
        max_tokens = 500,
        n=1
    )
    streamlit.session_state.hst_conversa.append(
        {"role": "assistant", 
         "content": retorno_openai['choices'][0]['message']['content']})
if btn_limpar: # boton "Limpar Conversa"
    streamlit.session_state.hst_conversa = [] # redefine a lista de histórico de conversa para vazia
    pregunta = '' # redefine o valor do input para uma string vazia
if len(streamlit.session_state.hst_conversa) > 0:
    for i in range(len(streamlit.session_state.hst_conversa)):
        if i % 2 == 0:
            with streamlit.container():
                streamlit.write(f"{emoji_user} Tu: " + streamlit.session_state.hst_conversa[i]['content'])
        else:
            with streamlit.container():
                streamlit.write(f"{emoji_robo} Respuesta de IA: " + streamlit.session_state.hst_conversa[i]['content'])
#informaciones del autor
streamlit.sidebar.markdown("<h3 style='text-align: center; font-size: 20px; color: Red'>By ImJoseitoh &reg - 2023</h3>", unsafe_allow_html=True)
