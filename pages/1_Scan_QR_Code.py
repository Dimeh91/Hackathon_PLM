import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

qr_value = st.text_input("QR détecté", key="qr_value", label_visibility="collapsed")

html_code = """
<script src="https://unpkg.com/html5-qrcode"></script>

<div id="reader" style="width: 320px; margin: auto"></div>

<script>
function onScanSuccess(decodedText, decodedResult) {
    // Send decoded text to Streamlit input field
    const inputBox = window.parent.document.querySelector('input[id="qr_value"]');
    inputBox.value = decodedText;
    inputBox.dispatchEvent(new Event('input', { bubbles: true }));
}

function onScanFailure(error) {
    // Ignore scan failures
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: { width: 250, height: 250 } },
    false
);

html5QrcodeScanner.render(onScanSuccess, onScanFailure);
</script>
"""

components.html(html_code, height=600)
    
if qr_value:
    st.success(f"QR Code détecté : {qr_value}")
    st.session_state["battery_id"] = qr_value
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données")