import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Champ invisible pour recevoir le QR
qr_value = st.text_input("QR détecté", key="qr_value", label_visibility="collapsed")

html_code = """
<iframe sandbox="allow-scripts allow-camera" style="border:none;width:100%;height:400px"
srcdoc="
<!DOCTYPE html>
<html>
<head>
<script src='https://unpkg.com/html5-qrcode'></script>
</head>
<body>
<div id='reader' style='width:300px;margin:auto'></div>

<script>
function onScanSuccess(decodedText){
    const input = window.parent.document.querySelector('input[id=qr_value]');
    input.value = decodedText;
    input.dispatchEvent(new Event('input', { bubbles: true }));
}

function onScanFailure(e){}

let scanner = new Html5QrcodeScanner(
    'reader',
    { fps: 10, qrbox: 250 },
    false
);
scanner.render(onScanSuccess, onScanFailure);
</script>

</body>
</html>
"></iframe>
"""

components.html(html_code, height=500)

# Si QR détecté → afficher et bouton
if qr_value:
    st.success(f"QR Code détecté : {qr_value}")
    st.session_state["battery_id"] = qr_value

    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données associées")