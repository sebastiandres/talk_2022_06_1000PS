import streamlit as st

st.title("🌐 PyScript")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Fácil de usar
    * No requiere instalación para usuario
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * ~~Requiere un servidor ejecutando de manera continua~~
    * Desarrollo puede llegar a ser complejo
    * ~~Requiere aprender un framework~~
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Media
    * Usuario: Baja
    """
    st.markdown(m)


with c2:
    st.image("images/eval/newweb.png", width=600)