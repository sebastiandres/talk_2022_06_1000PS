import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("Librería (pypi + readthedocs)")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Escalable y flexible
    * Aprendizaje "para toda la vida"
    * Apropiado para algunas tareas.
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Versionamiento es muy dificil
    * Requiere instalación (pero es fácil)
    * Requiere documentación y explicación
    * Encapsula código pero no funcionalidad
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Alta
    * Usuario: Media
    """
    st.markdown(m)

with c2:
    st.image("images/eval/libreria.png", width=600)