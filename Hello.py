import streamlit as st
import pandas as pd

# Función para cargar datos de Google Sheets
def cargar_datos():
    xls = pd.ExcelFile("https://docs.google.com/spreadsheets/d/1ib2USv--f8fDn9t1Mhtp_FWOCWZfp9xV/export?format=xlsx")
    datito = pd.read_excel(xls)
    st.write(datito)

# Configuración de la página
st.set_page_config(layout="wide")
st.sidebar.title("ÁREA 4000\:blossom::sunflower:")
st.sidebar.header('PRESA DE RELAVES', divider='rainbow')

# Menú principal
selected_page = st.sidebar.selectbox('SELECCIONAR OPCIÓN', ['Control Compras', 'Control Materiales'])

if selected_page == 'Control Compras':
    selected_subpage = st.sidebar.radio('OPCIONES DE CONTROL COMPRAS', ['EXPEDATING', 'RESERVAS', 'AVISOS'])
    
    # Borra el contenido antes de mostrar el nuevo título y carga de datos
    st.title("")  
    
    if selected_subpage == 'EXPEDATING':
        st.title('SEGUIMIENTO DE COMPRAS ')
        cargar_datos()

    elif selected_subpage == 'RESERVAS':
        st.title('RESERVA DE MATERIALES EN SAP')
        # Puedes agregar lógica específica para 'RESERVAS' aquí si es necesario.

    elif selected_subpage == 'AVISOS':
        st.title('AVISOS GENERADOS EN SAP')
        # Puedes agregar lógica específica para 'AVISOS' aquí si es necesario.

elif selected_page == 'Control Materiales':
    selected_subpage = st.sidebar.radio('OPCIONES DE CONTROL MATERIALES', ['SURPLUS', 'C. DIRECTOS', 'DM08', 'DM05'])
    
    # Borra el contenido antes de mostrar el nuevo título
    st.title("")  
    
    if selected_subpage == 'SURPLUS':
        st.title('MATERIALES EN CUSTODIA EN WAREHOUSE - SURPLUS')
        # Puedes agregar lógica específica para 'SURPLUS' aquí si es necesario.

    elif selected_subpage == 'C. DIRECTOS':
        st.title('MATERIALES EN CUSTODIA EN WAREHOUSE - CARGOS DIRECTOS')
        # Puedes agregar lógica específica para 'C. DIRECTOS' aquí si es necesario.

    elif selected_subpage == 'DM08':
        st.title('MATERIALES EN CUSTODIO DM08')
        # Puedes agregar lógica específica para 'DM08' aquí si es necesario.

    elif selected_subpage == 'DM05':
        st.title('MATERIALES EN CUSTODIO DM05')
        # Puedes agregar lógica específica para 'DM05' aquí si es necesario.
