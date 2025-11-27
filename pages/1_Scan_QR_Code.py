import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# 1) PREPARER LE SCANNER HTML/JS
scanner_html = """
<div id="reader" style="width: 700px"></div>

<script src="https://unpkg.com/html5-qrcode"></script>

<script>
    function onScanSuccess(decodedText) {
        // Envoi direct à Streamlit via query params
        const url = new URL(window.location.href);
        url.searchParams.set("qr_value", decodedText);

        // Recharge la page AVEC le QR code
        window.location.href = url.toString();
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

# 2) AFFICHER LE SCANNER
components.html(scanner_html, height=500)

# 3) RECUPERER LE QR DANS STREAMLIT (nouveau système)
params = st.query_params
qr_value = params.get("qr_value", None)

# 4) AFFICHER LE RESULTAT
if qr_value:
    qr_value = qr_value[0]  # toujours une liste
    st.success(f"QR Code détecté : **{qr_value}**")

    # stocker dans session
    st.session_state["battery_id"] = qr_value

    # bouton pour aller à la page CSV
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de la batterie")
else:
    st.info("Aucun QR code détecté pour l'instant.")