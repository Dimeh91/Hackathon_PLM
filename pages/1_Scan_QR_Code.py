import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="QR Scanner", page_icon="📷", layout="wide")

st.title("📷 Scanner une batterie")

qr_value = st.text_input("QR détecté", key="qr_value", label_visibility="collapsed")

html_code = """
<iframe sandbox="allow-scripts allow-camera;" style="border:none;width:100%;height:400px"
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
    const inputBox = window.parent.document.querySelector('input[id=qr_value]');
    inputBox.value = decodedText;
    inputBox.dispatchEvent(new Event('input', { bubbles: true }));
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

components.html(html_code, height=500, scrolling=True)

if qr_value:
    st.success(f"QR détecté : {qr_value}")
    st.session_state["battery_id"] = qr_value
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données")