import streamlit as st

st.title("📈 Webapps")

c1, c2 = st.columns([1,3])

c1.subheader("Alternativas")

m = """
* Gradio
* Plotly
* Streamlit
* Dash
"""
c1.markdown(m)

c2.image("images/stars.png", width=800)