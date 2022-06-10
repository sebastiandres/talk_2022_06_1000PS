import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("Repositorios (github, bitbucket, ...)")

m = """
Ejemplos:
"""
st.markdown(m)

m = """
* https://github.com/sebastiandres
  * https://github.com/sebastiandres/talk_2022_06_1000PS
  * https://github.com/sebastiandres/streamlit_book
"""
st.markdown(m)

m = """
* https://bitbucket.org/sebastiandres/
  * https://bitbucket.org/sebastiandres/pypsdier/
"""
st.markdown(m)