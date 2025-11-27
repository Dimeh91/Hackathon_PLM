import streamlit as st

st.set_page_config(page_title="Centre de Tri", page_icon="♻️")

st.title("♻️ Centre de Tri")

# Fake database utilisateur
users = {
    "recycle": {"password": "recycle123", "role": "recycler"}
}

if "tri_logged_in" not in st.session_state:
    st.session_state["tri_logged_in"] = False

if not st.session_state["tri_logged_in"]:

    st.subheader("Connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if username in users and users[username]["password"] == password:
            st.session_state["tri_logged_in"] = True
            st.success("Connexion réussie !")
            st.rerun()
        else:
            st.error("Identifiants incorrects.")

    st.stop()

# -----------------------------------------------
# Interface Centre de Tri
# -----------------------------------------------

st.success("Connecté au Centre de Tri ✔")

st.subheader("Traitement et recyclage des batteries")

battery_to_recycle = st.text_input("ID Batterie à recycler")

if st.button("Marquer comme recyclée"):
    st.success(f"Batterie {battery_to_recycle} recyclée avec succès.")
    # Ici tu pourras mettre à jour Neo4j ou CSV