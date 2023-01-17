#import streamlit as st
from pymongo import MongoClient
import streamlit as st


@st.experimental_singleton
def get_connection():
    # connection à la base de donnée en local
    client = MongoClient("mongodb://root:root@localhost:27017/")
    # connection à la db
    db_name = client["disney"]
    # connection à la collection
    collection = db_name["disney"]
    return collection


@st.experimental_memo(ttl=600)
def statistics():
    collection = get_connection()
    total = collection.count_documents({})
    pipeline = [{"$group": {"_id": "$Site", "count": {"$sum": 1}}}]
    total_site = list(collection.aggregate(pipeline=pipeline))
    return total, total_site


