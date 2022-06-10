import streamlit as st

st.title("📓 Notebooks")
st.header("Alternativas")
m = """
* Jupyter Notebook
* Binder
* Google Colab
* Deep Note
* Hex
* ...
"""
st.markdown(m)

notebook_url = "https://colab.research.google.com/drive/1u2nTKKMVmVnSqEl4m8f_JsFggsrwYxh3"
st.markdown(f"Ejemplo en [google colab]({notebook_url})")