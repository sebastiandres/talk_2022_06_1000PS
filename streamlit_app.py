import streamlit as st
import streamlit_book as stb

st.set_page_config(layout="wide")

# Set multipage
stb.set_book_config(menu_title="Charla",
                    menu_icon="file-richtext",
                    options=[
                            "Introducción",
                            "Problema",
                            "DIY",
                            "GUI", 
                            "Notebook", 
                            "Old Web", 
                            "New Web", 
                            "Chatbots", 
                            "Webapps", 
                            "Conclusión", 
                            ],
                    paths=[
                            "docs/00_intro/", 
                            "docs/10_problema/", 
                            "docs/20_DIY/", 
                            "docs/30_GUI/", 
                            "docs/40_notebook/", 
                            "docs/50_old_web/", 
                            "docs/70_new_web/", 
                            "docs/60_bots/", 
                            "docs/80_webapps/", 
                            "docs/90_conclusion/", 
                            ],
                    save_answers=False,
                    )