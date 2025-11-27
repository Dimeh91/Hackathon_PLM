import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")

st.write("Pointez votre caméra vers un QR code.")

# --- 1) JS SCANNER AVEC ENVOI DIRECT VERS STREAMLIT ---
component = components.declare_component("qrscanner", url="http://localhost:3001")

qr_value = component(default="")

if qr_value:
    st.success(f"QR Code détecté : **{qr_value}**")
    st.session_state["battery_id"] = qr_value
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de la batterie")
else:
    st.info("Aucun QR détecté pour l'instant.")