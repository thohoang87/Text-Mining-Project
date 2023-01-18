import streamlit as st
from fonctions.main import load_db


st.set_page_config(
    page_title="Disney Text Mining",
    page_icon="👋",
)
st.title("Hello")
st.markdown('Page principale')
st.sidebar.markdown('Page principale')

if st.button('Recharger la base de données'):
    result = load_db()
    st.write(result[0][0])