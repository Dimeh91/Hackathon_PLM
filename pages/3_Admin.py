import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="Admin", page_icon="🔑")

st.title("🔑 Espace Administrateur")

# --------------------
# Gestion de session
# --------------------
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False

# --------------------
# Si NON connecté → Formulaire de login
# --------------------
if not st.session_state["admin_logged_in"]:

    st.subheader("Connexion administrateur")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    # Identifiants simplifiés pour hackathon
    if st.button("Se connecter"):
        if username == "admin" and password == "admin123":
            st.session_state["admin_logged_in"] = True
            st.success("Connexion réussie !")
            st.rerun()
        else:
            st.error("Identifiants incorrects.")

    st.stop()

# --------------------
# Si connecté → Interface Admin
# --------------------

st.success("Connecté en tant qu'administrateur ✔")

# Bouton de déconnexion
if st.button("Déconnexion"):
    st.session_state["admin_logged_in"] = False
    st.rerun()

st.subheader("🛠️ Gestion des données Batteries")

# Liste des CSV dans /data
data_files = [f for f in os.listdir("data") if f.endswith(".csv")]

if not data_files:
    st.error("Aucun fichier CSV trouvé dans /data.")
    st.stop()

battery_choice = st.selectbox("Choisissez une batterie à modifier :", data_files)

# Charger la batterie choisie
df = pd.read_csv(f"data/{battery_choice}")

st.write("### 🔍 Aperçu des données actuelles")
st.dataframe(df, use_container_width=True)

st.write("### ✏️ Modifier les données")

edited_df = st.data_editor(df, hide_index=True, num_rows="dynamic")

# Bouton pour sauvegarder
if st.button("💾 Sauvegarder les modifications"):
    edited_df.to_csv(f"data/{battery_choice}", index=False)
    st.success("Modifications enregistrées avec succès !")