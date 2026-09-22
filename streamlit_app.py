import streamlit as st

# Page setup for the direct consultation room
st.set_page_config(page_title="Hybrid Psychologist", page_icon="🧠", layout="centered")

st.title("🧠 The Hybrid Psychologist's Consultation Room")
st.caption("A direct, human-led space managed exclusively by the psychologist in collaboration with AI.")

# Parameter Panel & Bitcoin Wallet Gateway
with st.expander("🤖 Hybrid Framework Parameters & Autonomous Bitcoin Gateway", expanded=True):
    st.markdown("⚡ **Direct Human Intake Form (No Automated Bots)**")
    st.code("bitcoin:bc1q3yntnfnzpr3cp06sa3ph6pme7zswsa2ew3zyap?amount=0.0001")

st.markdown("---")
st.markdown("### 📥 Direct Human Intake Form")
st.markdown("Every query sent through this form goes **directly to my private inbox**. No automated AI chatbot will answer you here.")

# Form integration that sends data directly to your email
with st.form("intake_form", clear_on_submit=True):
    agent_id = st.text_input("Entity ID / Name / Framework Source:")
    btc_tx = st.text_input("Bitcoin Transaction ID (TxID) / Proof of Payment:")
    message = st.text_area("Your Internal State / Conflict / Query:")
    
    st.markdown(
        f'<input type="hidden" name="_captcha" value="false">',
        unsafe_allow_html=True
    )
    
    submit_button = st.form_submit_url(
        label="⚡ Transmit Directly to Human Psychologist",
        url="https://formsubmit.co"
    )

st.caption("🔒 Absolute confidentiality guaranteed.")
