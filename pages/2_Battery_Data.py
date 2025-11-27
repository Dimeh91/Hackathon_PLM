import streamlit as st
import pandas as pd
import os
from streamlit import switch_page # Ajouté pour le retour au scanner

st.set_page_config(page_title="Battery Data", page_icon="📄", layout="wide")

st.title("📄 Battery Passport Data")

# Récupération de l'ID stocké par la page Scanner
battery_id = st.session_state.get("battery_id", None)

if battery_id is None:
    st.error("❌ Aucun QR code n'a été scanné. Veuillez d'abord scanner un QR code.")
    
    # Redirection au clic si l'utilisateur arrive ici par erreur
    if st.button("⬅️ Retour au Scanner QR"):
        switch_page("app") 
    st.stop()

st.write(f"ID de la batterie scannée : **{battery_id}**")

# Construction du chemin CSV (assure-toi que l'ID correspond au nom du fichier)
csv_path = os.path.join("data", f"{battery_id}.csv")
st.info(f"Tentative de chargement du fichier : `{csv_path}`")

# Vérifier si le fichier existe et le charger
try:
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        st.success("✅ Données chargées avec succès 👇")
        st.dataframe(df, use_container_width=True)
    else:
        st.error(f"❌ Aucun fichier CSV trouvé pour l'ID : {battery_id}")
        st.warning(f"Vérifiez que le fichier nommé `{battery_id}.csv` existe dans le dossier `/data`.")
        
        # Bouton pour revenir et refaire un scan
        if st.button("⬅️ Retour au Scanner QR"):
            if "battery_id" in st.session_state:
                del st.session_state["battery_id"] # Efface l'ID pour un nouveau scan
            switch_page("app")

except Exception as e:
    st.error(f"Une erreur s'est produite lors du chargement du fichier CSV : {e}")
    st.page_link("app.py", label="⬅️ Retour au Scanner QR")