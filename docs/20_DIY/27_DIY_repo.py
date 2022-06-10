import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("Repositorios (github, bitbucket, ...)")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Escalable y flexible
    * Aprendizaje "para toda la vida"
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Curva de aprendizaje difícil
    * Comparte el código pero no la funcionalidad
    * Requiere instalación de dependencias y adicionales
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Media
    * Usuario: Media
    """
    st.markdown(m)


with c2:
    st.image("images/eval/repo.png", width=600)