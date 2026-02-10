import streamlit as st
import pandas as pd

# ----------------------------
# CONFIGURATION DE LA PAGE
# ----------------------------
st.set_page_config(page_title="Album Photo du Chien", layout="wide")

# ----------------------------
# CHARGEMENT DES UTILISATEURS
# ----------------------------
@st.cache_data
def load_users():
    return pd.read_csv("users.csv")

users_df = load_users()

# ----------------------------
# FONCTION AUTHENTIFICATION
# ----------------------------
def authenticate(username, password):
    user = users_df[
        (users_df["name"] == username) &
        (users_df["password"] == password)
    ]
    return user

# ----------------------------
# SESSION STATE
# ----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# ----------------------------
# PAGE LOGIN
# ----------------------------
if not st.session_state.logged_in:

    st.title("🔐 Page d'authentification")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        user = authenticate(username, password)

        if not user.empty:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Connexion réussie ✅")
            st.rerun()
        else:
            st.error("Identifiants incorrects ❌")

# ----------------------------
# APPLICATION PRINCIPALE
# ----------------------------
else:

    # Sidebar
    st.sidebar.title("📌 Menu")
    st.sidebar.write(f"Bienvenue {st.session_state.username} 👋")

    page = st.sidebar.radio(
        "Navigation",
        ["👉🏻 Accueil", "🐶 Album Photo"]
    )

    if st.sidebar.button("Déconnexion"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

        # ----------------------------
    # PAGE ACCUEIL
    # ----------------------------
    if page == "👉🏻 Accueil":
        st.title("🏠 Page d'accueil")
        st.write("Bienvenue dans l'application Album Photo du Chien ! 🐶")
        st.write("Utilisez le menu à gauche pour naviguer.")

    # ----------------------------
    # PAGE ALBUM PHOTO
    # ----------------------------
    elif page == "🐶 Album Photo":
        st.title("📸 Album Photo du Chien")

        # 3 imagens na mesma linha
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("MILKA")
            st.image("cao7.jpeg", use_container_width=True)

        with col2:
            st.header("MIMOSA")
            st.image("cao4.jpeg", use_container_width=True)

        with col3:
            st.header("PIPOCA")
            st.image("cao8.jpeg", use_container_width=True)
