import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Placeholder pour afficher le résultat
result = st.empty()

# JS + HTML du scanner
scanner_html = """
<div id="reader" style="width: 320px"></div>

<script src="https://unpkg.com/html5-qrcode"></script>

<script>
    function onScanSuccess(decodedText) {
        // Envoyer vers Streamlit via postMessage
        const message = {type: "qr_scanned", data: decodedText};
        window.parent.postMessage(message, "*");
    }

    function onScanFailure(error) {
        // silence
    }

    const scanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: 250 },
        false
    );
    scanner.render(onScanSuccess, onScanFailure);
</script>
"""

components.html(scanner_html, height=500)

# Réception JS -> Streamlit
qr_receiver = """
<script>
window.addEventListener("message", (event) => {
    if (event.data && event.data.type === "qr_scanned") {
        const qrValue = event.data.data;
        window.parent.postMessage(
            {isStreamlitMessage: true, qrValue: qrValue},
            "*"
        );
    }
});
</script>
"""

st.markdown(qr_receiver, unsafe_allow_html=True)

# Lire la valeur envoyée par JS
if "qrValue" not in st.session_state:
    st.session_state["qrValue"] = None

# AFFICHER LA VALEUR DU QR CODE DÉTECTÉ
if st.session_state["qrValue"]:
    result.success(f"QR Code détecté : {st.session_state['qrValue']}")
    st.session_state["battery_id"] = st.session_state["qrValue"]

    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données")