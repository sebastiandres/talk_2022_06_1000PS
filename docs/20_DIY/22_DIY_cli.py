import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("CLI - Command Line Interface")

st.markdown("Agregando algunas líneas adicionales podemos empaquetar nuestras funciones como un script ejecutable desde el terminal.")

with open("code/csv_to_excel.py", "r") as fh:
    cli_str = fh.read()
st.code(cli_str)