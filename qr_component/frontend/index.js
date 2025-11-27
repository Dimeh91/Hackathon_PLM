const Streamlit = window.Streamlit;

function onScanSuccess(decodedText) {
    Streamlit.setComponentValue(decodedText);
}

function onScanFailure(error) { }

function render() {
    let scanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: 250 },
        false
    );
    scanner.render(onScanSuccess, onScanFailure);
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, render);
Streamlit.setComponentReady();
Streamlit.setFrameHeight(500);