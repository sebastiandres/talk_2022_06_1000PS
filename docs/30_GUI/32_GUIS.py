import streamlit as st

st.title("💻 GUI - Graphical User Interface")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Orientado a la funcionalidad
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Versionamiento es difícil
    * Requiere instalación
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Alta
    * Usuario: Baja (pero instalación puede ser difícil)
    """
    st.markdown(m)

with c2:
    st.image("images/eval/gui.png", width=600)