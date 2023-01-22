# import streamlit as st
# import pandas as pd
# import pandas as pd
# # from unidecode import unidecode
# from fonctions.analyse import *
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
from gensim.models import Word2Vec
# from scipy.cluster.hierarchy import dendrogram, linkage,fcluster
# from sklearn.feature_extraction.text import CountVectorizer
# import matplotlib.pyplot as plt
# # from wordcloud import WordCloud
# # import pattern
# # from pattern.fr import sentiment
from fonctions.connection_bdd import *
from fonctions.analyse import *
from collections import Counter

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Analyse ", page_icon="📊")
st.markdown("# Analyse")
st.sidebar.header("Analyse")
st.write(
    """The aim here is to highlight the hotel data """
)


total, total_site, some_comments, years = statistics()

analysis_options = ["Commentaires", "Note","Localisation"]
selected_option = st.selectbox("Select an analysis option:", analysis_options)
selected_year = st.selectbox("Choisissez l'année :", years)

if selected_year and selected_option=='Commentaires':
    comments = hotel(selected_option, selected_year)
    corpus_nettoye = nettoyage_corpus(comments)

    st.markdown("## le World Cloud des commentaires")
    
    st.pyplot(wordcloud(corpus_nettoye))


    st.markdown('## Analyse des sentiments')
    sentiments, comm_tres_positifs, comm_positifs, comm_neutres, comm_negatifs, comm_tres_negatifs = liste_sentiment(corpus_nettoye=corpus_nettoye)
    fig, axs = fig_sentiment(sentiments)
    st.pyplot(fig)

    st.markdown('## Wordcloud des commentaires très positifs')
    if len(comm_tres_positifs) > 0:
        st.pyplot(wordcloud(comm_tres_positifs))
    else:
        st.write('Il n\' a pas de commentaires très positifs ...')
    st.markdown('## Wordcloud des commentaires positifs')
    if len(comm_positifs) > 0:
        st.pyplot(wordcloud(comm_positifs))
    else:
        st.write('Il n\' a pas de commentaires positifs ...')
    st.markdown('## Wordcloud des commentaires neutres')
    if len(comm_neutres) > 0:
        st.pyplot(wordcloud(comm_neutres))
    else:
        st.write('Il n\' a pas de commentaires neutres ...')
    st.markdown('## Wordcloud des commentaires négatifs')
    if len(comm_negatifs) > 0:
        st.pyplot(wordcloud(comm_negatifs))
    else:
        st.write('Il n\' a pas de commentaires négatifs ...')
    st.markdown('## Wordcloud des commentaires très négatifs')
    if len(comm_tres_negatifs) > 0:
        st.pyplot(wordcloud(comm_tres_negatifs))
    else:
        st.write('Il n\' a pas de commentaires très négatifs ...')


    
    modele_hotel = Word2Vec(corpus_nettoye,vector_size=100,window=3,min_count=2,epochs=100)
    words_hotel = modele_hotel.wv
    
    #la matrice des liens
    Z_hotel = matrice_lien(corpus_nettoye,words_hotel)
    #st.button("Re-run")
    
    number = st.number_input("Entrez un seuil :", min_value=5, max_value=200, step=1, format="%d", value=10)
    
    st.markdown("## le dendrogramme")
    #afficher le dendrogramme
    my_dendogram(Z_hotel,seuil=number)
    #st.button("Re-run")
    
elif selected_option == 'Note' and selected_year:
    notes = hotel(selected_option, selected_year)
    st.pyplot(pie_charte_notes(notes))

elif selected_option == 'Localisation' and selected_year:
    localistations = hotel('Localisation', selected_year)
    st.markdown(f'## Localisations les plus fréquentes pour l\'année {selected_year}')
    for x in localistations:
        st.write(str(x["_id"]) + " " + str(x['count']))

# elif selected_option == "Note":
#     query_note_hotel = "SELECT ANNÉE,NOTE FROM COMMENTAIRE_HOTEL,NOTE,DATECOMMENTAIRE WHERE COMMENTAIRE_HOTEL.ID_NOTE = NOTE.ID_NOTE AND COMMENTAIRE_HOTEL.ID_DATECOMMENTAIRE = DATECOMMENTAIRE.ID_DATECOMMENTAIRE"
#     note_hotel = pd.read_sql(query_note_hotel, con=con)
#     st.write("note_hotel")
#     ## Choisi l'année
#     years = note_hotel['ANNÉE'].unique()
#     # Use st.selectbox to create a dropdown menu to select the year
#     selected_year = st.selectbox("Choisissez l'année :", years)
#     note_hotel_year = pd.DataFrame(note_hotel["NOTE"][note_hotel["ANNÉE"] == selected_year])
#     # on affiche bar chart:

#     count_note_hotel = note_hotel_year["NOTE"].value_counts()
#     count_note_hotel.plot(kind="bar")
#     st.set_option('deprecation.showPyplotGlobalUse', False)
#     st.pyplot()

    
# else:
#     # code to perform comment analysis
#     # Importer la table "localisation":

#     query_local_hotel = "SELECT ANNÉE,LOCALISATION FROM COMMENTAIRE_HOTEL,LOCALISATION,DATECOMMENTAIRE WHERE COMMENTAIRE_HOTEL.ID_LOCALISATION = LOCALISATION.ID_LOCALISATION AND COMMENTAIRE_HOTEL.ID_DATECOMMENTAIRE = DATECOMMENTAIRE.ID_DATECOMMENTAIRE"
#     local_hotel = pd.read_sql(query_local_hotel, con=con)
#     st.write("local_hotel")
#     # On sélectionne les localisations par rapport à l'année:
#     years = local_hotel['ANNÉE'].unique()
#         # Use st.selectbox to create a dropdown menu to select the year
#     selected_year = st.selectbox("Choisissez l'année :", years)

#     local_hotel_year = pd.DataFrame(local_hotel["LOCALISATION"][local_hotel["ANNÉE"] == selected_year])
    
#     # on affiche une table - les 10 localisations les plus fréquentes:

#     st.write(local_hotel_year.value_counts()[:10])
# con.close()



