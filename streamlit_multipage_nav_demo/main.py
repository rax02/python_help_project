import streamlit as st

home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
contact_us_page = st.Page("pages/contact_us.py", title="Contact Us", icon=":material/phone:")

pg = st.navigation([home_page, contact_us_page])
# Set the page configuration
st.set_page_config(page_title="Data Visualization App", page_icon="📊", layout="centered")

# Include custom CSS for Helvetica font
with open("css/default.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pg.run()