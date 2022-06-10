import streamlit as st

st.markdown("# Otros")

c1, c2 = st.columns([5,7])

m="""
- Web IDEs (Integrated Development Environment): 
  - Gitpod
  - Replit
- Reproducibilidad: 
  - Kubernettes
  - Docker
- Comunidades: 
  - Kaggle 
  - HuggingFace
- Compartir datos:
  - FigShare
  - Zenodo
- Redes Sociales: 
  - medium, twitter, linkedin, etc.
"""

c1.markdown(m)

c2.image("images/options.png", width=600)