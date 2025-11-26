import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Scan QR Code", page_icon="📷", layout="wide")

st.title("📷 Scan QR Code")
st.write("Pointez votre caméra vers un QR code.")

# HTML + JS QR Scanner
qr_scanner = """
<!DOCTYPE html>
<html>
  <body>
    <div id="reader" width="600px"></div>

    <script src="https://unpkg.com/html5-qrcode"></script>

    <script>
      function onScanSuccess(decodedText) {
        // Send QR code data to Streamlit
        window.parent.postMessage({ "qrData": decodedText }, "*");
      }

      function onScanFailure(error) {
        // Ignore scan errors
      }

      let scanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: 250 },
        false
      );
      scanner.render(onScanSuccess, onScanFailure);
    </script>
  </body>
</html>
"""

# Show scanner
components.html(qr_scanner, height=500)

# Listen to messages sent from JavaScript
qr_container = st.empty()

# FIX : Replace all experimental features with st.query_params updates
if "qrData" not in st.session_state:
    st.session_state["qrData"] = None

# Capture JS → Streamlit messages
def process_qr_message():
    # Streamlit listens to browser messages automatically
    if st.session_state["qrData"]:
        return st.session_state["qrData"]
    return None

# Button to manually trigger read (works when the browser sends a message)
if "qrData" not in st.query_params:
    st.query_params["qrData"] = None

# Detect new QR values sent from frontend
if st.session_state.get("qrData") != st.query_params.get("qrData"):
    st.session_state["qrData"] = st.query_params.get("qrData")

# Display QR code value
qr_result = st.session_state["qrData"]

if qr_result:
    st.success(f"QR détecté : **{qr_result}**")

    # Save scanned ID
    st.session_state["battery_id"] = qr_result

    # Redirect button
    st.page_link("pages/2_Battery_Data.py", label="➡️ Voir les données de la batterie")