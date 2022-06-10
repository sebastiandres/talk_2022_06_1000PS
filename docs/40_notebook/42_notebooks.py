import streamlit as st

st.title("📓 Notebooks")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Documentación y código
    * Autocontenido
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Versionamiento es muy dificil
    * No es tan intuitivo
    * Jupyter Notebook requiere instalación
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Baja
    * Usuario: Baja
    """
    st.markdown(m)

with c2:
    st.image("images/eval/notebook.png", width=600)