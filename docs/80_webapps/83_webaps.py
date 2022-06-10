import streamlit as st

st.title("📈 Webapps")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Fácil de usar
    * Fácil de desarrollar: 100% Python
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Requiere un servidor ejecutando de manera continua - pero existen alternativas gratis!
    * Limitaciones de mezclar componentes y widgets existentes.
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Baja
    * Usuario: Baja
    """
    st.markdown(m)

with c2:
    st.image("images/eval/webapps.png", width=600)