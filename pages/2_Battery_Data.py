import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Battery Data", page_icon="📄", layout="wide")

st.title("📄 Battery Passport Data")

battery_id = st.session_state.get("battery_id", None)

if battery_id is None:
    st.error("Aucun QR code n'a été scanné.")
    st.stop()

csv_path = f"data/{battery_id}.csv"

if not os.path.exists(csv_path):
    st.error(f"Fichier introuvable : {csv_path}")
    st.stop()

df = pd.read_csv(csv_path)

st.write(f"### 🔋 Données de la batterie **{battery_id}**")
st.dataframe(df, use_container_width=True)

# ----------------------------------------------------------
# PARTIE ADMIN : modification possible seulement si connecté
# ----------------------------------------------------------
if st.session_state.get("admin_logged_in"):

    st.success("Mode Administrateur activé : vous pouvez modifier les données")

    edited = st.data_editor(df, hide_index=True, num_rows="dynamic")

    if st.button("💾 Sauvegarder les modifications"):
        edited.to_csv(csv_path, index=False)
        st.success("Modifications enregistrées ✔")

else:
    st.info("Connexion admin requise pour modifier les données.")