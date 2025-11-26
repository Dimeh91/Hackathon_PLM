import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Battery Data", page_icon="📄", layout="wide")

st.title("📄 Battery Passport Data")

# Récupération de l'ID stocké par la page Scan QR
battery_id = st.session_state.get("battery_id", None)

if battery_id is None:
    st.error("Aucun QR code n'a été scanné. Veuillez d'abord scanner un QR code.")
    st.stop()

st.write(f"ID de la batterie scannée : **{battery_id}**")

# Construction du chemin CSV
csv_path = f"data/{battery_id}.csv"

# Vérifier si le fichier existe
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.success("Données chargées avec succès 👇")
    st.dataframe(df, use_container_width=True)
else:
    st.error(f"Aucun fichier CSV trouvé pour : {battery_id}")
    st.info("Vérifiez que le fichier existe dans le dossier `/data` et qu'il porte le bon nom.")