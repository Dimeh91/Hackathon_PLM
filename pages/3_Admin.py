import streamlit as st

st.set_page_config(page_title="Admin", page_icon="🔑")

st.title("🔑 Espace Administrateur")

# Fake database utilisateur
users = {
    "admin": {"password": "admin123", "role": "admin"}
}

# Si l'utilisateur n'est pas connecté → affichage login
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False

if not st.session_state["admin_logged_in"]:

    st.subheader("Connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if username in users and users[username]["password"] == password:
            st.session_state["admin_logged_in"] = True
            st.success("Connexion réussie !")
            st.rerun()
        else:
            st.error("Identifiants incorrects.")

    st.stop()

# -----------------------------------------------
# Si connecté → Interface Admin
# -----------------------------------------------

st.success("Connecté en tant qu'Administrateur ✔")

st.subheader("Panneau de gestion")

st.write("📌 Ici tu peux ajouter des batteries, modifier des données, etc.")

battery_id = st.text_input("Ajouter un nouvel ID de batterie")

if st.button("Créer une nouvelle batterie"):
    st.success(f"Batterie créée : {battery_id}")
    # Tu pourras ajouter ici du code pour écrire un CSV ou Neo4j