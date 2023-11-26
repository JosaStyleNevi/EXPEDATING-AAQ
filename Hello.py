import streamlit as st
import pandas as pd
xls= pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/1ib2USv--f8fDn9t1Mhtp_FWOCWZfp9xV/export?format=xlsx")
xls = pd.read_excel(xls)
st.data_editor(xls)