import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# Champ caché pour récupérer la valeur du QR
qr_value = st.text_input("", key="qr_value", label_visibility="collapsed")

# Scanner HTML + JS : fonctionne sur Streamlit Cloud
components.html(
    """
    <script src="https://unpkg.com/html5-qrcode"></script>

    <div id="reader" style="width: 320px; margin: auto;"></div>

    <script>
    function onScanSuccess(decodedText) {

        // Trouver le champ Streamlit
        const inputBox = window.parent.document.querySelector('input[id="qr_value"]');

        if (inputBox) {
            inputBox.value = decodedText;
            inputBox.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }

    function onScanFailure(error) {
        // Rien
    }

    // Lancer le scanner
    const html5QrcodeScanner = new Html5QrcodeScanner(
        "reader", 
        { fps: 10, qrbox: 250 },
        false
    );
    html5QrcodeScanner.render(onScanSuccess, onScanFailure);
    </script>
    """,
    height=500
)

# Traitement Streamlit si QR détecté
if qr_value:
    st.success(f"QR Code détecté : **{qr_value}**")

    # Stocker la valeur scannée dans la session
    st.session_state["battery_id"] = qr_value

    # Bouton vers la page des données
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de cette batterie")