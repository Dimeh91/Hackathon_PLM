import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode
import io

st.set_page_config(page_title="Scan QR Code", page_icon="📷")

st.title("📷 Scan QR Code (server-side decoding)")
st.write("Prenez en photo un QR code pour afficher les données.")

img_file = st.camera_input("Scannez un QR code")

if img_file:
    img = Image.open(img_file)

    decoded = decode(img)

    if decoded:
        qr_value = decoded[0].data.decode("utf-8")
        st.success(f"QR détecté : **{qr_value}**")

        st.session_state["battery_id"] = qr_value

        st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données")
    else:
        st.error("Aucun QR code détecté. Essayez de nouveau.")