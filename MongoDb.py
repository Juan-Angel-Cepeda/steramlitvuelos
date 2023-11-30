from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import consumer as cs
from datetime import datetime
import streamlit as st

#uri = st.secrets["DB_MONGO_URI"]
uri = "mongodb+srv://a338832:pHMc4cHtxeD4z3sg@vuelos.hyce5yh.mongodb.net/?retryWrites=true&w=majority"

def backupMongo():
    consumer = cs.Consumer('vuelos',partition=0)

    try:
        connection = MongoClient(uri, server_api=ServerApi(version='1'))
        vuelos_db = connection.vuelos_db
        vuelos_col = vuelos_db.vuelos

        for flights in consumer.consume():
            for flight in flights:
                flight['timestamp'] = datetime.utcnow()
                vuelos_col.insert_one(flight)
                print("Guradado en MongoDB")

        connection.close()

    except Exception as e:
        print(e)
    
