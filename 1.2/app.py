import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

st.title("Bienvenue sur le site web de Dara")

# Lista de boroughs únicos
boroughs = df['pickup_borough'].dropna().unique()

choix = st.selectbox(
    "Indiquez votre arrondissement de récupération de votre taxi",
    boroughs
)

st.write("Tu as choisi :", choix)

# Mostrar a imagem correspondente ou a imagem de interrogação
if choix == "Manhattan":
    st.image("manhattan.jpg", caption="Manhattan, New York City")

elif choix == "Bronx":
    st.image("Bronx.webp", caption="Bronx, New York City")

elif choix == "Queens":
    st.image("queens.jpeg", caption="Queens, New York City")

elif choix == "Brooklyn":
    st.image("brooklyn.jpg", caption="Brooklyn, New York City")
