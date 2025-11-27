import streamlit as st

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Champ caché
qr_value = st.text_input("QR détecté", key="qr_value", label_visibility="collapsed")

# HTML DIRECT (pas iframe)
html_code = """
<div id="reader" style="width: 500px; margin: auto;"></div>

<script src="https://unpkg.com/html5-qrcode@2.3.7"></script>

<script>
function onScanSuccess(decodedText) {
    const inputBox = window.parent.document.querySelector('input[id="qr_value"]');
    inputBox.value = decodedText;
    inputBox.dispatchEvent(new Event('input', { bubbles: true }));
}

function onScanFailure(error) {}

setTimeout(() => {
    const scanner = new Html5QrcodeScanner(
        "reader", 
        { fps: 10, qrbox: 250 },
        false
    );
    scanner.render(onScanSuccess, onScanFailure);
}, 500);
</script>
"""

st.components.v1.html(html_code, height=600, scrolling=False)
    
if qr_value:
    st.success(f"QR Code détecté : **{qr_value}**")
    st.session_state["battery_id"] = qr_value
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données associées")