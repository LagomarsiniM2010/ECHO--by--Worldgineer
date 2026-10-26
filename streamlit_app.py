import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import base64

st.set_page_config(page_title="ECHO", page_icon="💙", layout="wide")

# Colores de ECHO ayuda de IA
st.markdown("""
<style>

/* Menu lateral */
[data-testid="stSidebar"] { background-color: #E8F1F5; }

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p { color: #174A73; font-size: 25px; font-weight: bold; }

[data-testid="stSidebar"] [data-baseweb="select"] > div { background-color: #FFFFFF; border: 2px solid #174A73; border-radius: 12px; min-height: 62px; }
[data-testid="stSidebar"] [data-baseweb="select"] span { color: #174A73; font-size: 24px; }

/* Fondo */
.stApp { background-color: #FFF8ED; color: #202B33; }

/* Letras generales */
.stApp p { font-size: 25px; line-height: 1.5; }

/* Titulos */
.stApp h1 { font-size: 55px; color: #174A73 !important; }
.stApp h2 { font-size: 42px; color: #174A73 !important; }
.stApp h3 { font-size: 34px; color: #174A73 !important; }

/* Recuadros */
[data-testid="stAlert"] p { font-size: 25px; }

/* Campos de configuracion */
.stTextInput label { font-size: 24px; font-weight: bold; }
.stTextInput input { font-size: 25px; min-height: 62px; }

/* Numeros del historial */
[data-testid="stMetricValue"] { font-size: 44px; }

/* Textos pequeños */
.stApp [data-testid="stCaptionContainer"] p { font-size: 20px; }

/* Botones normales */
.stButton > button { background-color: #174A73; color: white; font-size: 25px; font-weight: bold; min-height: 72px; border-radius: 14px; width: 100%; }
.stButton > button:hover { background-color: #176B55; color: white; }

/* Colores de asistencia */
.st-key-caida button { background-color: #A42424; border: 2px solid #A42424; }
.st-key-agua button { background-color: #174A73; border: 2px solid #174A73; }
.st-key-comida button { background-color: #176B55; border: 2px solid #176B55; }
.st-key-miedo button { background-color: #A3450B; border: 2px solid #A3450B; }
.st-key-ayuda button { background-color: #8C3268; border: 2px solid #8C3268; }
.st-key-bano button { background-color: #315A91; border: 2px solid #315A91; }

/* Botones de asistencia */
.st-key-caida button,
.st-key-agua button,
.st-key-comida button,
.st-key-miedo button,
.st-key-ayuda button,
.st-key-bano button { color: white; font-size: 29px; font-weight: bold; min-height: 88px; border-radius: 14px; width: 100%; padding: 12px; }

/* Color cuando pasamos el mouse */
.st-key-caida button:hover,
.st-key-agua button:hover,
.st-key-comida button:hover,
.st-key-miedo button:hover,
.st-key-ayuda button:hover,
.st-key-bano button:hover { color: white; filter: brightness(0.85); }

/* Para navegar con el teclado */
.stButton > button:focus-visible { outline: 4px solid #D38A28; outline-offset: 3px; }

</style>
""", unsafe_allow_html=True)

# Cerrar diseño de UX


# Poner imagen en base64
with open("ECHO.png", "rb") as imagen:
    logo = base64.b64encode(imagen.read()).decode()

