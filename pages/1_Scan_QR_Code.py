import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Input caché – reçoit la valeur depuis le JS
qr_value = st.text_input("QR détecté", key="decodedText", label_visibility="collapsed")

# Scanner HTML + JS
components.html(
    """
    <div id="reader" style="width: 350px"></div>

    <script src="https://unpkg.com/html5-qrcode"></script>

    <script>
    function onScanSuccess(decodedText) {
        // Trouver l'input Streamlit par son ID
        const inputBox = window.parent.document.querySelector('input[id="decodedText"]');

        if (inputBox) {
            inputBox.value = decodedText;
            inputBox.dispatchEvent(new Event('input', { bubbles: true }));
        }

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
    """,
    height=500
)

# Lorsque la valeur change → on affiche les infos Streamlit
if qr_value:
    st.success(f"QR Code détecté : **{qr_value}**")

    # On stocke le résultat dans la session
    st.session_state["battery_id"] = qr_value

    # Bouton vers la page Battery Data
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de la batterie")