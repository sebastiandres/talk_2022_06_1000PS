import streamlit as st

st.title("💻 GUI - Graphical User Interface")


c1, c2 = st.columns([3,7])

with c1:
    st.subheader("Alternativas")
    m = """
    * PyGUI
    * Wax, wxpython
    * Pyforms
    * PySimpleGUI
    * Libavg
    * Kivy
    * PySide2
    * Tkinter
    * PyQt
    """
    st.markdown(m)

with c2:
    st.image("images/pyqt.png", width=600)
    st.caption("https://dev.to/amigosmaker/pyqt-vs-tkinter-spanish-2n4k")