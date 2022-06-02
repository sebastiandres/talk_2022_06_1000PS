import streamlit as st

st.title("Intro")

st.markdown("""
This is a test, considering a reference to a single file
""")

st.sidebar.markdown("Some text")
st.sidebar.selectbox("Some options", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 1", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 2", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 3", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 4", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 5", ["uno", "dos", "tres"])