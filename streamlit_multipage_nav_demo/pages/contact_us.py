import streamlit as st

# Include custom CSS for Helvetica font
with open("streamlit_multipage_nav_demo/css/default.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Contact Us")

st.header("Get in Touch")

st.write("Feel free to reach out to us through any of the following methods:")

st.subheader("Email")
st.write("contact@example.com")

st.subheader("Phone")
st.write("+1 234 567 890")

st.subheader("Address")
st.write("1234 Example St, Example City, EX 12345")

st.subheader("Social Media")
st.write("Follow us on Twitter: [@example](https://twitter.com/example)")
st.write("Like us on Facebook: [Example](https://facebook.com/example)")