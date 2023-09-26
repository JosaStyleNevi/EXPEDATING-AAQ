import streamlit as st
import pandas as pd
excel=pd.read_excel("Copia de REPORTE COMENSALES - IMCO 23.09.23.xlsx")
st.data_editor(excel)