import streamlit as st

st.markdown("# Conclusión")

c1, c2 = st.columns([5,4])
c1.image("images/cacarear_huevo.jpg", width=600)
m="""
## - Opciones para todos los gustos, capacidades y bolsillos.
## - Piensa en tu público objetivo primero que nada.
## - Poner el huevo y cacarearlo.
"""
c2.markdown(m)