# LOGO
st.markdown(f"""
<div style="display: flex; align-items: center; gap: 5px;">
    <img src="data:image/png;base64,{logo}" width="200">
    <h1 style="font-size: 90px;">ECHO</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<p style="margin-top: -80px; margin-left: 50px; font-size: 26px;">Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)


# Guardamos la informacion
if "historial" not in st.session_state:
    st.session_state.historial = []

if "nombre" not in st.session_state:
    st.session_state.nombre = "Maria N. Burgos"

if "lugar" not in st.session_state:
    st.session_state.lugar = "Home For Elderly"

if "familiar" not in st.session_state:
    st.session_state.familiar = "Sebastian Lagomarsini"

if "telefono" not in st.session_state:
    st.session_state.telefono = "939-308-4067"


# Menu principal
menu = st.sidebar.selectbox("Menu principal", ["Inicio", "Asistencia", "Orientación", "Encargado", "Configuración"])


# Inicio
if menu == "Inicio":
    st.header("Bienvenido a ECHO")
    st.write("Aquí puedes encontrar información sobre cómo utilizar la aplicación y sus funcionalidades.")

    st.divider()
    st.markdown('<p style="text-align: center; font-size: 18px; color: #174A73;">© 2026 Worldgineer. Todos los derechos reservados.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 16px; color: #52616B; margin-top: -20px;">ECHO | Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)


# Asistencia
elif menu == "Asistencia":
    st.header("Asistencia")
    st.write("¿Qué necesitas?")

    # Primera fila
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        if st.button("Me caí", key="caida", use_container_width=True):
            st.success("Me caí y necesito ayuda")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Me caí")

    with col2:
        if st.button("Tengo sed", key="agua", use_container_width=True):
            st.success("Necesito agua")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Tengo sed")

    with col3:
        if st.button("Tengo hambre", key="comida", use_container_width=True):
            st.success("Necesito comida")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Tengo hambre")

    # Segunda fila
    col4, col5, col6 = st.columns(3, gap="medium")

    with col4:
        if st.button("Tengo miedo", key="miedo", use_container_width=True):
            st.success("Necesito compañía")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Tengo miedo")

    with col5:
        if st.button("Necesito ayuda", key="ayuda", use_container_width=True):
            st.success("Necesito alguien que me ayude")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Necesito ayuda")

    with col6:
        if st.button("Tengo que ir al baño", key="bano", use_container_width=True):
            st.success("Necesito ir al baño")
            hora = datetime.now(ZoneInfo("America/Puerto_Rico")).strftime("%I:%M %p")
            st.session_state.historial.append(hora + " - Tengo que ir al baño")

    st.divider()
    st.markdown('<p style="text-align: center; font-size: 18px; color: #174A73;">© 2026 Worldgineer. Todos los derechos reservados.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 16px; color: #52616B; margin-top: -20px;">ECHO | Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)


# Orientación
elif menu == "Orientación":
    st.header("Mi orientación.")

    fecha = datetime.now(tz=ZoneInfo("America/Puerto_Rico")).strftime("%d/%m/%Y")

    # Datos actualizados desde Configuración
    st.subheader("Hola " + st.session_state.nombre + "!")
    st.write("📅 Hoy es: " + fecha)
    st.write("🏠 Estás en: " + st.session_state.lugar)

    st.subheader("👨‍👩‍👧 Mi persona de confianza")
    st.write("Nombre: " + st.session_state.familiar)
    st.write("📞 Teléfono: " + st.session_state.telefono)

    st.divider()

    # Mensaje para dar tranquilidad
    st.success("Estás en un lugar conocido. Si necesitas ayuda, puedes hablar con tu familiar o una persona de confianza.")

    st.divider()
    st.markdown('<p style="text-align: center; font-size: 18px; color: #174A73;">© 2026 Worldgineer. Todos los derechos reservados.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 16px; color: #52616B; margin-top: -20px;">ECHO | Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)


# Encargado
elif menu == "Encargado":
    st.header("Encargado")

    # Mostramos los datos guardados
    st.subheader("Persona: " + st.session_state.nombre)
    st.write("🏠 Lugar: " + st.session_state.lugar)
    st.write("👨‍👩‍👧 Familiar: " + st.session_state.familiar)
    st.write("📞 Teléfono: " + st.session_state.telefono)

    st.divider()

    # Historial
    total = len(st.session_state.historial)
    st.metric("Mensajes recibidos", total)
    st.subheader("Historial de mensajes")

    if total == 0:
        st.info("Todavía no hay mensajes guardados.")
    else:
        for mensaje in st.session_state.historial:
            st.write("• " + mensaje)

    if st.button("Borrar historial"):
        st.session_state.historial = []
        st.rerun()

    st.divider()
    st.markdown('<p style="text-align: center; font-size: 18px; color: #174A73;">© 2026 Worldgineer. Todos los derechos reservados.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 16px; color: #52616B; margin-top: -20px;">ECHO | Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)


# Configuración
elif menu == "Configuración":
    st.header("Configuración")
    st.write("Aquí puedes configurar la aplicación.")

    nombre = st.text_input("Nombre", value=st.session_state.nombre)
    lugar = st.text_input("Lugar", value=st.session_state.lugar)
    familiar = st.text_input("Familiar", value=st.session_state.familiar)
    telefono = st.text_input("Teléfono", value=st.session_state.telefono)

    # Guardamos los cambios
    if st.button("Guardar información"):
        st.session_state.nombre = nombre
        st.session_state.lugar = lugar
        st.session_state.familiar = familiar
        st.session_state.telefono = telefono

        st.success("¡Información guardada!")

    st.divider()
    st.markdown('<p style="text-align: center; font-size: 18px; color: #174A73;">© 2026 Worldgineer. Todos los derechos reservados.</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 16px; color: #52616B; margin-top: -20px;">ECHO | Haz que tu mensaje retumbe</p>', unsafe_allow_html=True)
# link

# https://super-space-succotash-jr9pgw554x4xhpppp-8501.app.github.dev/