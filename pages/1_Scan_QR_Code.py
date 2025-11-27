import streamlit as st
import streamlit.components.v1 as components
# Importation cruciale pour la navigation forcée
from streamlit import switch_page 

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Scannez un QR code pour charger les données de la batterie.")

# --- 1. Le widget Streamlit qui reçoit la valeur ---
QR_INPUT_KEY = "qr_decoded_value"
qr_value = st.text_input("QR détecté", key=QR_INPUT_KEY, label_visibility="collapsed")

# --- 2. Scanner HTML + JS ---
# NOTE: Le JS utilise la variable QR_INPUT_KEY de Python pour garantir la bonne communication
components.html(
    f"""
    <div id="reader" style="width: 350px"></div>

    <script src="https://unpkg.com/html5-qrcode"></script>

    <script>
    function onScanSuccess(decodedText) {{
        const inputId = "{QR_INPUT_KEY}";
        
        // Trouver l'input Streamlit dans la fenêtre parente (l'application Streamlit)
        const inputBox = window.parent.document.querySelector('input[id="' + inputId + '"]');

        if (inputBox) {{
            // Seulement mettre à jour si la valeur est nouvelle pour éviter les reloads inutiles
            if (inputBox.value !== decodedText) {{
                inputBox.value = decodedText;
                
                // Déclencher un événement 'input' pour informer Streamlit du changement
                // Ceci est l'action qui déclenche le re-run du script Python
                inputBox.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }}
        }}
    }}

    function onScanFailure(err) {{}}

    const scanner = new Html5QrcodeScanner(
        "reader",
        {{ fps: 10, qrbox: 250 }},
        false
    );
    window.scanner = scanner;

    scanner.render(onScanSuccess, onScanFailure);
    </script>
    """,
    height=500
)

# --- 3. Logique de Stockage et REDIRECTION IMMÉDIATE ---
# S'exécute quand Streamlit détecte que qr_value a changé grâce à l'événement JS
if qr_value:
    st.success(f"QR Code détecté : **{qr_value}**")

    # Stocker le résultat dans la session
    st.session_state["battery_id"] = qr_value

    st.info("Redirection immédiate vers les données...")
    
    # COMMANDE CRUCIALE : Force la navigation vers la page /pages/2_Battery_Data.py
    switch_page("2_Battery_Data") 
    
    # NOTE: st.page_link n'est plus nécessaire car la redirection est automatique