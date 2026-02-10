import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Manipulation de données et création de graphiques")

# Liste des fichiers CSV
csv_list = {
    "Flights": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv",
    "Tips": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv",
    "Iris": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv",
    "Titanic": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv",
    "Diamonds": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv"
}

# Choix CSV
st.subheader("Choisissez un fichier CSV à charger")
csv_choice = st.selectbox("Fichier CSV", list(csv_list.keys()))
df = pd.read_csv(csv_list[csv_choice])

st.subheader(f"Données du dataset: {csv_choice}")
st.dataframe(df)

# Choix des colonnes
st.subheader("Choisissez les colonnes pour le graphique")
col_x = st.selectbox("Colonne X", df.columns)

numeric_cols = df.select_dtypes(include='number').columns
if len(numeric_cols) == 0:
    st.warning("Aucune colonne numérique disponible pour créer un graphique.")
    col_y = None
else:
    col_y = st.selectbox("Colonne Y (numérique)", numeric_cols)

chart_type = st.selectbox("Type de graphique", ["bar_chart", "line_chart", "scatter_chart"])

st.subheader("Graphique généré")

if col_y is not None:
    df_plot = df[[col_x, col_y]].copy()

    if chart_type == "scatter_chart":
        plt.figure(figsize=(8,5))
        plt.scatter(df_plot[col_x], df_plot[col_y], color="blue")
        plt.xlabel(col_x)
        plt.ylabel(col_y)
        plt.grid(True)
        st.pyplot(plt)

    elif chart_type in ["bar_chart", "line_chart"]:
        # Forçar coluna X como string
        df_plot[col_x] = df_plot[col_x].astype(str)

        # Agrupar valores iguais no eixo X
        df_agg = df_plot.groupby(col_x, as_index=False)[col_y].sum()  # ou mean()

        if chart_type == "bar_chart":
            st.bar_chart(df_agg.set_index(col_x))
        else:
            st.line_chart(df_agg.set_index(col_x))

# Matrice de corrélation
st.subheader("Matrice de corrélation")
if st.checkbox("Afficher la matrice de corrélation"):
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        st.warning("Aucune donnée numérique pour calculer la corrélation.")
    else:
        corr = numeric_df.corr()
        # st.dataframe(corr)
        st.write("Carte de chaleur de la corrélation")
        plt.figure(figsize=(6,4))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        st.pyplot(plt)
