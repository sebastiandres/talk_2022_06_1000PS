import streamlit as st

# Set wide display
st.set_page_config(layout="wide")

st.write("USER:")
st.write(st.experimental_user)

# Some display on the sidebar

st.sidebar.markdown("Some text")
st.sidebar.selectbox("Some options", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 1", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 2", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 3", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 4", ["uno", "dos", "tres"])
st.sidebar.selectbox("Some options 5", ["uno", "dos", "tres"])