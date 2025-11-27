import streamlit as st
import streamlit.components.v1 as components

st.title("Test Scanner Minimal")

components.html("""
<div id="reader" style="width: 350px"></div>

<script src="https://unpkg.com/html5-qrcode"></script>

<script>
function onScanSuccess(decodedText) {
    alert("QR détecté : " + decodedText);
}

function onScanFailure(err) {}

const scanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: 250 },
    false
);

scanner.render(onScanSuccess, onScanFailure);
</script>
""", height=500)