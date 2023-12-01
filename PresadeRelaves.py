import streamlit as st
import pandas as pd

def cargar_datos(filtro_palabra):
    xls = pd.ExcelFile("https://docs.google.com/spreadsheets/d/1Dp5DmHEZ_UZ2NrIzOuvS5J1jNlyEo7v5/export?format=xlsx")
    datito = pd.read_excel(xls)

    for filtro in filtros:
        filtro = filtro.lower()
        datito = datito[datito.apply(lambda row: row.astype(str).str.lower().str.contains(filtro).any(), axis=1)]

    st.write(datito)

st.set_page_config(layout="wide")
st.sidebar.title("ÁREA 4000:blossom::sunflower:")
st.sidebar.header('PRESA DE RELAVES', divider='rainbow')

selected_page = st.sidebar.selectbox('SELECCIONAR OPCIÓN', ['Control Compras', 'Control Materiales'])

if selected_page == 'Control Compras':
    selected_subpage = st.sidebar.radio('OPCIONES DE CONTROL COMPRAS', ['EXPEDATING', 'RESERVAS', 'AVISOS'])

    st.title("")  
    
    if selected_subpage == 'EXPEDATING':
        st.title('SEGUIMIENTO DE COMPRAS ')
        filtros = st.text_input("Filtrar por palabras clave (separadas por coma):")
        filtros = [filtro.strip() for filtro in filtros.split(',')]  # Convertir la entrada en una lista de filtros
        cargar_datos(filtros)

    elif selected_subpage == 'RESERVAS':
        st.title('RESERVA DE MATERIALES EN SAP')

    elif selected_subpage == 'AVISOS':
        st.title('AVISOS GENERADOS EN SAP')

elif selected_page == 'Control Materiales':
    selected_subpage = st.sidebar.radio('OPCIONES DE CONTROL MATERIALES', ['SURPLUS', 'C. DIRECTOS', 'DM08', 'DM05'])

    st.title("")  
    
    if selected_subpage == 'SURPLUS':
        st.title('MATERIALES EN CUSTODIA EN WAREHOUSE - SURPLUS')

    elif selected_subpage == 'C. DIRECTOS':
        st.title('MATERIALES EN CUSTODIA EN WAREHOUSE - CARGOS DIRECTOS')

    elif selected_subpage == 'DM08':
        st.title('MATERIALES EN CUSTODIO DM08')

    elif selected_subpage == 'DM05':
        st.title('MATERIALES EN CUSTODIO DM05')
