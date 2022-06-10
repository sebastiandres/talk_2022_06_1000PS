import streamlit as st

st.title("🛠️ DIY - Do It Yourself")
st.header("Librería (pypi + readthedocs)")

m = """
Ejemplos:
"""
st.markdown(m)

m = """
* streamlit_book
  * https://pypi.org/project/streamlit-book/
  * https://streamlit-book.readthedocs.io/en/latest/
"""
st.markdown(m)

m = """
* pypsdier
  * https://pypi.org/project/pypsdier/
  * https://pypsdier.readthedocs.io/en/latest/
"""
st.markdown(m)

st.markdown("Existe una enorme satisfacción en crear una librería que puedes instalar con pip:")
st.code("pip install streamlit_book")