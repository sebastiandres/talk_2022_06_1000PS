import streamlit as st

st.set_page_config(layout="wide")
c1, c2 = st.columns([7,3])
with c1:
    st.markdown("## 1000 Programadores Salteños")
    st.markdown("# Construí esto, pero...  _¿Cómo lo comparto?_")
    st.markdown("## Sebastián Flores, Junio 2022")
    st.write("Repositorio de la presentación: https://github.com/sebastiandres/talk_2022_06_1000PS")
with c2:
    st.image("images/streamlit_cl.png")
