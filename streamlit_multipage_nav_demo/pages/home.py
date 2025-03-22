import streamlit as st
import time

# Include custom CSS for Helvetica font
with open("css/default.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Include custom CSS for animations and styling
with open("css/home.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and subtitle with animations
st.title("Welcome to the Dream land 🌟")

x = st.slider('Select a number:', min_value=0, max_value=100)  #👈 this is a widget
st.write(f'{x} squared is {x * x} 🎉')
st.write(f'{x} cubed is {x ** 3} 🚀')
st.write(f'The square root of {x} is {x ** 0.5} 🌿')
st.write(f'{x} doubled is {x * 2} 🔥')


