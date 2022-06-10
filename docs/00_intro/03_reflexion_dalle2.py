import streamlit as st

if 'index' not in st.session_state:
    st.session_state['index'] = 0

st.caption("Una pequeña reflexión antes de comenzar...")

st.markdown("Si existe DALLE2 (OpenAI)... ¿Vale la pena ser artista?")

links = [
"images/dalle2/A photo of kittens stressing over an Excel spreadsheet in an office.jpeg",
"images/dalle2/Confused_Bear_in_a_Calculus_Class.jpeg",
"images/dalle2/Darth Vader in Van Gogh's starry night..jpeg",
"images/dalle2/Expanded_Mona_Lisa.jpg",
]

if st.button("Ejemplos de DALLE2"):
    st.session_state['index'] = (st.session_state['index'] + 1) % len(links)
    image = links[st.session_state['index']]
    caption = image.split("/")[-1].split(".")[0]
    st.image(image, width=600)
    st.caption(caption)