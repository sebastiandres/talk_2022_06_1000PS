import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("CLI - Command Line Interface")

c1, c2 = st.columns([3,7])

with c1:
    st.subheader("✅ Ventajas")
    m = """
    * Encapsula el código y lo hace utilizable
    * Puede trabajar con distintos sistemas operativos
    * Puede trabajar 'en batch'
    """
    st.markdown(m)

    st.subheader("❌ Desventajas")
    m = """
    * Requiere instalación de dependencias
    * Versionamiento no automático
    """
    st.markdown(m)

    st.subheader("🚀 Complejidad")
    m = """
    * Creador: Baja-Media
    * Usuario: Media
    """
    st.markdown(m)


with c2:
    st.image("images/eval/cli.png", width=600)