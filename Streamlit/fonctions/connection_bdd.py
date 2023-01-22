import streamlit as st
from pymongo import MongoClient
import streamlit as st
from bson.son import SON
import re


@st.experimental_singleton
def get_connection():
    # connection à la base de donnée en local
    client = MongoClient("mongodb", port=27017)
    # connection à la db
    db_name = client["disney"]
    # connection à la collection
    collection = db_name["Tripadvisor"]
    return collection


# @st.experimental_memo(ttl=600)
@st.cache
def statistics():
    collection = get_connection()
    total = collection.count_documents({})
    pipeline = [{"$group": {"_id": "$Site", "count": {"$sum": 1}}}]
    total_site = list(collection.aggregate(pipeline=pipeline))
    some_comments = list(collection.find({},{'_id':0}).limit(5))
    years = (collection.distinct('Annee_commentaire', {'Type':'Hotel'}))
    years = [x for x in years if x is not None]
    years = [x for x in years if re.compile(r'\d{4}').match(x)]
    return total, total_site, some_comments, years

@st.cache
def hotel(option, annee):
    collection = get_connection()
    if option == 'Commentaires':
        commentaires = [x['Commentaire'] for x in collection.find({'Type':'Hotel', 'Annee_commentaire':annee}, {'_id':0, 'Commentaire':1})]
        return commentaires
    elif option == 'Note':
        notes = [x['Note'] for x in collection.find({'Type':'Hotel', 'Annee_commentaire':annee}, {'_id':0, 'Note':1})]
        return notes
    elif option == 'Localisation':
        pipeline = [{'$match':{'Annee_commentaire':annee, 'Type':'Hotel'}}, {'$group' : {'_id':'$Localisation', 'count' : { '$sum': 1 }}}, {'$sort': SON([('count', -1), ('_id',1)])}, {'$limit':10}]
        localisations = [x for x in collection.aggregate(pipeline) if x['_id'] is not None and x['_id'] != '']
        return localisations



@st.cache
def parc(option, annee):
    collection = get_connection()
    if option == 'Commentaires':
        commentaires = [x['Commentaire'] for x in collection.find({'Type':'Parc', 'Annee_commentaire':annee}, {'_id':0, 'Commentaire':1})]
        return commentaires
    elif option == 'Note':
        notes = [x['Note'] for x in collection.find({'Type':'Parc', 'Annee_commentaire':annee}, {'_id':0, 'Note':1})]
        return notes
    elif option == 'Localisation':
        pipeline = [{'$match':{'Annee_commentaire':annee, 'Type':'Parc'}}, {'$group' : {'_id':'$Localisation', 'count' : { '$sum': 1 }}}, {'$sort': SON([('count', -1), ('_id',1)])}, {'$limit':10}]
        localisations = [x for x in collection.aggregate(pipeline) if x['_id'] is not None and x['_id'] != '']
        return localisations