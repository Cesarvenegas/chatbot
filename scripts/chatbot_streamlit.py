import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Descargar recursos de NLTK
nltk.download('punkt')
nltk.download('wordnet')

# Definir pares de preguntas y respuestas (puedes personalizarlos)
pares = [
    [
        r"hola|buenos días|buenas tardes",
        ["¡Hola! ¿En qué puedo ayudarte hoy?", "¡Buen día! ¿Cómo puedo asistirte?"]
    ],
    [
        r"¿Cuáles son los horarios de consulta?",
        ["Nuestro horario de consulta es de lunes a viernes, de 8:00 am a 6:00 pm."]
    ],
    [
        r"¿Cómo me preparo para un examen de sangre?",
        ["Debes ayunar durante 8 horas antes del examen y tomar suficiente agua."]
    ],
    [
        r"gracias|muchas gracias",
        ["¡De nada! Estoy aquí para ayudarte.", "¡No hay problema! ¿Necesitas algo más?"]
    ],
    [
        r"adiós|chao|hasta luego",
        ["¡Hasta luego! Que tengas un buen día.", "¡Adiós! Cuídate."]
    ]
]

# Crear el chatbot
chatbot = Chat(pares, reflections)

# Inyectar CSS personalizado para ocupar la pantalla completa y alinear a la derecha
st.markdown(
    """
    <style>
    .stApp {
        max-width: 100% !important;
        padding-left: 60% !important;
        padding-right: 2% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Configurar la interfaz de Streamlit
st.title("Chatbot de Asistencia Hospitalaria 🏥")
st.write("¡Hola! Soy un chatbot de asistencia hospitalaria. ¿En qué puedo ayudarte?")

# Inicializar el historial de chat en session_state
if "historial" not in st.session_state:
    st.session_state.historial = []

# Función para manejar la interacción con el chatbot
def enviar_mensaje():
    usuario_input = st.session_state.input_usuario  # Obtener la entrada del usuario
    respuesta = chatbot.respond(usuario_input)  # Obtener la respuesta del chatbot

    # Guardar la interacción en el historial
    st.session_state.historial.append(f"Tú: {usuario_input}")
    if respuesta:
        st.session_state.historial.append(f"Chatbot: {respuesta}")
    else:
        st.session_state.historial.append("Chatbot: Lo siento, no entendí tu pregunta. ¿Puedes reformularla?")

    # Limpiar el campo de entrada
    st.session_state.input_usuario = ""

# Mostrar el historial de chat
for mensaje in st.session_state.historial:
    st.write(mensaje)

# Campo de entrada y botón
st.text_input("Escribe tu mensaje:", key="input_usuario", on_change=enviar_mensaje)