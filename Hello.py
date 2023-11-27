import streamlit as st

# Configurar el título de la aplicación
st.title("Menú Lateral con Streamlit")

# Botones en lugar de cuadro desplegable
if st.sidebar.button("Expedating de Compras"):
    st.write("Bienvenido a la página de inicio.")

if st.sidebar.button("Materiales para Anddes"):
    st.write("Configura tus preferencias aquí.")

if st.sidebar.button("Materiales Surplus"):
    st.write("¿Necesitas ayuda? ¡Estamos aquí para ayudarte!")

# Puedes agregar más opciones y contenido según tus necesidades