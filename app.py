import streamlit as st

st.set_page_config(
    page_title="Battery Passport - Hackathon PLM",
    page_icon="🔋",
    layout="centered"
)

# Logo (si tu veux en ajouter un)
# st.image("assets/logo.png", width=180)

st.title("🔋 Battery Passport — Hackathon PLM")

st.markdown("""
Bienvenue dans l'application **Battery Passport** développée pour le hackathon PLM × ESILV.  

Cette solution permet :  
- 📷 **de scanner le QR code d’une batterie**,  
- 🔍 **d’afficher automatiquement les informations liées à cette batterie**,  
- 📄 **de consulter les données contenues dans le Battery Passport**,  
- ♻️ **d’anticiper les workflows Garagiste → Owner → Centre de tri**.  

---

### 🔧 **Fonctionnalités principales**
- **Scan QR Code** : identifiez instantanément une batterie.  
- **Visualisation des données** : accédez à toutes les informations directement depuis un CSV.  
- **Extensions possibles** : télémétrie, logs, décisions, PLM, etc.  

---

### 🚀 **Commencez ici**
Utilisez le menu sur la gauche pour naviguer :

1. **📷 Scanner un QR code**  
2. **📄 Afficher les données associées**  
3. **⚙️ Options / Admin**  

---

### 👥 Équipe Hackathon  
*Nom 1 – Nom 2 – Nom 3*  
ESILV — PLM & Data Hackathon 2025
""")