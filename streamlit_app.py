import streamlit
import os 
import openai
import json

emoji_robo = "🤖"
emoji_user = "🙋"

openai.api_key = streamlit.secrets["ClaveAI"]

streamlit.title(f'{emoji_robo} Pergunte a Wall-E(BETA🫤)')
streamlit.write('***')

if 'hst_conversa' not in streamlit.session_state:
    streamlit.session_state.hst_conversa = []
pregunta = streamlit.text_input('Digite su pregunta: ')

col1, col2 = streamlit.columns(2)

with col1:
    btn_enviar = streamlit.button("Enviar Mensaje")    
with col2:
    btn_limpar = streamlit.button("Limpar Chat")

def enviar_mensaje():
    global pregunta
    streamlit.session_state.hst_conversa.append({"role": "user", "content": pregunta})
    retorno_openai = openai.ChatCompletion.create(
        model = "text-davinci-003",    
        messages = streamlit.session_state.hst_conversa,
	max_tokens=1000,
	n = 1
    )
    streamlit.session_state.hst_conversa.append(
        {"role": "assistant", 
         "content": retorno_openai['choices'][0]['message']['content']})
    pregunta = ""  # Limpiar el cuadro de texto

def limpiar_chat():
    global pregunta
    streamlit.session_state.hst_conversa = []  # Limpiar el historial de conversación
    pregunta = ""  # Limpiar el cuadro de texto

if btn_enviar: 
    enviar_mensaje()

if btn_limpar: 
    limpiar_chat()

if len(streamlit.session_state.hst_conversa) > 0:
    for i in range(len(streamlit.session_state.hst_conversa)):
        if i % 2 == 0:
            with streamlit.container():
                streamlit.write(f"{emoji_user} Tu: " + streamlit.session_state.hst_conversa[i]['content'])
        else:
            with streamlit.container():
                streamlit.write(f"{emoji_robo} Wall-E: " + streamlit.session_state.hst_conversa[i]['content'])
                
#informaciones del autor
streamlit.sidebar.markdown("<h3 style='text-align: center; font-size: 20px; color: Red'>By ImJoseitoh &reg - 2023</h3><p><h2><center>+5356960902</h2></p>", unsafe_allow_html=True)
