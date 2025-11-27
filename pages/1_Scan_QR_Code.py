import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Champ caché qui recevra le QR
qr_value = st.text_input("QR détecté (invisible)", key="qr_value", label_visibility="collapsed")

# Scanner QR en HTML + JS
scanner_html = """
<div id="reader" style="width: 500px"></div>

<script src="https://unpkg.com/html5-qrcode"></script>

<script>
function onScanSuccess(decodedText) {
    // Injecter la valeur dans un input Streamlit invisible
    const inputBox = window.parent.document.querySelector('input[id="qr_value"]');
    inputBox.value = decodedText;

    // Déclencher un event 'input' pour que Streamlit capte la valeur
    const event = new Event('input', { bubbles: true });
    inputBox.dispatchEvent(event);
}

function onScanFailure(error) {
    // ignore
}

const scanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: 250 },
    false
);
scanner.render(onScanSuccess, onScanFailure);
</script>
"""

components.html(scanner_html, height=400)

# Si QR détecté → afficher confirmation + bouton
if qr_value not in ("", None):
    st.success(f"QR Code détecté : {qr_value}")

    st.session_state["battery_id"] = qr_value

    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de la batterie")