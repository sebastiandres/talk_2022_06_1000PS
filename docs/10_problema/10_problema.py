import streamlit as st

st.markdown("## Problema:")
st.markdown("Alguien necesita ayuda para convertir un archivo csv a excel.")
st.markdown("### TODO. EL. TIEMPO.")
st.markdown("¿Cómo le ayudamos?")
st.markdown("¿Cómo compartimos nuestro código?")
st.markdown("¿Cómo generamos autonomía?")

if st.button("¿Porqué es difícil?"):
    st.markdown("**3 problemas comunes**: encoding, separador, conversión automática de tipos.")
    st.image("images/problema_csv.png")