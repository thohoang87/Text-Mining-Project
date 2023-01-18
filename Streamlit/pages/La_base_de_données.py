import streamlit as st
import time
import sys
from fonctions.connection_bdd import statistics






st.markdown('Mise à jour de la base de données')
st.sidebar.markdown('Page secondaire')
total, total_site = statistics()
st.write(f'Il y a actuellement : {total} commentaires dans la base de données.')
for x in total_site:
    st.write(f"{x['_id']} : {x['count']}")
