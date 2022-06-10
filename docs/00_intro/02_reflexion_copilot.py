import streamlit as st

if 'index' not in st.session_state:
    st.session_state['index'] = 0

st.caption("Una pequeña reflexión antes de comenzar...")

st.markdown("Si existe Copilot (Github)... ¿Vale la pena ser programador?")

if st.button("Ejemplo de Copilot"):
    st.image("images/copilot.gif", width=1200)
    st.caption("https://pythondiario.com/2021/08/ejemplos-github-copilot.html")
