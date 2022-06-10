import streamlit as st

st.title("🛠️ DIY - Do It Yourself")

st.subheader("Alternativas")
m = """
* Enviar scripts por correo electrónico
* CLI - Command Line Interface:
  * sys.argv
  * argparse
  * docopt
  * click
  * typer
* Repositorios:
  * github
  * bitbucket
  * gitlab
* Librerías:
  * Wheel
  * Pypi
* Documentación:
  * Readthedocs
"""
st.markdown(m)