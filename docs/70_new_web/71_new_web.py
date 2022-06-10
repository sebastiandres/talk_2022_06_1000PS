import streamlit as st

st.title("🌐 PyScript")

option = st.selectbox("Script", ["hello_world.html", "bokeh.html", "csv_to_excel.html"])
filepath = f"pyScripts/{option}"
html_code = open(filepath).read()
st.code(html_code)
st.components.v1.html(html_code, height=600)